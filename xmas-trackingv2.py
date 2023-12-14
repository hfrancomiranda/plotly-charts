
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
Location = r'/docs/details.xlsx'

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

    fig.show()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab([
            html.Div([
                dbc.Row(['2023 Xmas Tracking'],
                        style={'font-weight': 'bold', 'font-size': '30px', 'padding': '20px'}, justify='center'),
                dbc.Row([
                    # first table
                    dbc.Col(html.Div(dash_table.DataTable(data=df.to_dict('records'),
                                                          columns=[{'id': c, 'name': c,
                                                                    'presentation': 'markdown'} if c == 'Link' else {
                                                              'id': c, 'name': c} for c in df.columns],
                                                          markdown_options={'html': True},
                                                          filter_action='native',
                                                          editable=True,
                                                          sort_action='native',
                                                          sort_mode='single',
                                                          page_current=0,
                                                          page_size=12,
                                                          style_cell={
                                                              'whiteSpace': 'normal',
                                                              'height': 'auto',
                                                              'maxWidth': '600px',  # for all cols
                                                              'minWidth': '100px',  # for all cols
                                                              'textAlign': 'left'
                                                          },
                                                          style_data={
                                                              'color': 'black',
                                                              'backgroundColor': 'white'
                                                          },
                                                          style_data_conditional=[
                                                              {
                                                                  'if': {'row_index': 'odd'},
                                                                  'backgroundColor': 'lightblue',
                                                                  # set background color for odd rows
                                                              },

                                                              {
                                                                  'if': {'row_index': 'even'},
                                                                  'backgroundColor': 'white',
                                                                  # set background color for even rows
                                                              }
                                                          ],
                                                          style_header={
                                                              'backgroundColor': '#000080',  # blue background color
                                                              'textAlign': 'center',  # center align column headers
                                                              'color': 'white',  # white font color
                                                              'fontWeight': 'bold'  # bold font
                                                          },
                                                          style_table={'width': '60%'}))),


                ])
            ])
        ])
    ])
], className='dbc')

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)







