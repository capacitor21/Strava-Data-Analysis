import requests
import json

with open('strava_tokens.json') as tokenFile:
    strava_tokens = json.load(tokenFile)
    print(strava_tokens)
    print("\n" + strava_tokens['access_token'])

url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']

res = requests.get(url + "?access_token=" + access_token)
data = res.json()

with open('myActivities.json', 'w') as activitiesFile:
    json.dump(data, activitiesFile)
