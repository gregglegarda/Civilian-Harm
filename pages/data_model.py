from page_data_model import bar
import dash
import dash_bootstrap_components as dbc
from dash import html
import app_theme

dash.register_page(__name__, path='/data_model')



layout = html.Div([
    # BAR ROW
    # already using containers, no need to contain
    html.Div([bar.headerbar]),
    html.Div([bar.navbar]),

    # MAIN CONTENT ROW
    dbc.Container([
            dbc.Button('Enter MIP/MIM Model Page', href='https://www.mimworld.org/html/2.0/index.htm'),
            dbc.Tabs([
                dbc.Tab(dbc.Card([
                    html.A([
                        html.Img(alt="Data Model",src="assets/conceptual_model.svg",style={'width':'100%'}
                    )],href="/data_model",),
                    ], style={'padding': '10px', 'background':app_theme.card_border_color}
                ), label="Conceptual Model (ERD)"),
                dbc.Tab(dbc.Card([
                    html.A([
                        html.Img(alt="Data Model",src="assets/logical_model.svg",style={'width':'100%'}
                    )],href="/data_model",),
                    ], style={'padding': '10px', 'background':app_theme.card_border_color}
                ), label="Logical Model (Expanded ERD)"),
                dbc.Tab(label="Physical Model (Database Schema and DDL Scripts)"),
                dbc.Tab(label="Network Model"),
                dbc.Tab(label="Hierarchical Model"),
                dbc.Tab(label="Data Schemas"),
            ],style = app_theme.tab_style),


    ], fluid=True,
        style={'background-color': app_theme.visual_card_background_color,
               'padding-top': '10px',
               # 'padding-bottom':'10px'
               }),
])
