import os
try:
    import dash_bootstrap_components
    print("dash_bootstrap_components is already installed")
except ImportError:
    os.system("pip install dash-bootstrap-components")

try:
    import dash_ag_grid as dag
    print("dash_ag_grid is already installed")
except ImportError:
    os.system("pip install dash-ag-grid")

try:
    from dash_extensions.javascript import assign
    print("dash_extensions is already installed")
except ImportError:
    os.system("pip install dash-extensions")


import dash_bootstrap_components as dbc
import pandas as pd

#app themes
dbc_icons = dbc.icons.BOOTSTRAP
external_stylesheets = dbc.themes.DARKLY
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
#dbc_css = "custom.css"
#dbc_css = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"

#external_stylesheets = "https://cdn.jsdelivr.net/npm/bootswatch@5.3.3/dist/darkly/bootstrap.min.css"
#external_stylesheets = ""
title = "CHMR Analytics"
icon = 'logo.ico'

#navbar
navbar_title = "Civilian Harm Mitigation and Response | Data Management Platform Dashboard"
navbar_logo = "assets/logo.svg"
navbar_link = "https://plotly.com"


#tabs
tab_style = {#'background-color':'black',
        #'width': '60%',
        #'height': '8px',
        #'line-height': '0px' ,
        #'line-width': '0px',
        #'margin-bottom': '40px',
         }
#home
card_border_color = '#d3d3d3'

#visual container
visual_container_color = '#222222'#b2cbf2'
visual_card_background_color = '#152238' #should be div
visual_view_height = '55vh'

#visual_map
marker_color_submissions = "yellow"
marker_color_incidents = "orange"
marker_color_investigations = "red"

visual_aggregated_color_palette_dark = ["#486de8","#e07f9d","#018977","#b088f5","#c55305","#8ea9ff","#ffb0c8","#40bfa9"]
visual_aggregated_color_palette_light = ["#688ae8","#c33d69","#2ea597","#8456ce","#e07941","#3759ce","#962249","#096f64"]
visual_aggregated_text_color = 'white'
#visual_components
visual_map_background_color = '#303030'
#visual_timeline

#controls
controls_card_background_color ='#152238' #should be div
controls_view_height = '55vh'
class_types = ["Submissions", "Incidents", "Investigations"]

#summary


metrics_view_height = '15vh'
summary_card_widths = 3
summary_submission_card_titles = [
    #1
    ["Total Submitted Reports", "Total number of reports submitted", 372, "reports"],
    ["Average Submission Time", "Average time taken to submit a report", 3.4, "hours"],
    ["Most Occurring Type of Submissions", "Most common type of submitted reports", "CHIRF", "submissions"], # Examples: Witness Reports, Incident Logs, Damage Assessments

    #2
    ["Accounted Submissions / Verified Incidents", "Number of submissions that correspond to verified incidents", 122, "incidents"],
    ["Un-accounted Submissions / Verified Incidents", "Number of submissions that do not correspond to verified incidents", 250, "incidents"],
    ["Submissions per Incident", "Ratio of submissions to verified incidents", 0.8, "per incident"],

    #3
    ["Civilian Submissions", "Total count of submitted reports by civilians", 301, "reports"],
    ["Combatant Submissions", "Total count of submitted reports by combatant personnel", 51, "reports"],
    ["Other Submissions", "Total count of submitted reports by other individuals", 20, "reports"],

    #4
    ["Average Age of Submitters", "Average age of individuals submitting reports", 32.7, "years"],
    ["Submission Distance", "Average distance from incident location to submission point", 12.1, "kilometers"],
]

summary_incidents_card_titles = [
    #1
    ["Total Verified Incidents", "Total number of incidents verified", 193, "incidents"],
    ["Total Casualties", "Total number of casualties", 370, "casualties"],
    ["Total Deaths", "Total number of deaths", 58, "deaths"],

    #2
    ["Total Submissions/Incidents", "% Percentage of submissions to incidents", 151.03, "percent"],
    ["Submissions per Incident", "Average number of submissions per incident", 1.5, "submissions"],

    #3
    ["Time of Incident", "Most common time of day for incidents", "12 to 3", "PM"],
    ["Most Occurring Location", "Most common geographical location of incidents", "Urban", "area"],

    #4
    ["Age of Casualties", "Average age of casualties", 40.2, "years"],

]

summary_investigations_card_titles = [
    #1
    ["Total Investigations", "Total number of investigations conducted", 83, "investigations"],
    ["Investigation Time", "Average time taken to complete an investigation", 6, "weeks"],
    ["Investigation Cost ($)", "$ Average cost of each investigation", 1.2, "million dollars"],
    ["Damage Estimate Per Year ($)", " $Estimated financial damage in dollars per year", 5.25, "billion dollars"],

    #2
    ["Investigations/Incidents", "% Percentage of investigations relative to incidents", 83.22, "percent"],
    ["Investigations per Incidents", "Average number of investigations per incident", 0.8, "investigations"],

    #3
    ["Total Misidentification (type)", "Total instances of misidentification", 21, "instances"],
    ["Misassociation (sub-type)", "Instances of misassociation", 11, "instances"],
    ["Misperception (sub-type)", "Instances of misperception", 10, "instances"],
    ["Total Collateral Damage (type)", "Total instances of collateral damage", 77, "instances"],
    ["Anticipated and Accepted (sub-type)", "Instances of anticipated and accepted collateral damage", 22, "instances"],
    ["Unanticipated Presence (sub-type)", "Instances of unanticipated presence leading to damage", 25, "instances"],
    ["Unanticipated Effects (sub-type)", "Instances of unanticipated effects leading to damage", 30, "instances"],

    #4
    ["Investigator Age", "Average age of investigators", 45, "years"]

]

