import json
import requests
import unicodedata
import pandas as pd

# Load the CSV file
df = pd.read_csv("dataset_part_2.csv")

# Calculate the number and occurrence of each orbit in the Outcome column
landing_outcomes = df['Outcome'].value_counts()

print(landing_outcomes)
print("=========================================================")
# Check the value of 'None None'
none_outcomes = df[df['Outcome'] == 'None None']
print(none_outcomes)
print("=========================================================")


# Check the value 
valueCounts = df[df['LaunchSite'] == 'CCAFS SLC 40']
print('counts of CCAFS SLC 40:', valueCounts)

print("=========================================================")

# Check the value 
valueCounts = df[df['Orbit'] == 'GTO']
print('counts of GTO:', valueCounts)