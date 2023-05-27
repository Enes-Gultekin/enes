import os
import json

file="stations.json"

##{
##    "uuid": "47174d8f-1b8e-4599-8a59-b580dd55bc87",
##    "number": "48900237",
##    "shortname": "EITZE",
##    "longname": "EITZE",
##    "km": 9.56,
##    "agency": "VERDEN",
##    "longitude": 9.276769435375872,
##    "latitude": 52.90406544743417,
##    "water": {
##      "shortname": "ALLER",
##      "longname": "ALLER"
##    }
##}

# the keys for the station dict
keys = ["uuid", "number", "shortname", "longname", "km", "agency",
        "longitude", "latitude", "water"] # water is another dict!

def convert2geojson(filename):
    pass

def write_geojson(geojson):
    pass

if __name__ == '__main__':
    if not os.path.exists(file):
        exit(0)

    geojs = convert2geojson(file)
    write_geojson(geojs)
