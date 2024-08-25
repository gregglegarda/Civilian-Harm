from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import app_theme
import data_connection



controls =  html.Div([
                #html.Div([dbc.Label("Panel Controls")],style={'text-align':'center'}),

            dbc.Card(dbc.CardBody([
                        #SELECT TYPE

                        #dbc.Label('Combatant Commands:'),
                        #dcc.RadioItems(data_connection.df_incidents.CombatantCommand.unique(),data_connection.df_incidents.CombatantCommand.unique()[1],inline=True,labelStyle= {'margin':'5px'}),


                        #html.Hr(style={"line-height": "5px", "line-color": "white"}),
                        dbc.Label("Timeline Selection"),
                        dcc.RadioItems(app_theme.class_types,app_theme.class_types[0],inline=True,labelStyle= {"margin":"5px"}),


                        html.Hr(style={"line-height": "5px", "line-color": "white"}),
                        dbc.Label("Aggregate Data:"),
                        dcc.RadioItems(["Yearly","Monthly",],"Yearly",inline=True,labelStyle= {"margin":"5px"}),


                        html.Hr(style={"line-height": "5px", "line-color": "white"}),
                        dbc.Label("Filter Records:"),
                        dbc.Select(["CHMR DMP DB0 (staging))","CHMR DMP DB1 (standard))","CHMR DMP DB2 (reporting))",],placeholder="Select Database (Redis DB)...", className="mb-3"),
                        dbc.Select(["submission","incident", "investigation", "organization",],placeholder="Select Table (Redis Keys)...", className="mb-3"),
                        dbc.Select(data_connection.df_incidents.columns,placeholder="Select Column...", className="mb-3"),
                        dbc.Input(placeholder="Search Column...", className="mb-3"),
                        dbc.Button("Update", className="me-1"),
                        dbc.Button("Show Details", className="me-1")


            ], style={'overflowY': 'scroll'}),className="h-100",
            ),
],style= {
'height': app_theme.controls_view_height,
'padding-top':'5px',
'background-color':app_theme.controls_card_background_color,
},)
