from page_incident_form import bar
import dash
import dash_bootstrap_components as dbc
from dash import html
import dash_leaflet as dl
from dash import Dash, html, Output, Input
from dash.exceptions import PreventUpdate
from dash_extensions.javascript import assign
import app_theme
from dash import dcc
from datetime import date


dash.register_page(__name__, path='/incident_form')






# How to render geojson.
point_to_layer = assign("""function(feature, latlng, context){
    const p = feature.properties;
    if(p.type === 'circlemarker'){return L.circleMarker(latlng, radius=p._radius)}
    if(p.type === 'circle'){return L.circle(latlng, radius=p._mRadius)}
    return L.marker(latlng);
}""")




layout = html.Div([
    # Security Level PAGE
    dbc.Navbar([
        dbc.Row([
            html.H6("UNCLASSIFIED (FOR MOCK PURPOSES ONLY)", style={'justify': 'center'})
        ], style={'textAlign': 'center', 'background': 'green', 'width': '100%'}),
    ], sticky="top", style={'padding': 0}),

    # BAR ROW
    # already using containers, no need to contain
    html.Div([bar.headerbar]),
    html.Div([bar.navbar]),

    #styling for page


    html.Div([


            # FORM Main CONTENT
            dbc.Container([

                    #title row
                    dbc.Row([
                        html.Div([html.Img(src=r'assets/us_army.png',style={'padding': '50px','padding-bottom':'10px', 'padding-top':'10px','width': '20%','justify': 'center'} ,className = 'center')],style={'width':'100'}),
                        html.H2("Civilian Harm Incident Reporting Form", style={'padding':'10px', 'padding-top':'10px'}),
                        #html.Div([html.Img(src=r'assets/chirf_banner.png',style={'padding': '50px','padding-bottom':'10px', 'padding-top':'10px','width': '100%', 'justify': 'center'},className='center')], style={'width': '100'}),
                        html.Div([dbc.Alert("The Civilian Harm Incident Report Form (CHIRF) supports "
                                      "CHMR-AP, Objective 6 by standardizing data collection on civilian harm "
                                      "incidents within the DoD. The CHIRF ensures consistent data formatting and "
                                      "improved access across all classification levels, facilitating efficient data "
                                      "sharing and analysis. While initially focused on the DoD, the scope of CHIRF "
                                      "may expand to include other U.S. Government entities and potentially allies, "
                                      "partners, and NGOs.",
                                      color="warning",dismissable=True,),],style={'padding':'50px','padding-bottom':'10px', 'padding-top':'10px'}),
                    ], style={'textAlign': 'center'}),


                    html.Hr(),

                    # Date Card
                    dbc.Row([
                        dbc.Card([
                            dbc.Row([
                                    dbc.Col(dbc.Label("Date:"), width=1),
                                    dbc.Col(dcc.DatePickerSingle(
                                        date=date(2017, 6, 21),
                                        display_format='MMM DD, YYYY'), width=4),
                                    dbc.Col(dbc.Button("Reset Form", type="reset", color="danger"),
                                            width=7, style={'textAlign':"right"})
                            ]),
                        ],style= {'padding':'50px'}),
                    ],style= {'padding':'50px','padding-bottom':'10px', 'padding-top':'10px'}),

                    #Contact Information Card
                    dbc.Row([
                            dbc.Card([
                                    html.H5("Contact Information:"),
                                    html.Hr(),

                                    dbc.Row([
                                            dbc.Col([
                                                dbc.Label("First Name:", html_for="firstName", style={"marginBottom": "5px"}),
                                                dbc.Input(type="text", id="firstName",placeholder="Enter first name",required=True,style={"marginBottom": "15px"},
                                            )],md=6,),
                                            dbc.Col([
                                                dbc.Label("Last Name:", html_for="lastName", style={"marginBottom": "5px"}),
                                                dbc.Input(type="text",id="lastName",placeholder="Enter last name",required=True,style={"marginBottom": "15px"},
                                            )],md=6,),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Label("Reporting Unit:", html_for="reportingUnit", style={"marginBottom": "5px"}),
                                            dbc.Input(type="text", id="reportingUnit",
                                                      placeholder="Enter the full unit designation of the reporting entity",
                                                      required=True, style={"marginBottom": "15px"})
                                        ], md=6),
                                        dbc.Col([
                                            dbc.Label("Position:", html_for="position", style={"marginBottom": "5px"}),
                                            dbc.Input(type="text", id="position", placeholder="Enter position",
                                                      style={"marginBottom": "15px"})
                                        ], md=6)
                                    ]),
                                    dbc.Row([
                                            dbc.Col([
                                                dbc.Label("Phone Number:", html_for="phoneNumber", style={"marginBottom": "5px"}),
                                                dbc.Input(type="tel", id="phoneNumber", placeholder="Enter commercial phone number", required=True, style={"marginBottom": "15px"}),
                                                html.P("Please enter a number in the format: +1234567890", className="help", style={"marginBottom": "15px"})
                                            ], md=6),
                                            dbc.Col([
                                                dbc.Label("DSN:", html_for="dsn", style={"marginBottom": "5px"}),
                                                dbc.Input(type="text", id="dsn", placeholder="Enter DSN", style={"marginBottom": "15px"})
                                            ], md=6)
                                    ]),
                                    dbc.Row([
                                            dbc.Col([
                                                dbc.Label("Email:", html_for="email", style={"marginBottom": "5px"}),
                                                dbc.Input(type="email", id="email", placeholder="Enter email address", required=True, style={"marginBottom": "15px"})
                                            ], md=6),
                                            dbc.Col([
                                                dbc.Label("Unit:", html_for="unit", style={"marginBottom": "5px"}),
                                                dbc.Input(type="text", id="unit", placeholder="If different from the Reporting Unit, enter your unit", style={"marginBottom": "15px"})
                                            ], md=6)
                                    ]),

                                    dbc.Label("Combatant Command (CCMD):", html_for="ccmd", style={"marginBottom": "5px"}),
                                    dbc.Select(id="ccmd", options=[
                                        {"label": "Please Select", "value": ""}, {"label": "None", "value": "None"},
                                        {"label": "AFRICOM", "value": "AFRICOM"}, {"label": "CENTCOM", "value": "CENTCOM"},
                                        {"label": "CYBERCOM", "value": "CYBERCOM"}, {"label": "EUCOM", "value": "EUCOM"},
                                        {"label": "INDOPACOM", "value": "INDOPACOM"}, {"label": "NORTHCOM", "value": "NORTHCOM"},
                                        {"label": "NATO", "value": "NATO"}, {"label": "SOCOM", "value": "SOCOM"},
                                        {"label": "SOUTHCOM", "value": "SOUTHCOM"}, {"label": "SPACECOM", "value": "SPACECOM"},
                                        {"label": "STRATCOM", "value": "STRATCOM"}, {"label": "Other", "value": "Other"}
                                        ], placeholder="Select a Combatant Command", className="form-control", style={"marginBottom": "15px"})
                            ],style= {'padding':'50px'}),
                    ],style= {'padding':'50px','padding-bottom':'10px', 'padding-top':'10px'}),



                    #Phase 1 card

                    dbc.Row([
                        dbc.Card([
                            html.H5("Initial Review (Phase 1)"),
                            html.P(html.Em("(DoDI 3000.17 Paragraph 4.4)")),
                            html.Hr(),

                            # Incident Date or Date Range Exact or Approximate
                            dbc.Row([
                                dbc.Label("Is the incident date or date range exact or approximate?"),
                                dbc.Col([
                                    dbc.ButtonGroup([
                                        dbc.Button("Exact", color="outline-primary"),
                                        dbc.Button("Approximate", color="outline-primary"),
                                    ]),
                                ])
                            ], className="form-group", style={"marginBottom": "15px"}),

                            # Incident Date or Date Range
                            dbc.Row([
                                dbc.Label("Incident Date or Date Range:", html_for="startDate"),
                                dbc.Col([
                                    dbc.Input(type="datetime-local", id="startDate", placeholder="Start date and time",
                                              className="form-control")
                                ], md=4, style={"marginBottom": "15px"}),
                                dbc.Col([
                                    dbc.Input(type="datetime-local", id="endDate", placeholder="End date and time",
                                              className="form-control")
                                ], md=4, style={"marginBottom": "15px"}),
                                dbc.Col([
                                    dbc.Select(id="timezone", options=[
                                        {"label": "Please Select", "value": ""},
                                        {"label": "UTC-12:00 (International Date Line West)", "value": "UTC-1200"},
                                        {"label": "UTC-11:00 (Coordinated Universal Time-11)", "value": "UTC-1100"},
                                        {"label": "UTC-10:00 (Hawaii)", "value": "UTC-1000"},
                                        {"label": "UTC-09:30 (Marquesas Islands)", "value": "UTC-0930"},
                                        {"label": "UTC-09:00 (Alaska)", "value": "UTC-0900"},
                                        {"label": "UTC-08:00 (Pacific Time - US & Canada)", "value": "UTC-0800"},
                                        {"label": "UTC-07:00 (Mountain Time - US & Canada)", "value": "UTC-0700"},
                                        {"label": "UTC-06:00 (Central Time - US & Canada)", "value": "UTC-0600"},
                                        {"label": "UTC-05:00 (Eastern Time - US & Canada)", "value": "UTC-0500"},
                                        {"label": "UTC-04:00 (Atlantic Time - Canada)", "value": "UTC-0400"},
                                        {"label": "UTC-03:30 (Newfoundland)", "value": "UTC-0330"},
                                        {"label": "UTC-03:00 (Brazil, Buenos Aires, Georgetown)", "value": "UTC-0300"},
                                        {"label": "UTC-02:00 (Mid-Atlantic)", "value": "UTC-0200"},
                                        {"label": "UTC-01:00 (Azores, Cape Verde Is.)", "value": "UTC-0100"},
                                        {"label": "UTC (Western European Time, London, Lisbon, Casablanca)", "value": "UTC+0000"},
                                        {"label": "UTC+01:00 (Central European Time, West Central Africa)", "value": "UTC+0100"},
                                        {"label": "UTC+02:00 (Eastern European Time, Cairo, Athens)", "value": "UTC+0200"},
                                        {"label": "UTC+03:00 (Moscow, Baghdad, Riyadh)", "value": "UTC+0300"},
                                        {"label": "UTC+03:30 (Tehran)", "value": "UTC+0330"},
                                        {"label": "UTC+04:00 (Abu Dhabi, Muscat, Baku, Tbilisi)", "value": "UTC+0400"},
                                        {"label": "UTC+04:30 (Kabul)", "value": "UTC+0430"},
                                        {"label": "UTC+05:00 (Ekaterinburg, Islamabad, Karachi, Tashkent)", "value": "UTC+0500"},
                                        {"label": "UTC+05:30 (Bombay, Calcutta, Madras, New Delhi, Colombo)", "value": "UTC+0530"},
                                        {"label": "UTC+05:45 (Kathmandu)", "value": "UTC+0545"},
                                        {"label": "UTC+06:00 (Almaty, Dhaka, Colombo)", "value": "UTC+0600"},
                                        {"label": "UTC+06:30 (Yangon, Cocos Islands)", "value": "UTC+0630"},
                                        {"label": "UTC+07:00 (Bangkok, Hanoi, Jakarta)", "value": "UTC+0700"},
                                        {"label": "UTC+08:00 (Beijing, Perth, Singapore, Hong Kong)", "value": "UTC+0800"},
                                        {"label": "UTC+09:00 (Tokyo, Seoul, Osaka, Sapporo, Yakutsk)", "value": "UTC+0900"},
                                        {"label": "UTC+09:30 (Adelaide, Darwin)", "value": "UTC+0930"},
                                        {"label": "UTC+10:00 (Eastern Australia, Guam, Vladivostok)", "value": "UTC+1000"},
                                        {"label": "UTC+10:30 (Lord Howe Island)", "value": "UTC+1030"},
                                        {"label": "UTC+11:00 (Magadan, Solomon Islands, New Caledonia)", "value": "UTC+1100"},
                                        {"label": "UTC+12:00 (Auckland, Wellington, Fiji, Kamchatka)", "value": "UTC+1200"},
                                        {"label": "UTC+12:45 (Chatham Islands)", "value": "UTC+1245"},
                                        {"label": "UTC+13:00 (Tonga, Samoa)", "value": "UTC+1300"},
                                        {"label": "UTC+14:00 (Line Islands)", "value": "UTC+1400"}
                                    ], placeholder="Select a Timezone", className="form-control")
                                ], md=4, style={"marginBottom": "15px"})
                            ], className="form-row"),

                            # UTM Coordinates
                            dbc.Row([
                                dbc.Label("If possible, enter UTM coordinates of the event:", html_for="utmCoordinates"),
                                dbc.Col([
                                    dbc.Input(type="text", id="utmCoordinates", placeholder="e.g., 29M 568148 9119361",
                                              className="form-control")
                                ], style={"marginBottom": "15px"})
                            ], className="form-group"),

                            # Event Location
                            dbc.Row([
                                dbc.Label("Otherwise, provide the location of the event:", html_for="eventLocation"),
                                dbc.Col([
                                    dbc.Input(type="text", id="eventLocation", placeholder="country, region, city, etc.",
                                              className="form-control")
                                ], style={"marginBottom": "15px"})
                            ], className="form-group"),

                            # Event Location Picker
                            dbc.Row([#MAP CONTENT PORTION
                                dbc.Container([

                                    html.Div([
                                        # Setup a map with the edit control.
                                        dl.Map(center=[56, 10], zoom=4, children=[
                                            dl.GestureHandling(),
                                            dl.TileLayer(), dl.FeatureGroup([
                                                dl.EditControl(id="edit_control"), dl.Marker(position=[56, 10])]),
                                        ], style={'width': '100%', 'height': '50vh'}, id="map"),
                                        # Buttons for triggering actions from Dash.
                                        html.Button("Draw maker", id="draw_marker"),
                                        html.Button("Remove -> Clear all", id="clear_all")
                                    ],style = {'padding-bottom':'50px'})

                                ], fluid=True,
                            ),]),

                            # Incident Type
                            dbc.Row([
                                dbc.Label("Is this incident an operation or exercise?"),
                                dbc.Col([
                                    dbc.ButtonGroup([
                                        dbc.Button("Operational", color="outline-primary"),
                                        dbc.Button("Exercise", color="outline-primary"),
                                    ]),
                                ])
                            ], className="form-group", style={"marginBottom": "15px"}),

                            # Responsible Entity
                            dbc.Row([
                                dbc.Label("Who is the entity believed to be responsible for the incident?"),
                                dbc.Col([
                                    dbc.ButtonGroup([
                                        dbc.Button("US", color="outline-primary"),
                                        dbc.Button("Ally or Partner", color="outline-primary"),
                                        dbc.Button("Other", color="outline-primary"),
                                        dbc.Button("Unknown", color="outline-primary"),
                                    ])
                                ], style={"marginBottom": "15px"})
                            ], className="form-group"),

                            # Operation Type
                            dbc.Row([
                                dbc.Label(
                                    "During which type of operation did the incident occur? (Multiple options may be selected.)"),
                                dbc.Col([
                                    dbc.ButtonGroup([
                                        dbc.Button("Air", color="outline-primary"),
                                        dbc.Button("Cyber", color="outline-primary"),
                                        dbc.Button("Ground", color="outline-primary"),
                                        dbc.Button("Naval", color="outline-primary"),
                                        dbc.Button("Unknown", color="outline-primary"),
                                        dbc.Button("Other", color="outline-primary"),
                                    ], id="operationTypeButtons")
                                ], style={"marginBottom": "15px"})
                            ], className="form-group"),

                            # Identify the known type of harm
                            dbc.Row([
                                dbc.Label("Identify the known type of harm:"),
                                dbc.Col([
                                    dbc.ButtonGroup([
                                        dbc.Button("Civilian Killed", color="outline-secondary"),
                                        dbc.Button("Civilian Injured", color="outline-secondary"),
                                        dbc.Button("Property Damaged", color="outline-secondary"),
                                        dbc.Button("Property Destroyed", color="outline-secondary"),
                                    ], id="harmTypeButtons")
                                ], style={"marginBottom": "15px"})
                            ], className="form-group"),

                            # Was the event deliberate or dynamic?
                            dbc.Row([
                                dbc.Label("Was the event deliberate or dynamic?"),
                                dbc.Col([
                                    dbc.ButtonGroup([
                                        dbc.Button("Deliberate", color="outline-secondary"),
                                        dbc.Button("Dynamic", color="outline-secondary"),
                                    ], id="eventNatureButtons")
                                ], style={"marginBottom": "15px"})
                            ], className="form-group"),

                        ], style={'padding': '50px'}),
                    ], style={'padding': '50px','padding-bottom':'10px', 'padding-top':'10px' }),


                    #Phase 2 Card
                    dbc.Row([
                        dbc.Card([
                            html.H5("Supplemental Report (Phase 2)"),
                            html.P(html.Em("(DoDI 3000.17 Paragraph 4.5)")),
                            html.Hr(),

                            dbc.Row([
                                dbc.Label("Location of shooter/weapon system:", html_for="shooterLocation", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="text", id="shooterLocation", placeholder="e.g., 29M 568148 9119361", style={"marginBottom": "15px"})
                                ])
                            ]),

                            dbc.Row([
                                dbc.Label("Intended Target Location (UTM):", html_for="targetLocation", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="text", id="targetLocation", placeholder="e.g., 29M 568148 9119361", style={"marginBottom": "15px"})
                                ])
                            ]),

                            dbc.Row([
                                dbc.Label("Identify weapon system used:", html_for="weaponSystem", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="text", id="weaponSystem", placeholder="Type of weapon will eventually be a dropdown selection.", style={"marginBottom": "15px"})
                                ])
                            ]),

                            dbc.Row([
                                dbc.Label("Identify munition type used:", html_for="munitionType", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="text", id="munitionType", placeholder="Type of munition will eventually be a dropdown selection.", style={"marginBottom": "15px"})
                                ])
                            ]),

                            dbc.Row([
                                dbc.Label("Estimated number of rounds fired:", html_for="roundsFired", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="number", id="roundsFired", placeholder="Enter the number of rounds fired, if known.", style={"marginBottom": "15px"})
                                ])
                            ]),


                        ], style={'padding': '50px'}),
                    ], style={'padding': '50px','padding-bottom':'10px', 'padding-top':'10px' }),


                    #Phase 3 Card
                    dbc.Row([
                        dbc.Card([
                            html.H5("Advanced Supplemental Report (Phase 3)"),
                            html.P(html.Em("(DoDI 3000.17 Paragraph 4.6)")),
                            html.Hr(),

                            dbc.Row([
                                dbc.Label("Description of Targeting Process:", html_for="targetingProcess", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Textarea(id="targetingProcess", rows=3, placeholder="Describe the targeting process leading to the incident.", style={"marginBottom": "15px"})
                                ])
                            ]),

                            dbc.Row([
                                dbc.Label("Attach incident documentation:", html_for="documentation", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="file", id="documentation", style={"marginBottom": "15px"})
                                ])
                            ]),

                            dbc.Row([
                                dbc.Label("Or provide a URL link to available documentation:", html_for="documentationUrl", style={"marginBottom": "5px"}),
                                dbc.Col([
                                    dbc.Input(type="url", id="documentationUrl", placeholder="Enter URL", style={"marginBottom": "15px"})
                                ])
                            ]),

                        ], style={'padding': '50px'}),
                    ], style={'padding': '50px','padding-bottom':'10px', 'padding-top':'10px' }),


                    #Subimt card
                    dbc.Row([
                            dbc.Container([
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.Label("Report ID:", html_for="reportId", className="badge badge-secondary", ),
                                            dbc.Input(type="text", id="reportId", placeholder="Enter Report ID", className="form-control", )
                                        ],style={'padding-left': '5px','padding-right': '5px','padding-bottom': '5px'}),
                                    ],md=3,)
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Button("Submit Form", color="primary", type="submit", className="mr-2"),
                                        dbc.Button("Reset Form", color="danger", type="reset")
                                    ], className="text-center")
                                ])
                            ], fluid=True),
                    ],style={'padding-left': '35px','padding-bottom':'10px', 'padding-top':'10px'}),

                    #Review Card
                    dbc.Row([
                        dbc.Card([
                            html.H5("Review Information"),
                            html.P(html.Em("(Please review if your information is correct)")),
                            html.Hr(),
                            #Review Map portion
                            dbc.Row([
                                html.P(html.Em("Date:")),
                                html.P(html.Em("First Name:")),
                                html.P(html.Em("Last Name:")),
                                html.P(html.Em("Reporting Unit:")),
                                html.P(html.Em("Position:")),
                                html.P(html.Em("Phone Number:")),
                                html.P(html.Em("DSN:")),
                                html.P(html.Em("Email:")),
                                html.P(html.Em("Unit:")),
                                html.P(html.Em("Combatant Command (CCMD):")),
                                html.P(html.Em("Is the incident date or date range exact or approximate?:")),
                                html.P(html.Em("Incident Date or Date Range:")),
                                html.P(html.Em("If possible, enter UTM coordinates of the event:")),
                                html.P(html.Em("Otherwise, provide the location of the event:")),
                                html.P(html.Em("Is this incident an operation or exercise?:")),
                                html.P(html.Em("Who is the entity believed to be responsible for the incident?:")),
                                html.P(html.Em("During which type of operation did the incident occur? (Multiple options may be selected.):")),
                                html.P(html.Em("Identify the known type of harm:")),
                                html.P(html.Em("Was the event deliberate or dynamic?:")),
                                html.P(html.Em("Location of shooter/weapon system:")),
                                html.P(html.Em("Intended Target Location (UTM):")),
                                html.P(html.Em("Identify weapon system used:")),
                                html.P(html.Em("Identify munition type used:")),
                                html.P(html.Em("Estimated number of rounds fired:")),
                                html.P(html.Em("Description of Targeting Process:")),
                                html.P(html.Em("Attach incident documentation:")),
                                html.P(html.Em("Or provide a URL link to available documentation:")),
                                html.P(html.Em("Report ID:")),
                                html.P(html.Em("Submit Form:")),
                                html.P(html.Em("Reset Form:")),
                            ]),


                            dbc.Container([
                                # Setup another map to that mirrors the edit control geometries using the GeoJSON component.
                                dl.Map(center=[56, 10], zoom=4, children=[
                                    dl.GestureHandling(),
                                    dl.TileLayer(), dl.GeoJSON(id="geojson", pointToLayer=point_to_layer, zoomToBounds=True),
                                ], style={'width': '100%', 'height': '50vh'}, id="mirror"),
                            ], fluid=True, style={'padding':0}
                            ),
                            html.Hr(),
                            dbc.Row([dbc.Button("Submit Incident Report")], style={'padding':0}),

                        ], style={'padding': '50px'}),
                    ], style={'padding': '50px','padding-bottom':'10px', 'padding-top':'10px'}),





            ], fluid=True,
                style={'background-color': app_theme.visual_card_background_color,
                       'padding-top': '10px',
                       'padding-bottom':'10px'
                       }),







    ],style={'padding': '100px','padding-top': '0px','padding-bottom': '10px'})
])
