# Fintech Project 1 - Retail Investors: Leveling Up

The ease of access to company information for the average retail investor is relatively limited. They might hear about a stock in the news or see trading charts that reflect price, but that information isn't usually available in the same place as long-term data/information about company. Our goal with this project is to bridge that gap. Our aim is to provide the average retail investor with long term data along with intraday charts in the same place, so they can make educated purchasing decisions on stocks.

Our goal was to create a dashboard where investors can see detailed company information all in one place. 

Part 1 - Long term hitorical data:

Part 2 - Intraday Data Displayed:

---

## Technologies

Part 1:

[fire](fire) - for the command line interface

[questionary](questionary) - gives ability to interact with the user and recieve user input in program

[sys](sys) - system-specific parameters and functions

[csv](csv) - for reading and writing .csv files


Part 2:

[import pandas as pd](import pandas as pd) - for the command line interface

[import plotly.express as px](import plotly.express as px) - gives ability to interact with the user and recieve user input in program

[from alpha_vantage.timeseries import TimeSeries](from alpha_vantage.timeseries import TimeSeries) - system-specific parameters and functions

[import dash](import dash) - for reading and writing .csv files

[mport dash_core_components as dcc](mport dash_core_components as dcc)

[import dash_html_components as html](import dash_html_components as html)

[from dash.dependencies import Output, Input](from dash.dependencies import Output, Input)

[import dash_bootstrap_components as dbc](import dash_bootstrap_components as dbc)

---

## Installation Guide

Install the following in your conda dev environment

Part 1:

```python
pip install fire
pip install questionary
pip install pytest
```
Part 2: 

```python
pip install fire
pip install questionary
pip install pytest
```

---

## Examples

make sure you activate your conda dev environment (python 3.8) before running the code:
```
conda activate dev
```
When prompted for .csv file, enter the following for this program:
```
data/daily_rate_sheet.csv
```
---

## Usage

This image shows an example of an user entering their information in the loan qualifier application:

![usage_example.png](usage_example.png)


The following csv file is created from this example:

![created_csv_example.png](created_csv_example.png)

---

## Contributors

UCB Fintech Bootcamp, Gabriel Silva & Wynham Guillemot 

---

## License

MIT License

Copyright (c) [2021] [UCB Fintech Bootcamp, Gabriel Silva & Wynham Guillemot]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
