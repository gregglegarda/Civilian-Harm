import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input, State
import app_theme
import data_connection


df = data_connection.df_submissions
df = data_connection.df_incidents
df = data_connection.df_investigations

dag_grid = dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            className="ag-theme-alpine-dark",
            columnSize="sizeToFit",
            style={'height': '100%'}
            )

records = html.Div([
    html.Div(dag_grid,style={'height': '100%'})
], style= {'padding':'5px',
           'background-color':app_theme.visual_container_color,
           'height': app_theme.visual_view_height,})
