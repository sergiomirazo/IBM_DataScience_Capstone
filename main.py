import json
import requests
import unicodedata
import pandas as pd
from spacex_API_Falcon9 import rest_api

static_json_url = "https://api.spacexdata.com/v4/launches/past"

response = requests.get(static_json_url)

print(response.status_code)

print(type(response.content))
#PRINT OUTPUT: <class 'bytes'>

content = response.content.decode('utf-8')
data = json.loads(content)

df = pd.DataFrame(data)

# Filter dataframe for Falcon 9 rockets
df_falcon9 = df[df['rocket'] == '5e9d0d95eda69973a809d1ec']

print(df_falcon9.head())

df_falcon9.to_csv('spacex_API_Falcon9.csv', index=False)

# Load the CSV file
df = pd.read_csv("spacex_API_Falcon9.csv")

# Calculate the number and occurrence of each orbit in the Outcome column
landing_outcomes = df['fairings'].value_counts()

print(landing_outcomes)

# Check the value of 'None None'
none_outcomes = df[df['fairings'] == '']
print('fairings:', none_outcomes)

rest_api()


