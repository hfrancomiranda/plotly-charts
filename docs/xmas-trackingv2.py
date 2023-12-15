
import pandas as pd
import warnings
import plotly.graph_objects as go
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html
import numpy as np
import warnings
from dash import dcc
import plotly.graph_objs as go
import plotly.express as px
from dash import dash_table
warnings.filterwarnings('ignore')

# import file
Location = r'docs/details.xlsx'

# read file
df = pd.read_excel(Location, sheet_name='details')

family_purchases = df[['Name', 'Price']].loc[(df['Order By'] == 'Us'), :].groupby('Name').sum().reset_index()

# Convert DataFrame to dictionary
my_dict = dict(zip(family_purchases['Name'], family_purchases['Price']))

total_budget = 375

# Create a gauge chart for each person
for person, purchases_to_date in my_dict.items():
    # Calculate the percentage of purchases to date compared to the total budget
    percentage_purchases = (purchases_to_date / total_budget) * 100

    # Create a gauge chart
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=percentage_purchases,
        title={'text': f"{person}'s Purchases vs Total Budget"},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))

    fig.update_layout(
        template="plotly_dark",
        annotations=[
            {
                "x": 0.5,
                "y": 0.5,
                "text": f"{person}'s Purchases: {purchases_to_date}<br>Total Budget: {total_budget}<br>{percentage_purchases:.2f}%",
                "showarrow": False,
                "font": {'size': 20}  # Adjust the font size here
            }
        ]
    )

    fig.write_image(f'docs/assets/images/{person}_gauge_chart.png')










