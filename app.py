import app_theme
from dash import Dash, html, dcc, callback, Output, Input, State
import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[
                                    app_theme.external_stylesheets,
                                    app_theme.dbc_css,
                                    app_theme.dbc_icons],
                #https://icons.getbootstrap.com/
                #https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
                title=app_theme.title,
                prevent_initial_callbacks=True,
                use_pages=True
                )
app._favicon = app_theme.icon

app.layout = html.Div([
        dash.page_container,
],style={#'background-color': "white",
         #'padding':'20px'
         })



# Copy data from the edit control to the geojson component.
@app.callback(Output("geojson", "data"), Input("edit_control", "geojson"))
def mirror(x):
    return x

# Trigger mode (draw marker).
@app.callback(Output("edit_control", "drawToolbar"), Input("draw_marker", "n_clicks"))
def trigger_mode(n_clicks):
    return dict(mode="marker", n_clicks=n_clicks)  # include n_click to ensure prop changes

# Trigger mode (edit) + action (remove all)
@app.callback(Output("edit_control", "editToolbar"), Input("clear_all", "n_clicks"))
def trigger_action(n_clicks):
    return dict(mode="remove", action="clear all", n_clicks=n_clicks)  # include n_click to ensure prop changes



if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8050, use_reloader=False)