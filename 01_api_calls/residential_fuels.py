import urllib.request
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

url = 'https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/?'
key = 'api_key=4uFR83cYBKGU8tpijJccYS6a7EHH9HUOdIhwxZq1'
query = '&frequency=annual&data[0]=value&facets[stateId][]=VA&start=2010&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'


response = urllib.request.urlopen(url+key+query)
response_bytes = response.read()
content = json.loads(response_bytes) # Convert response to json
response.close()

df = pd.DataFrame.from_dict(content['response']['data'])

data = df
data['value-units'].value_counts()
data['sector-name'].value_counts()
data['period'] = pd.to_numeric(data['period'])
data['value'] = pd.to_numeric(data['value'])

residential = data[(data['sector-name'] == 'Residential carbon dioxide emissions') & (data['fuel-name'] == 'All Fuels')]

scatter_plot = residential.plot.scatter(x='period', y='value')
scatter_plot.set_title('Residential Use of All Fuels Over the Years')

st.write(scatter_plot)
st.pyplot(plt.gcf())