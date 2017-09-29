import requests


# Get the 5 latest disasters from api.reliefweb
def pulling_new_data_from_endpoint(number=1):
    URI = "https://api.reliefweb.int/v1/disasters"
    query = {'limit': number, 'preset': 'latest', 'appname':'emergps'}
    return requests.get(URI, params=query).json()


# After getting the latest disasters we retrieve the last
def retrieve_ad_data_of_disaster(url):
    req = requests.get(url).json()
    req = req['data'][0]['fields'] # Remove some layers
    print req
    countries = [{"name": x['name'], "location": x['location'], "href":x['href']} for x in req['country']]
    disaster = {"name":req['name'], "href":url,"graphic_url":req['url'], "location":countries, "created_at":req['date']['created'], "active":req["current"]}
    return disaster





