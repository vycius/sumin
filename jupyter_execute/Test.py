#!/usr/bin/env python
# coding: utf-8

# # Test
# 

# In[1]:


import pandas as pd
import seaborn as sns
import plotly.express as px


# In[2]:


cities = pd.read_json('https://www.visimarsrutai.lt/services-ext/api/municipalities')

for city in cities:


# In[ ]:





# In[2]:


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})

import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                           )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[14]:


import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_mapbox(df, geojson=geojson, color="winner",
                           locations="district", featureidkey="properties.district",
                           center={"lat": 45.5517, "lon": -73.7073},
                           mapbox_style="carto-positron", zoom=9)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[22]:


import pandas as pd
import plotly.express as px

#import dataset
df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

#select entries with the continent as asia
df = df[df['date'] == '2021-02-04']
df = df[df.continent == 'Asia']

display(df)
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

#plot
fig = px.choropleth(df, geojson=counties, locations="iso_code",
                    color="new_cases",
                    hover_name="location",
                           featureidkey="properties.district",
                    title = "Daily new COVID cases",
                     color_continuous_scale=px.colors.sequential.PuRd,
                        )

fig["layout"].pop("updatemenus")
fig.show()


# In[ ]:




