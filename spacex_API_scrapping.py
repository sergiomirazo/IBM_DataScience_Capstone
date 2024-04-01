import sys
import requests
import json
import pandas as pd

def rest_api():
    static_json_url = "https://api.spacexdata.com/v4/launches/past"
    rocket_json_url = "https://api.spacexdata.com/v4/rockets/"
    rocket_names_file = "rockets.txt"
    
    response = requests.get(static_json_url)
    
    content = response.content.decode('utf-8')
    data = json.loads(content)
    
    df = pd.DataFrame(data)
    rocket_names = set()
    
    for index, row in df.iterrows():
        rocket_id = row['rocket']
        
        if rocket_id not in rocket_names:
            rocket_response = requests.get(rocket_json_url + rocket_id)
            rocket_content = rocket_response.content.decode('utf-8')
            rocket_data = json.loads(rocket_content)
            
            rocket_name = rocket_data['name']
            
            rocket_names.add(rocket_id)
            
            with open(rocket_names_file, 'a') as f:
                f.write(f"The rocket with ID '{rocket_id}' corresponds to the rocket named '{rocket_name}'\n")
    
    print(f"All rocket names have been stored in the file '{rocket_names_file}'.")


