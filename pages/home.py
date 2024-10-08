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
                        html.Img(alt="MIM",src="assets/mim.png",style={'width':'100%'}
                    )],href="https://www.mimworld.org/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})


card4 = dbc.Card([
                    html.A([
                        html.Img(alt="Submit Incident",src="assets/incident_form.png",style={'width':'100%'}
                    )],href="/incident_form"),
], style={'padding': '10px', 'background':app_theme.card_border_color})


card5 = dbc.Card([
                    html.A([
                        html.Img(alt="OMNI",src="assets/omni.png",style={'width':'100%'}
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
                        html.Img(alt="Advana",src="assets/advana.png",style={'width':'100%'}
                    )],href="https://www.boozallen.com/d/insight/thought-leadership/advanced-enterprise-analytics-at-the-defense-department.html"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card9 = dbc.Card([
                    html.A([
                        html.Img(alt="Databricks",src="assets/databricks.png",style={'width':'100%'}
                    )],href="https://www.databricks.com/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card10 = dbc.Card([
                    html.A([
                        html.Img(alt="Tableau",src="assets/tableau.png",style={'width':'100%'}
                    )],href="https://www.tableau.com/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card11 = dbc.Card([
                    html.A([
                        html.Img(alt="Servicenow",src="assets/servicenow.png",style={'width':'100%'}
                    )],href="https://www.servicenow.com/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card12 = dbc.Card([
                    html.A([
                        html.Img(alt="QLIK",src="assets/qlik.png",style={'width':'100%'}
                    )],href="https://www.qlik.com/us"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

card13 = dbc.Card([
                    html.A([
                        html.Img(alt="NIEM",src="assets/niem.png",style={'width':'100%'}
                    )],href="https://www.niem.gov/"),
], style={'padding': '10px', 'background':app_theme.card_border_color})

layout = html.Div([
    # BAR ROW
    # already using containers, no need to contain
    html.Div([bar.headerbar]),
    html.Div([bar.navbar]),

    # MAIN CONTENT ROW
    dbc.Container([
            dbc.Row([
                html.Div([html.Img(src=r'assets/logo.svg',
                                   style={'padding': '50px', 'padding-bottom': '10px', 'padding-top': '10px',
                                          'width': '20%', 'justify': 'center'}, className='center')],
                         style={'width': '100','textAlign': 'center'}),
                html.H2(["DATA MANAGEMENT PLATFORM"],style={'textAlign': 'center'}),
                html.H4(["CIVILIAN HARM MITIGATION AND RESPONSE"],style={'textAlign': 'center', 'padding-bottom': '50px'}),
                html.Hr(style={'textAlign': 'center'})
            ]),

            dbc.Row([
                html.H6(["VISUALIZATIONS AND DASHBOARDS"],style={'textAlign': 'left'}),
                dbc.Col([card1], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card10], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card12], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card2], width={'size': 2}, style={'padding': '50px'}),
                html.Hr(style={'textAlign': 'center'}),

                html.H6(["DATA MODELS"],style={'textAlign': 'left'}),
                dbc.Col([card3], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card6], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card13], width={'size': 2}, style={'padding':'50px'}),
                html.Hr(style={'textAlign': 'center'}),

                html.H6(["FORMS"],style={'textAlign': 'left'}),
                dbc.Col([card4], width={'size': 2}, style={'padding': '50px'}),
                html.Hr(style={'textAlign': 'center'}),

                html.H6(["DATA STORES AND DATABASE"],style={'textAlign': 'left'}),
                dbc.Col([card5], width={'size': 2}, style={'padding': '50px'}),
                dbc.Col([card7], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card8], width={'size': 2}, style={'padding':'50px'}),
                html.Hr(style={'textAlign': 'center'}),

                html.H6(["ANALYTICS"],style={'textAlign': 'left'}),
                dbc.Col([card9], width={'size': 2}, style={'padding':'50px'}),
                dbc.Col([card11], width={'size': 2}, style={'padding':'50px'}),

            ]),

    ], fluid=True,
        style={'background-color': app_theme.visual_card_background_color,
               'padding-top': '40px',
               # 'padding-bottom': '10px',
               }),
])
