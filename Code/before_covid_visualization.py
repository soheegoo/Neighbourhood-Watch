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
_, non_covid_data = c.main()

non_covid_data.drop(columns=['Avg House Price', 'Avg Unemployment Rate', 'Avg Crime Rate'])

property_prices = pd.read_csv('property_prices.csv')

property_prices = property_prices.drop(columns=['Neighbourhood ID', 'Neighbourhood Name',
                                                'Average Property Price 2021', 'Average Property Price 2020',
                                                '$ Change (1 year)', '$ Change (3 year)'])

neighbourhood_crime_rates = pd.read_csv('neighbourhood_crime_rates.csv')

neighbourhood_crime_rates = neighbourhood_crime_rates.drop(columns=['Hood_ID', 'Neighbourhood',
                                                                    'Assault_Rate2019',
                                                                    'Assault_Rate2020'])

frames = [non_covid_data, property_prices, neighbourhood_crime_rates]

non_covid_data = pd.concat(frames, axis=1, join="inner")
non_covid_data = non_covid_data.T.drop_duplicates().T

# Initialize figure
fig1 = go.Figure()

# Create figure object
fig1.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=non_covid_data['Neighbourhood Name'],
                        locations=non_covid_data['Neighbourhood ID'],  # Assign location data,
                        z=non_covid_data['Cluster Labels'],  # Assign information data
                        colorbar = {'title': 'Neighbourhood Desirability Index', 'tickmode': 'array', 'nticks': 3, 'tickvals': [0,1,2],
                                    'ticktext': ['Least Desirable', 'Semi-Desirable', 'Most Desirable']},
                        zauto=True,
                        showscale=True
                        ))

fig1.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=non_covid_data['Neighbourhood Name'],
                        locations=non_covid_data['Neighbourhood ID'],  # Assign location data,
                        z=non_covid_data['Assault_Rate2018'],  # Assign information data
                        colorscale='Reds',
                        colorbar={'title': 'Crime Rate (per 100,000 people)'},
                        zauto=True,
                        showscale=True
                        ))
fig1.add_trace(
    go.Choroplethmapbox(geojson=toronto_neighbourhoods,  # Assign geojson file
                        featureidkey='properties.AREA_SHORT_CODE',
                        hovertext=non_covid_data['Neighbourhood Name'],
                        locations=non_covid_data['Neighbourhood ID'],  # Assign location data,
                        z=non_covid_data['Average Property Price 2018'],  # Assign information data
                        colorscale='Greens',
                        colorbar={'title': 'Average Property Price (in millions)'},
                        zauto=True,
                        showscale=True
                        ))

fig1.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Desirability Index",
                     method="update",
                     args=[{"visible": [True, False, False]},
                           {"title": "Toronto Neighbourhoods Desirability Index Before Covid"}]),
                dict(label="Crime Rate",
                     method="update",
                     args=[{"visible": [False, True, False]},
                           {"title": "Crime Rate in Toronto Neighbourhoods Before Covid"}]),
                dict(label="Property Prices",
                     method="update",
                     args=[{"visible": [False, False, True]},
                           {"title": "Average Property Prices in Toronto Neighbourhood Before Covid"}]),
            ]),
        )
    ])

# Update layout
fig1.update_layout(

    mapbox_style="carto-positron",  # Decide a style for the map
    mapbox_zoom=9,  # Zoom in scale
    mapbox_center={"lat": 43.7, "lon": -79.4},  # Center location of the map
)

fig1.show()

