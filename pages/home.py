from page_home import bar
import dash
import dash_bootstrap_components as dbc
from dash import html
import app_theme

dash.register_page(__name__, path='/')




card1 = dbc.Card([
                    html.A([
                        html.Img(alt="Explore Data Page",src="assets/explore_data.png",style={'width':'100%'}
                    )],href="/historical_data",),
 ], style={'padding': '10px', 'background':app_theme.card_border_color})


card2 = dbc.Card([
                    html.A([
                        html.Img(alt="Interactive Map Page",src="assets/interactive_map.png",style={'width':'100%'}
                    )],href="/interactive_map",),
], style={'padding': '10px', 'background':app_theme.card_border_color})


card3 = dbc.Card([
                    html.A([
                        html.Img(alt="Records",src="assets/records.png",style={'width':'100%'}
                    )],href="/incident_form"),
], style={'padding': '10px', 'background':app_theme.card_border_color})


card4 = dbc.Card([
                    html.A([
                        html.Img(alt="Submit Incident",src="assets/incident_form.png",style={'width':'100%'}
                    )],href="/incident_form"),
], style={'padding': '10px', 'background':app_theme.card_border_color})


card5 = dbc.Card([
                    html.A([
                        html.Img(alt="Data Bases",src="assets/databases.png",style={'width':'100%'}
                    )],href="/data_model",),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card6 = dbc.Card([
                    html.A([
                        html.Img(alt="Data Model",src="assets/data_model.png",style={'width':'100%'}
                    )],href="/data_model",),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card7 = dbc.Card([
                    html.A([
                        html.Img(alt="Intelink",src="assets/intelink.png",style={'width':'100%'}
                    )],href="https://www.intelink.gov/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card8 = dbc.Card([
                    html.A([
                        html.Img(alt="Intelink",src="assets/intelink.png",style={'width':'100%'}
                    )],href="https://www.intelink.gov/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

layout = html.Div([
    # BAR ROW
    # already using containers, no need to contain
    html.Div([bar.headerbar]),
    html.Div([bar.navbar]),

    # MAIN CONTENT ROW
    dbc.Container([
            dbc.Row([
                html.H3(["DATA MANAGEMENT PLATFORM"],style={'textAlign': 'center'}),
                html.H6(["CIVILIAN HARM MITIGATION AND RESPONSE"],style={'textAlign': 'center'})
            ]),
            dbc.Row([
                dbc.Col([card1], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card2], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card3], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card4], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card5], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card6], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card7], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card8], width={'size': 2}, style={'padding':'50px'}),
            ]),
    ], fluid=True,
        style={'background-color': app_theme.visual_card_background_color,
               'padding-top': '40px',
               # 'padding-bottom': '10px',
               }),
])
