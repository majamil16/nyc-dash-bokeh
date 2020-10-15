# nyc-dash-bokeh
COMP 598 bokeh server assignment

to run (on port 8080):

bokeh serve --port 8080 --allow-websocket-origin={SERVER IP ADDRESS}:8080 --auth=scripts/auth.py nyc_dash

visit http://{IP ADDRESS}:8080/nyc_dash?username=nyc&password=iheartnyc 
