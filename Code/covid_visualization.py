"""
Actual Mapping

"""
# Import libraries
import json
from plotly import graph_objects as go
import pandas as pd
import cluster as c

toronto_neighbourhoods = json.load(open('neighbourhoods.geojson'))

# dataframe
covid_data, non_covid_data = c.main()

# Initialize figure
fig = go.Figure()

# Create figure object
fig.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=covid_data['Neighbourhood Name'],
                        locations=covid_data['Neighbourhood ID'],  # Assign location data,
                        z=covid_data['Cluster Labels'],  # Assign information data
                        colorbar={'title': 'Neighbourhood Desirability Index', 'tickmode': 'array', 'nticks': 3,
                                  'tickvals': [0, 1, 2],
                                  'ticktext': ['Least Desirable', 'Semi-Desirable', 'Most Desirable']},
                        zauto=True,
                        showscale=True

                        ))


fig.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        locations=covid_data['Neighbourhood ID'],  # Assign location data
                        z=covid_data['Avg Vaccination Rate'],  # Assign information data
                        zauto=True,
                        hovertext=covid_data['Neighbourhood Name'],
                        colorscale='viridis',
                        colorbar = {'title': 'Average Vaccination Rate (Percentage)'},
                        showscale=True
                        ))
fig.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=covid_data['Neighbourhood Name'],
                        locations=covid_data['Neighbourhood ID'],  # Assign location data,
                        z=covid_data['Avg Covid Case Rate'],  # Assign information data
                        zauto=True,
                        colorscale='Blues',
                        colorbar = {'title': 'Average Covid Case Rate (per 100,000 people)'},
                        showscale=True
                        ))

fig.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=covid_data['Neighbourhood Name'],
                        locations=covid_data['Neighbourhood ID'],  # Assign location data,
                        z=covid_data['Avg Unemployment Rate'],  # Assign information data
                        zauto=True,
                        colorscale='darkmint',
                        colorbar = {'title': 'Average Unemployment Rate (Percentage)'},
                        showscale=True
                        ))
fig.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=covid_data['Neighbourhood Name'],
                        locations=covid_data['Neighbourhood ID'],  # Assign location data,
                        z=covid_data['Avg House Price'],  # Assign information data
                        zauto=True,
                        colorscale='burgyl',
                        colorbar = {'title': 'Average Property Price (in millions)'},
                        showscale=True
                        ))

fig.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=covid_data['Neighbourhood Name'],
                        locations=covid_data['Neighbourhood ID'],  # Assign location data,
                        z=covid_data['Avg Crime Rate'],  # Assign information data
                        zauto=True,
                        colorscale='Blues',
                        colorbar = {'title': 'Average Crime Rate (per 100,000 people)'},
                        showscale=True
                        ))


fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Desirability Index",
                     method="update",
                     args=[{"visible": [True, False, False, False, False, False]},
                           {"title": "Toronto Neighbourhoods Desirability Index"}]),
                dict(label="Vaccination Rate",
                     method="update",
                     args=[{"visible": [False, True, False, False, False, False]},
                           {"title": "Vaccination Completion in Toronto Neighbourhoods"}]),
                dict(label="Covid-19 Rate",
                     method="update",
                     args=[{"visible": [False, False, True, False, False, False]},
                           {"title": "Covid-19 in Toronto Neighbourhoods (per 100,000 people)"}]),
                dict(label="Unemployment Rate",
                     method="update",
                     args=[{"visible": [False, False, False, True, False, False]},
                           {"title": "Unemployment Rate in Toronto Neighbourhoods"}]),
                dict(label="Property Prices",
                     method="update",
                     args=[{"visible": [False, False, False, False, True, False]},
                           {"title": "Average Property Prices in Toronto Neighbourhood"}]),
                dict(label="Crime Rate",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, True]},
                           {"title": "Crime Rate in Toronto Neighbourhoods"}]),
            ]),
        )
    ])

# Update layout
fig.update_layout(

    mapbox_style="carto-positron",  # Decide a style for the map
    mapbox_zoom=9,  # Zoom in scale
    mapbox_center={"lat": 43.7, "lon": -79.4},  # Center location of the map
)

fig.show()
