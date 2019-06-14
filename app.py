#Dependencies - dash, plotly, pandas libraries required
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go


#Reading map.csv
df = pd.read_csv('map.csv')


#Utilized openly available css file to align elements
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



#Reference - https://dash.plot.ly/dash-core-components
app.layout = html.Div([html.Div([html.H1("Expected Multivariate Testing Duration Across Countries")],
                                style={'textAlign': "center", "padding-bottom": "30"}),
                       html.Div([html.Span("Expected Experiment Duration (in weeks) for specific Webpage : ", className="six columns",
                                           style={"text-align": "right", "width": "40%", "padding-top": 10}),
                                 dcc.Dropdown(id="value-selected", value='lifeExp',
                                              options=[{'label': 'Home Page', 'value': 'homepage'},
                                                       {'label': "Checkout Page", 'value': 'checkout'},
                                                       {'label': "Merchant Page", 'value': 'merchant'}],
                                              style={"display": "block", "margin-left": "auto", "margin-right": "auto",
                                                     "width": "70%"},
                                              className="six columns")], className="row"),
                       dcc.Graph(id="my-graph"),
                       dcc.Graph (id="my-graph2",figure=go.Figure(
        data=[
            go.Bar(
                x=['US','India','Germany','Italy','China','Mexico','UK','Russia','Japan','Netherlands'],
                y=[0.343,1.422,1.443,1.545,1.574,1.711,2.297,2.421,2.913,3.329],
                name='Homepage Experiment Expected Duration (In increasing number of weeks)',
                marker=go.bar.Marker(
                    color='rgb(55, 83, 109)'
                )
            )
        ],
        layout=go.Layout(
            title='10 Best Countries to conduct Homepage Experiment',
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1.0
            ),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300}
                               
                               
                               
                               
                               
                               ),
            dcc.Graph (id="my-graph3",figure=go.Figure(
        data=[
            go.Bar(
                x=['US','China','UK','Japan','India','France',' Germany','Philippines','Saudi Arabia','Russia'],
                y=[0.659,0.814,2.871,3.800,3.952,4.178,6.466,8.308,8.807,9.129],
                name='Checkout Experiment Expected Duration (In increasing number of weeks)',
                marker=go.bar.Marker(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=go.Layout(
            title='10 Best Countries to conduct Checkout Experiment',
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1.0
            ),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300}
                               
                               ),
            
            dcc.Graph (id="my-graph4",figure=go.Figure(
        data=[
            go.Bar(
                x=['US','India','Bangladesh'],
                y=[9.518,674.873,1225.751],
                name='Merchant Page Experiment Expected Duration (In increasing number of weeks)',
                marker=go.bar.Marker(
                    color='rgb(238,130,238)'
                )
            )
        ],
        layout=go.Layout(
            title=' Best Countries to conduct Merchant Page Experiment',
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1.0
            ),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300}
                               
                               )
            
                       ], className="container")


@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("value-selected", "value")]
)
def update_figure(selected):
    dff = df.groupby(['ccthree', 'country']).mean().reset_index()
    def title(text):
        if text == 'homepage':
            return "Home Page"
        elif text == 'checkout':
            return "Checkout Page"
        else:
            return "Merchant Page"
    trace = go.Choropleth(locations=dff['ccthree'],z=dff[selected],text=dff['country'],autocolorscale=False,
                          colorscale= 'Viridis', marker={'line': {'color': 'rgb(255,255,255)','width': 2}},
                          colorbar=dict({"thickness": 10,"len": 0.3,"x": 1.1,"y": 0.7,
                                    'title': {"text": title(selected), "side": "bottom"}}))
    return {"data": [trace],
            "layout": go.Layout(title=title(selected),height=800,geo={'showframe': False,'showcoastlines': False,
                                                                      'projection': {'type': "miller"}})}

# =============================================================================
# app.layout = html.Div( children=[
#     html.H1(children='Hello Chicks'),
# 
#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),
# 
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization',
#                 
#         }
#             }
#                 
#     ),
# 
# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montréal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value='MTL'
# )
# ])
# =============================================================================

# =============================================================================
if __name__ == '__main__':
    app.run_server()
# =============================================================================

