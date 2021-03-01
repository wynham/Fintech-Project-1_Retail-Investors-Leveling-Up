# Fintech Project 1 - Retail Investors: Leveling Up

The ease of access to company information for the average retail investor is relatively limited. They might hear about a stock in the news or see trading charts that reflect price, but that information isn't usually available in the same place as long-term data/information about company. Our goal with this project is to bridge that gap. Our aim is to provide the average retail investor with long term data along with intraday charts in the same place, so they can make educated purchasing decisions on stocks.

Our goal was to create a dashboard where investors can see detailed company information all in one place. 

Part 1 - Long term hitorical data:

Part 2 - Intraday Data Displayed:

---

## Technologies

Part 1:

[json](json) - to interact with JSON files in Python

[pandas](pandas) - Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both   easy and intuitive

[path](path) - to find files and read them into the program

[NumPy](NumPy) - NumPy is a Python library used for working with arrays

[hvplot](hvplot) - to visualize data in interactive graphs.


Part 2:


```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries 
import dash                               
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc  
```

---

## Installation Guide

Install the following in your conda dev environment

Part 1:

```python
pip install path
pip install pandas
pip install json
pip install numpy
pip install hvplot
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
