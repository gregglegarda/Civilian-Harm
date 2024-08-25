import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input, State
import app_theme


headerbar = dbc.Navbar(
    dbc.Container([
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.A(html.Img(src=app_theme.navbar_logo, height="50px"), href=app_theme.navbar_link, style={"textDecoration": "none"})),
                    dbc.Col(dbc.NavbarBrand(app_theme.navbar_title, className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
        ], fluid=True),
    color="dark",
    dark=True,
)

navbar = dbc.Nav([
    dbc.NavItem(dbc.NavLink("Home", active=False,href="/")),
    dbc.DropdownMenu(
        [dbc.DropdownMenuItem("Historical Data",href="/historical_data"),
                dbc.DropdownMenuItem("Interactive Map",href="/interactive_map"),
                dbc.DropdownMenuItem("All Database Records", href="/"),
                dbc.DropdownMenuItem("Lessons Learned Cards",href="/"),],
        label="Explore",
        nav=True,
    ),
    dbc.DropdownMenu(
        [dbc.DropdownMenuItem("Submit Incident (Public)",href="/incident_form"),
                dbc.DropdownMenuItem("Verify Incident",href="/"),
                dbc.DropdownMenuItem("Assess Incident",href="/"),
                dbc.DropdownMenuItem("Investigate Incident",href="/"),],
        label="Incident Process",
        nav=True,
    ),
    dbc.DropdownMenu(
        [dbc.DropdownMenuItem("Intelink Repository",href="https://www.intelink.gov/"),
                dbc.DropdownMenuItem("Data Model",href="/data_model"),
                dbc.DropdownMenuItem("Databases",href="/"),
                dbc.DropdownMenuItem("Data Flow",href="/"),],
        label="Data Design",
        nav=True,
    ),
    #dbc.NavItem(dbc.NavLink("Explore Data", active=False,href="/explore_data")),
    #dbc.NavItem(dbc.NavLink("Interactive Map", active=False,href="/interactive_map")),
    #dbc.NavItem(dbc.NavLink("Submit Incident", active=False, href="/incident_form")),
    #dbc.NavItem(dbc.NavLink("Verify Incident", active=False, href="/")),
    #dbc.NavItem(dbc.NavLink("Investigate Incident", active=False, href="/")),

    #dbc.DropdownMenu(
    #    [dbc.DropdownMenuItem("Data Model",active=True,href="/data_model"),
    #            dbc.DropdownMenuItem("Intelink",href="https://www.intelink.gov/"),
    #            dbc.DropdownMenuItem("Community Engagement and Users"),
    #            dbc.DropdownMenuItem("Lessons Learned"),
    #            dbc.DropdownMenuItem("Mitigation and Response"),],
    #    label="External Links",
    #    nav=True,
    #)
],pills=True
)

