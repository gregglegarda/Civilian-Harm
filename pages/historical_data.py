import app_theme
from page_historical_data import bar, tabs
import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path='/historical_data')

layout = html.Div([
    # BAR ROW
    # already using containers, no need to contain
    html.Div([bar.headerbar]),
    html.Div([bar.navbar]),

    # MAIN CONTENT ROW
    dbc.Container([
        dbc.Row([
            # COLUMN CONTROLS
            dbc.Col(
                # CONTROLS CARD
                tabs.tabs_panel,
                width={'size': 3},
                style={'background-color': app_theme.visual_card_background_color,  # 'blue',
                       # 'padding-left':'0'
                       }),

            # COLUMN VISUAL
            dbc.Col(
                # TABS

                tabs.tabs_main,  # content is in tabs

                width={'size': 9},
                style={'background-color': app_theme.visual_card_background_color,
                       'padding-left': '0'
                       }),
        ])
    ], fluid=True,
        style={'background-color': app_theme.visual_card_background_color,
               'padding-top': '10px',
               # 'padding-bottom':'10px'
               }),

    # LOWER CONTENT ROW
    dbc.Container([
        dbc.Row([
            # SUMMARY
            tabs.tabs_lower  # content is in tabs
        ], style={'padding': '10px',
                  })
    ], fluid=True,
        style={'background-color': app_theme.visual_card_background_color}
    )
])
