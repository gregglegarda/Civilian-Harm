import app_theme
import dash_leaflet as dl
import dash_bootstrap_components as dbc
import app_theme
import data_connection
from dash import Dash, html, dcc, callback, Output, Input, State

color_submissions = app_theme.marker_color_submissions
color_incidents = app_theme.marker_color_incidents
color_investigations = app_theme.marker_color_investigations
radius = 50





def create_marker_content(df, row):
    content_columns = df.columns.to_list()
    content_list = ["<b>" + x + ":</b> " + str(row[x]) + "<br>" for x in content_columns]
    content = ' '.join(content_list)
    return content


def create_marker_submission(row):
    markers = dl.Circle(center=[row.SubmissionLat, row.SubmissionLong], radius=radius, color=color_submissions,
                        children=[dl.Popup(
                            maxHeight = 100,
                            maxWidth=500,
                            content= create_marker_content(data_connection.df_submissions, row)

                                )])
    return markers

def create_marker_incident(row):
    markers = dl.Circle(center=[row.IncidentLat, row.IncidentLong], radius=radius, color=color_incidents,
                        children=[dl.Popup(
                            maxHeight = 100,
                            maxWidth=500,
                            content=create_marker_content(data_connection.df_incidents, row)
                                )])
    return markers

def create_marker_investigation(row):
    markers = dl.Circle(center=[row.InvestigationLat, row.InvestigationLong], radius=radius, color=color_investigations,
                        children=[dl.Popup(
                            maxHeight = 100,
                            maxWidth=500,
                            content=create_marker_content(data_connection.df_investigations, row)
                                )])
    return markers