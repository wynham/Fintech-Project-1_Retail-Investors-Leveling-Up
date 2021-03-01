#this is the imports section of the code - all of these are necessary for the program to run properly

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries 
import dash                               
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc   



#in this section the User will type in the ticker they want displayed in the DASH application

# ATTENTION: Please enter your stock in the ticker string below

ticker = 'TSLA'

# Once ticker is entered, save the file and the dash app will automatically update
# In this section we make the API call and select which columns to pull data from. We'll use an interval of every 5 minutes

key = 'RLVN7TWQW8MB1ZI3'
ts = TimeSeries(key, output_format='pandas')
ttm_data, ttm_meta_data = ts.get_intraday(symbol=ticker,interval='5min', outputsize='compact')
df = ttm_data.copy()
df=df.transpose()
df.rename(index={"1. open":"open", "2. high":"high", "3. low":"low", "4. close":"close","5. volume":"volume"},inplace=True)
df=df.reset_index().rename(columns={'index': 'indicator'})
df = pd.melt(df,id_vars=['indicator'],var_name='date',value_name='rate')
df = df[df['indicator']!='volume']

#the dataframe is then saved into a CSV file each time a new ticker is selected by the User 

df.to_csv("api_data.csv", index=False)


#The progeram then reads the saved CSV file

dff = pd.read_csv("api_data.csv")
dff = dff[dff.indicator.isin(['high'])]

#this is the main setup for the DASH app

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}])

#this section sets up the layout for the DASH app

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader("Fintech Intraday Stock Analyzer - Alpha Vantage API"),
                    
                    dbc.CardImg(
                        src="/assets/berkeleylogo1.png",
                        top=True,
                        style={"width": "12rem"},
                        className="ml-3"),
                        
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.P("Stock: " + ticker, className="ml-3")
                            ],width={'size':5, 'offset':1}),

                            dbc.Col([
                                dcc.Graph(id='indicator-graph', figure={},
                                          config={'displayModeBar':False},
                                          )
                            ], width={'size':3,'offset':2})
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='daily-line', figure={},
                                          config={'displayModeBar':False})
                            ], width=12)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dbc.Button("Click here to purchase or sell stock", color="primary", block=True)
                            ], width=9)
                        ], justify="center")
                    ]),
                ],
                style={"width": "40rem"},
                className="mt-3"
            )
        ], width=6)
    ], justify='center'),
    dcc.Interval(id='update', n_intervals=0, interval=1000*500)
])

#Here we setup the DASH app callback for the Indicator Graph. The indicator graph shows the percent change for the stock over the course of the day
#It will either display numbers in green if there was a positive change, or red if there was a negative change in the stocks value over the course of the day

@app.callback(
    Output('indicator-graph', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    dff_rv = dff.iloc[::-1]
    day_start = dff_rv[dff_rv['date'] == dff_rv['date'].min()]['rate'].values[0]
    day_end = dff_rv[dff_rv['date'] == dff_rv['date'].max()]['rate'].values[0]

    fig = go.Figure(go.Indicator(
        mode="delta",
        value=day_end,
        delta={'reference': day_start, 'relative': True, 'valueformat':'.2%'}))
    fig.update_traces(delta_font={'size':12})
    fig.update_layout(height=30, width=70)

    if day_end >= day_start:
        fig.update_traces(delta_increasing_color='green')
    elif day_end < day_start:
        fig.update_traces(delta_decreasing_color='red')

    return fig

# Here we setup the DASH app callback for the Line Graph. Similarly, it will display a green line with green filling underneath if there was a positive change
# Or it wil display a red line with red filling underneath if there was a negative change over the course of the day
@app.callback(
    Output('daily-line', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    dff_rv = dff.iloc[::-1]
    fig = px.line(dff_rv, x='date', y='rate',
                   range_y=[dff_rv['rate'].min(), dff_rv['rate'].max()],
                   height=120).update_layout(margin=dict(t=0, r=0, l=0, b=20),
                                             paper_bgcolor='rgba(0,0,0,0)',
                                             plot_bgcolor='rgba(0,0,0,0)',
                                             yaxis=dict(
                                             title=None,
                                             showgrid=False,
                                             showticklabels=False
                                             ),
                                             xaxis=dict(
                                             title=None,
                                             showgrid=False,
                                             showticklabels=False
                                             ))

    day_start = dff_rv[dff_rv['date'] == dff_rv['date'].min()]['rate'].values[0]
    day_end = dff_rv[dff_rv['date'] == dff_rv['date'].max()]['rate'].values[0]

    if day_end >= day_start:
        return fig.update_traces(fill='tozeroy',line={'color':'green'})
    elif day_end < day_start:
        return fig.update_traces(fill='tozeroy',
                             line={'color': 'red'})

# The final function that makes the DASH app run

if __name__=='__main__':
    app.run_server(debug=True, port=3000)


# After the program runs, navigate to this link (http://127.0.0.1:3000/) to run the program. This link will also display in your terminal below