import requests
import json

url = "https://www.strava.com/api/v3/athlete/activities?include_all_efforts=" "Authorization: Bearer [[token]]"

newTokenUrl = "http://www.strava.com/oauth/authorize?client_id=[50618]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all"

access_token = "6e92d60c8afbae26d0727e42e91f0949e2b214a9"
refresh_token = "668400a223bdd7bfd926f232adca81bc791e4344"
client_secret = "039c8695de20b66f8dd0aac27bdea06e5af5d818"
client_id = 50618
code = '1f9cf797b9c0dc7739dd8c7ef90d8b420b1f9621'


response = requests.post(
    url = 'https://www.strava.com/oauth/token',
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code'
    }
)

strava_tokens = response.json()
print(strava_tokens)

with open('strava_tokens.json', 'w') as tokenFile:
    json.dump(strava_tokens, tokenFile)

