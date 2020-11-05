# nyc-dash-bokeh
NYC 311 Call Bokeh Server

Displays a Bokeh dashboard of response time to calls to New York City's 311 service for 2 selected zipcodes, as well as the 2020 average. 


To run (on port 8080):

bokeh serve --port 8080 --allow-websocket-origin={SERVER IP ADDRESS}:8080 --auth=scripts/auth.py nyc_dash

Authenticates with username=nyc & password=iheartnyc.

To view the dashboard, visit http://{IP ADDRESS}:8080/nyc_dash?username=nyc&password=iheartnyc 
