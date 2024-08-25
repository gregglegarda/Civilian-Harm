import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input, State
from dash import dcc
import app_theme
import data_connection


#DATA PIPELINE
df_submissions = data_connection.df_submissions.copy()
df_incidents = data_connection.df_incidents.copy()
df_investigations = data_connection.df_investigations.copy()

#years_submission = df_submissions["SubmissionYear"].unique().tolist()
#years_incident = df_incidents["IncidentYear"].unique().tolist()
#years_investigation = df_investigations["InvestigationYear"].unique().tolist()


years_submission = df_submissions.groupby("SubmissionYear").size().reset_index(name='Count')
years_incident = df_incidents.groupby("IncidentYear").size().reset_index(name='Count')
years_investigation = df_investigations.groupby("InvestigationYear").size().reset_index(name='Count')

years = sorted(set(years_submission['SubmissionYear']).union(set(years_incident['IncidentYear'])).union(set(years_investigation['InvestigationYear'])))

years_submission_reindexed = years_submission.set_index('SubmissionYear').reindex(years, fill_value=0).reset_index()
years_incident_reindexed = years_incident.set_index('IncidentYear').reindex(years, fill_value=0).reset_index()
years_investigation_reindexed = years_investigation.set_index('InvestigationYear').reindex(years, fill_value=0).reset_index()

counts_submission = years_submission_reindexed['Count'].tolist()
counts_incident = years_incident_reindexed['Count'].tolist()
counts_investigation = years_investigation_reindexed['Count'].tolist()




#FIGURE
fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=counts_submission,
                name='Submissions',
                marker_color=app_theme.visual_aggregated_color_palette_dark[0]
                ))
fig.add_trace(go.Bar(x=years,
                y=counts_incident,
                name='Incidents',
                marker_color=app_theme.visual_aggregated_color_palette_dark[1]
                ))
fig.add_trace(go.Bar(x=years,
                y=counts_investigation,
                name='Investigations',
                marker_color=app_theme.visual_aggregated_color_palette_dark[2]
                ))




fig.update_layout(
    margin=dict(r=15, t=55, b=45),
    #margin=dict(l=15, r=15, t=55, b=45),
    title_font_size = 14,
    yaxis_zeroline=False,
    title={'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_text="Yearly Volume of Records",
    xaxis_title="Year",
    yaxis_title="Number of Records",
    font_color="white",
    #title_font_color="white",
    #xaxis_color="white",
    #yaxis_color="white",
    xaxis_type = "category",
    xaxis_gridcolor="#303030",
    yaxis_gridcolor="#303030",
    plot_bgcolor='#222222',
    paper_bgcolor='#303030',
    legend_bgcolor='rgba(255, 255, 255, 0)',
    legend_bordercolor='rgba(255, 255, 255, 0)',
    legend=dict(x=0, y=1.0, ),
    barmode='group',
    bargap=0.15,  # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.

)


aggregated = html.Div([
    dcc.Graph(figure=fig,style={'height': "100%", "position":'relative'})
], style= {'padding':'5px',
           'background-color':app_theme.visual_container_color,
           'height': app_theme.visual_view_height,})