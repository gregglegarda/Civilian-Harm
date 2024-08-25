import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
import plotly.graph_objects as go
import app_theme
from dash import Dash, html, dcc, callback, Output, Input, State
import data_connection
from datetime import datetime
import plotly.express as px


#from dash_bootstrap_templates import load_figure_template
#load_figure_template(["cyborg", "darkly"])


df = data_connection.df_submissions
#df = data_connection.df_incidents
#df = data_connection.df_investigations
dataset_name = "Submission"


df_fig = df.copy()
df_fig.columns = [col.replace(dataset_name, "") for col in df_fig.columns]
print(df_fig.columns)
df_fig['Date'] = df_fig.apply(lambda row: datetime.strptime(f"{int(row.Year)}-{int(row.Month)}-{int(row.Day)}", '%Y-%m-%d'), axis=1)
df_fig["Date"] = pd.to_datetime(df_fig[[ "Day", "Month", "Year"]])
print(type(df_fig["Duration"][0]))
df_fig["Duration"] = pd.to_numeric(df_fig["Duration"], errors='coerce')
print(type(df_fig["Duration"][0]))
#df_fig = df_fig.groupby("Date").size().reset_index(name='Count')
df_fig = df_fig.groupby("Date").agg({"Duration":"sum"}).reset_index()
print(df_fig)

# Create figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=list(df_fig.Date), y=list(df_fig.Duration)))



# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
fig.update_layout(
    margin=dict(r=15, t=55, b=45),
    #margin=dict(l=15, r=15, t=55, b=45),
    title={'x':0.5,'xanchor': 'center','yanchor': 'top'},
    title_font_size = 14,
    title_text="Civilian Harm "+ dataset_name +" Durations Daily Trend",
    xaxis_title="Daily Timeline",
    yaxis_title= dataset_name + "Duration (Hours) per Day",
    title_font_color="white",
    xaxis_color="white",
    yaxis_color="white",
    xaxis_gridcolor = "#303030",
    yaxis_gridcolor = "#303030",
    plot_bgcolor='#222222',
    paper_bgcolor ='#303030',
    yaxis_zeroline=False
)
fig.update_traces(line_color='#4c9ed6')

timeline = html.Div([
    dcc.Graph(figure=fig,style={'height':'100%'})
], style= {'padding':'5px',
           'background-color':app_theme.visual_container_color,
           'height': app_theme.visual_view_height,
           })