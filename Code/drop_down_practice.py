import json
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import urllib.request

toronto_neighbourhoods = json.load(open('neighbourhoods.geojson'))

vaccine_trends = pd.read_csv('vaccine_trends.csv')
vaccine_trends = vaccine_trends.drop(columns=['18+ Population (18+ nhood 2021 May 2021 )',
                                              'Count of 18+ fully vaccinated clients'])
vaccine_trends.head()
#neighbourhood_cases = pd.read_csv('neighbourhood_cases.csv')

#neighbourhood_cases = neighbourhood_cases.drop(columns=['Rate per 100,000 people', 'Case Count'])

mycustomdata = np.stack((vaccine_trends['Vaccination Rate'], vaccine_trends['Neighbourhood Name']), axis=-1)

title = 'Chloropleth Maps'

fig = go.Figure(go.Choroplethmapbox(geojson= toronto_neighbourhoods,
                                    locations=vaccine_trends['Neighbourhood Name'],
                                    z=vaccine_trends['Vaccination Rate'],
                                    featureidkey='properties.id',
                                    coloraxis="coloraxis",
                                    customdata=mycustomdata,
                                    hovertemplate='Vaccine Rate: %{customdata[0]}' + \
                                                  'Neighbouthood: %{customdata[1]} ',
                                    marker_opacity=0.75, marker_line_width=0.5))
fig.update_layout(coloraxis_colorscale='Viridis',
                  mapbox=dict(style='carto-positron',
                              zoom=6.5,
                              center={"lat": 43.6532, "lon": -79.3832},
                              ))
fig.update_layout(title_text=title,
                  title_x=0.5,
                  margin={"r": 10, "t": 60, "l": 0, "b": 0});
# fig.show()


matter_r = [[0.0, '#2f0f3d'],  # cmocean colorscale
            [0.1, '#4f1552'],
            [0.2, '#72195f'],
            [0.3, '#931f63'],
            [0.4, '#b32e5e'],
            [0.5, '#cf4456'],
            [0.6, '#e26152'],
            [0.7, '#ee845d'],
            [0.8, '#f5a672'],
            [0.9, '#faca8f'],
            [1.0, '#fdedb0']]

button1 = dict(method='update',
               label='Vaccine Rate',
               args=[
                   {"z": [vaccine_trends['Vaccination Rate']],
                    "hovertemplate": "Vaccine Rate: %{customdata[0]}'" + \
                                                 " Neighbourhood: %{customdata[1]} "
                    },  # dict for fig.data[0] updates
                   {"coloraxis.colorscale": "Viridis"}  # dict for  layout attribute update
               ])
"""
button2 = dict(method='update',
               label='Neighbouthood Rate',
               args=[
                   {"z": [neighbourhood_cases['Rate per 100,000 people (rounded)']],
                    "hovertemplate": "Canton: %{customdata[0]}<br>" + \
                                     "Neighbouthood: %{customdata[1]}"
                    },
                   {"coloraxis.colorscale": matter_r}  # update layout attribute
               ])
"""


fig.update_layout(updatemenus=[dict(active=0,
                                    buttons=[button1])]
                  );
fig.show()
#import chart_studio.plotly as py

#py.iplot(fig, filename='update-choroplethmapbox')
