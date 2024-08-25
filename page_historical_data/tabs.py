import dash_bootstrap_components as dbc

import app_theme
from page_historical_data import panel_controls, summary, visual_aggregated, visual_records, visual_timeline

tabs_panel = dbc.Tabs([
    dbc.Tab(panel_controls.controls, label="Panel Controls"),
],style = app_theme.tab_style)

tabs_main = dbc.Tabs([
    dbc.Tab(visual_timeline.timeline, label="Timeline"),
    dbc.Tab(visual_aggregated.aggregated, label="Aggregated"), # add by year, month, day
    dbc.Tab(visual_records.records, label="Records"),

    #dbc.Tab(visual_map_view.map, label="View Map"),
],style = app_theme.tab_style)


tabs_lower = dbc.Tabs([
    dbc.Tab(summary.summary_submissions, label="Submissions"),
    dbc.Tab(summary.summary_incidents, label="Incidents"),
    dbc.Tab(summary.summary_investigations, label="Investigations"),
],style = app_theme.tab_style)