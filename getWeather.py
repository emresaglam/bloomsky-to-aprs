import requests
import argparse
import json
import datetime

parser = argparse.ArgumentParser(description='Take Bloomsky device data and create a pymultimonaprs weather json format')
parser.add_argument('--config', '-c', default='config.json')
parser.add_argument('--output', '-o', default='weather.json')
args=parser.parse_args()

aprsData = {}

# Default config.json file is in the same folder.

# Read config.json
with open(args.config, 'r') as f:
	configurations = f.read()

config = json.loads(configurations)

bloomSky_apiKey = config["bloomsky"]["api_key"]

url = "http://thirdpartyapi.appspot.com/api/skydata/?unit=intl"

header = {"Authorization" : bloomSky_apiKey}

r = requests.get(url, headers = header)

bloomskyData = r.json()

aprsData["timestamp"] = int (datetime.datetime.now().strftime("%s"))
aprsData["temperature"] = bloomskyData[0]['Data']['Temperature']
aprsData["humidity"] = bloomskyData[0]['Data']['Humidity']
aprsData["pressure"] = bloomskyData[0]['Data']['Pressure']

aprsJson = json.dumps(aprsData,indent=4)

aprsFile = open(args.output, 'w')
aprsFile.write(aprsJson)
aprsFile.close()

