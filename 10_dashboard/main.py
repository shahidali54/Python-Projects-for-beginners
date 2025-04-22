import dash
from dash import dcc, html

# This is a simple Dash app that displays a header and a graph.
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data':[
                    {'x':[1,2,3],'y':[4,1,2],'type': 'bar', 'name':'Bar Chart'},
                    {'x':[1,2,3],'y':[2,4,5],'type': 'line', 'name':'Line Chart'}
                ],
                'layout': {
                    'title': 'Graph Title',
                    'xaxis': {'title' : 'x-axis'},
                    'yaxis': {'title' : 'y-axis'},
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True, port=8050) 