import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='Date')

fig = px.line(df, x='Date', y='Sales')
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales'
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(id='header', children='Pink Morsel Sales Visualiser'),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
