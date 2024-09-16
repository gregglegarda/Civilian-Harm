from page_interactive_map import bar
import dash
import dash_bootstrap_components as dbc
from dash import html
import app_theme
import dash_leaflet as dl
import dash_bootstrap_components as dbc
import app_theme
import data_connection
from dash import Dash, html, dcc, callback, Output, Input, State
import functions


dash.register_page(__name__, path='/interactive_map')


# Some markers of incidents
#### DATA MARKERS CREATION
submissions_markers = data_connection.df_submissions.apply(lambda x: functions.create_marker_submission(x), axis=1).to_list()
incidents_markers = data_connection.df_incidents.apply(lambda x: functions.create_marker_incident(x), axis=1).to_list()
investigations_markers = data_connection.df_investigations.apply(lambda x: functions.create_marker_investigation(x), axis=1).to_list()



# Some shapes.
weather = dl.WMSTileLayer(url="https://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi", layers="nexrad-n0r-900913", format="image/png", transparent=True)
#markers = [dl.Marker(position=[56, 10]), dl.CircleMarker(center=[55, 10], radius=50)]


# Some tile urls.
keys = ["Google - Hybrid",
        "Google - Terrain",
        "Open Street Map",
         ]
url_templates = ["http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}",
                "http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}",
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                 ]
attribution = '<a href="http://gregglegarda.com"></a>'


map =  html.Div([
            dl.Map([
                dl.FullScreenControl(),
                #toggling the base maps
                dl.LayersControl(
                    [dl.BaseLayer(dl.TileLayer(url=template, attribution=attribution),
                                  name=key, checked=key == keys[0]) for key,template in zip(keys,url_templates)]+
                    [dl.Overlay(dl.LayerGroup(weather), name="weather", checked=False)]
                ),
                #toggling raster layer
                dl.LayersControl([
                    dl.Overlay(dl.LayerGroup(submissions_markers), name="Submissions", checked=True),
                    dl.Overlay(dl.LayerGroup(incidents_markers), name="Incidents", checked=True),
                    dl.Overlay(dl.LayerGroup(investigations_markers), name="Investigations", checked=True),
                    ]
                ),

            ], maxBoundsViscosity= 1.0,
                preferCanvas=True,
                zoom=3,
                minZoom=3,
                center=(10, 10),
                worldCopyJump= True,
                #autosize = False,
                style={
                    'height': '100%',
                    'background-color':app_theme.visual_map_background_color},
            )
    ], style= {'height': '75vh',
            'padding':'5px',
            'background-color':app_theme.visual_container_color
               })


layout = html.Div([
    # BAR ROW
    # already using containers, no need to contain
    html.Div([bar.headerbar]),
    html.Div([bar.navbar]),

    # MAIN CONTENT ROW
    dbc.Container([
            map
    ], fluid=True,
        style={'background-color': app_theme.visual_card_background_color,
               'padding-top': '10px',
               'padding-bottom':'10px'
               }),
])
