import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='Date')

app = dash.Dash(__name__)

colors = {
    'background': '#1e1e1e',
    'text': '#ff69b4',
    'text_light': '#ffffff'
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'fontFamily': 'sans-serif', 'padding': '40px', 'minHeight': '100vh'}, children=[
    html.H1(
        id='header', 
        children='Pink Morsel Sales Visualiser',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'marginBottom': '30px'
        }
    ),
    
    html.Div(
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            style={
                'color': colors['text_light'], 
                'display': 'flex', 
                'justifyContent': 'center', 
                'gap': '25px', 
                'fontSize': '18px', 
                'marginBottom': '40px'
            }
        )
    ),
    
    dcc.Graph(
        id='sales-line-chart'
    )
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]
        
    fig = px.line(filtered_df, x='Date', y='Sales')
    
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text_light'],
        title_font_color=colors['text'],
        xaxis_title='Date',
        yaxis_title='Sales',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#333333')
    )
    
    fig.update_traces(line_color=colors['text'], line_width=2)
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)