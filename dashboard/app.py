import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.Div([
        html.H1("Data Visualization", className="text-center"),
        dcc.Tabs([
            dcc.Tab([html.Div([html.Br(),
                    dcc.Dropdown(options= data_visualization["Province"].unique(), value='ON' ,id="1"),
                    dcc.Dropdown(options= ['Price', 'Number_Beds', 'Number_Baths', 'Population','Median_Family_Income', 'n_city'], value="Price", id = "2"),
                    dcc.Graph(id="figure 1")]),
                    html.Div([html.Br(),
                    dcc.Dropdown(options= data["Province"].unique(), value='ON' ,id="3"),
                    dcc.Graph(id = "figure 2"),
                    dcc.Graph(id = "figure 3")]),
                    html.Div([
                    dcc.Tabs([
                    dcc.Tab(html.Div([
                    html.H4('Most and Least Expensive Cities'),
                    dcc.Graph(id="graph"),
                    html.P("Subplots Width:"),
                    dcc.Slider(
                    id='slider-width', min=.2, max=.8,
                    value=0.5, step=0.1)]),
                    label = "Average Price in each Cities"),
])
])
                             ],
                    label = "Cities"),
            dcc.Tab([html.Div([html.Br(),
                    dcc.Dropdown(options= ['Price', 'Number_Beds', 'Number_Baths', 'Population','Median_Family_Income', 'n_province'], value='Price' ,id="4"),
                    dcc.Graph(id="figure 4")]),
                    html.Div([html.Br(),
                    dcc.Dropdown(options= data['Province'].unique(), value='ON' ,id="5"),
                    dcc.Graph(id = "figure 5"),
                    dcc.Graph(id = "figure 6")
                              ])],
                    label = "Provinces")
])
])
])

# Add controls to build the interaction
@callback(
    [Output(component_id='figure 1', component_property='figure'), Output(component_id='figure 2', component_property='figure'),
     Output(component_id = 'figure 3', component_property='figure'), Output("graph", "figure")],
    [Input(component_id='1', component_property='value') , Input(component_id='2', component_property='value'),
     Input(component_id='3', component_property='value') , Input("slider-width", "value")]
)

def update_graph(col_chosen1, col_chosen2, col_chosen3, left_width):
    fig1 = px.histogram(data_visualization[data_visualization["Province"] == col_chosen1], x = "City", y= col_chosen2, histfunc='avg').update_xaxes(categoryorder="total descending")
    fig2 = px.violin(data[data["Province"]== col_chosen3], y = "Price", color="City" , hover_data= ["City","Number_Beds","Number_Baths","Population","Median_Family_Income"])
    fig3 = px.pie(data[data["Province"] == col_chosen3], "City")

    graph = make_subplots(rows=1, cols=2, column_widths=[left_width, 1 - left_width])
    graph.add_trace(go.Bar(x=top10_city["City"], y=top10_city["Price"]), row = 1, col = 1)
    graph.add_trace(go.Line(x=top10_city["City"], y=top10_city["Price"]), row = 1, col = 1, )
    graph.add_trace(go.Bar(x=low10_city["City"], y=low10_city["Price"]), row = 1, col = 2, )
    graph.add_trace(go.Line(x=low10_city["City"], y=low10_city["Price"]), row = 1, col = 2)
    fig1.write_html("fig1.html")
    return fig1, fig2, fig3, graph

@callback(
    [Output(component_id='figure 4', component_property='figure'), Output(component_id='figure 5', component_property='figure'), Output(component_id='figure 6', component_property='figure')],
    [Input(component_id='4', component_property='value'), Input(component_id='5', component_property='value')]
)

def update_graph(col_chosen4, col_chosen5):
    fig4 = px.histogram(data_visualization, x = "Province", y= col_chosen4, histfunc='avg').update_xaxes(categoryorder="total descending")
    fig5 = px.pie(data[data["Province"] == col_chosen5],"City")
    fig6 = px.violin(data, y="Price", color="Province", hover_data= ["City","Number_Beds","Number_Baths","Population","Median_Family_Income"], box=True)
    return fig4, fig5, fig6


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
