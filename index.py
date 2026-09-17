from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your pages
from apps import home, dashboard, data, about

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content', children=[]),

    html.Div(
        [
            html.Div([
                html.Div([
                    html.Img(src="/assets/statistics.png", style={"width": "4.9rem"}),
                    html.H5("Sales Dashboard", style={'color': 'white', 'margin-top': '20px'}),
                ], className='image_title')
            ], className="sidebar-header"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-house"),
                        html.Span("Home", style={'margin-top': '3px'})], className='icon_title')],
                        href="/apps/home",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("Dashboard", style={'margin-top': '3px'})], className='icon_title')],
                        href="/apps/dashboard",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-database"),
                        html.Span("Data", style={'margin-top': '3px'})], className='icon_title')],
                        href="/apps/data",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-circle-info"),
                        html.Span("About", style={'margin-top': '3px'})], className='icon_title')],
                        href="/apps/about",
                        active="exact",
                        className="pe-3"
                    ),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        id="bg_id",
        className="sidebar",
    )

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname in ('/', '/apps/dashboard'):
        return dashboard.layout
    elif pathname == '/apps/home':
        return home.layout
    elif pathname == '/apps/data':
        return data.layout
    elif pathname == '/apps/about':
        return about.layout
    return html.Div([
        html.H3('404: Page not found', style={'color': 'white', 'padding': '20px'})
    ])


if __name__ == '__main__':
    app.run_server(debug=False, host='127.0.0.1', port=8051)
