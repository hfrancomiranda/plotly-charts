import dash
from dash import dcc, html
import plotly.express as px

# Sample data
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 12, 8, 15, 7]
}

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1("Dash Plotly Example"),
    
    # Scatter plot using Plotly Express
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(data, x='X', y='Y', title='Scatter Plot')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)


