import requests
import pandas as pd

r = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()

print(r)

#df = pd.read_json(r['elements'], dtype=object)
#print(df.head())

for players in r['elements']:

    if players["cost_change_event"] != 0:
        print(f'{players["first_name"]},{players["second_name"]},{players["now_cost"]},{players["cost_change_event"]}')