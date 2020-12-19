import json
import pandas as pd
import os
import time
import getActivities
import folium
from folium import plugins
import decoder

#if file doesn't exist make requests for new activities


#getActivities.getLastest()
#else if file hasn't been updated in a day
    #make new request
if not os.path.exists("myActivities.json"):
    getActivities.getLastest()
    print("Getting latest activities")
elif os.path.getctime("myActivities.json"):
    print() 

with open("myActivities.json") as activities:
    data = json.load(activities)


map = folium.Map(location=[40.8923, -74.4774], zoom_start=10) #intialize the map


lines = []
#Get all the polyline routes for each activity and decode them 
for activity in data:
    encodedLine = activity['map']['summary_polyline']
    if encodedLine != None:
        decoded = decoder.decode_polyline(activity['map']['summary_polyline']) #decode the line
        folium.PolyLine(decoded).add_to(map) #add the line to the mao

map.save('./map.html')

df = pd.json_normalize(data)

print(df.head())
print(df[df['type'] == 'Ride'].mean())

distance = df[df['type'] == 'Ride']['distance']

distance.plot()


