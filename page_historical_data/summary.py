import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input, State
import app_theme
import pandas as pd


# Create DataFrame
df_submissions_card = pd.DataFrame(app_theme.summary_submission_card_titles, columns=['Title',  "Description", 'Value','Sign'])
df_incidents_card = pd.DataFrame(app_theme.summary_incidents_card_titles, columns=['Title', "Description",'Value', 'Sign'])
df_investigations_card = pd.DataFrame(app_theme.summary_investigations_card_titles, columns=['Title', "Description",'Value', 'Sign'])

def create_card(row):
    cards = dbc.Col([
                dbc.Toast(
                    [
                        dbc.Row([
                            dbc.Col([
                                html.H3(row.Value, className="mb-0"),
                                html.Strong((row.Sign).upper(),style={'display': 'inline-block'}),

                            ], width={'size': 5},style={'textAlign': 'right','padding-right':0}),
                            dbc.Col([
                                html.Small(row.Description, className="mb-0"),
                            ],width={'size':7},style={'textAlign': 'left','padding-left':'5px'}),

                        ])
                     ],
                    header=[html.Small(row.Title, className="mb-0")]
                )
        ], #width={'size': app_theme.summary_card_widths},
            style={'padding-right': '0px',
                   'padding-top': '10px',
                   })
    return cards

submissions_cards = df_submissions_card.apply(lambda x: create_card(x), axis=1).to_list()
incidents_cards = df_incidents_card.apply(lambda x: create_card(x), axis=1).to_list()
investigations_cards = df_investigations_card.apply(lambda x: create_card(x), axis=1).to_list()

summary_submissions = html.Div([dbc.Row(submissions_cards,style={"flexWrap": "nowrap"})],style={'overflowX': 'scroll'})
summary_incidents = html.Div([dbc.Row(incidents_cards,style={"flexWrap": "nowrap"})],style={'overflowX': 'scroll'})
summary_investigations = html.Div([dbc.Row(investigations_cards,style={"flexWrap": "nowrap"})],style={'overflowX': 'scroll'})


