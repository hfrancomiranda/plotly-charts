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
import plotly.subplots as sp
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
                "font": {'size': 15}  # Adjust the font size here
            }
        ]
    )

    fig.write_image(f'docs/{person}_gauge_chart.png')


# create tables
family_listing = df.loc[(df['Order By'].isnull()), :]

for name in family_listing['Name'].unique():
    filtered_df = family_listing.loc[(family_listing['Name'] == name), :]
    # Creating a table using Plotly Graph Objects with custom header style
    fig2 = go.Figure(data=[go.Table(
        header=dict(values=list(filtered_df.columns),
                    fill_color='navy',  # Set header background color
                    font=dict(color='white', size=14)),  # Set font color and size
        cells=dict(values=[filtered_df[col] for col in filtered_df.columns]))
    ])

    # Customizing the layout
    fig2.update_layout(
        title='Customized Table',
        # margin=dict(l=10, r=10, t=60, b=10),  # Adjust margins
        # height=300,  # Set the height of the table
        # autosize=False,  # Disable autosizing
        # width=500,  # Set the width of the table
    )

    # Show the figure
    fig2.show()
