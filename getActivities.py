import requests
import json
import time

#url for when you need new code
newTokenUrl = "http://www.strava.com/oauth/authorize?client_id=[clientID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all"


with open('strava_tokens.json') as tokenFile:
    strava_tokens = json.load(tokenFile)
with open('myInfo.json') as myInfo:
    myInfo = json.load(myInfo)

#If current token has expired make post request for new one
if strava_tokens['expires_at'] < time.time():
    res = requests.post(
        url = 'https://www.strava.com/oauth/token',
        data = {
            'client_id': myInfo['client_id'],
            'client_secret': myInfo['client_secret'],
            'code': myInfo['code'],
            'grant_type': 'refresh_token',
            'refresh_token': strava_tokens['refresh_token']
        }
    )

    newtokens = res.json()
    #update token file
    with open('strava_tokens.json', 'w') as newStravaTokens:
        json.dump(newtokens, newStravaTokens)
    strava_tokens = newtokens


url = "https://www.strava.com/api/v3/activities?access_token="
res = requests.get(url + strava_tokens['access_token'])
data = res.json()

#Write actives json to my activities json file
with open('myActivities.json', 'w') as activitiesFile:
    json.dump(data, activitiesFile)
