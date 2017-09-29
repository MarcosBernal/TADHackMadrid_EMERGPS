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


# #response_text = pulling_new_data_from_endpoint()
#
# response_text = {u'count': 1, u'links': {u'self': {u'href': u'https://api.reliefweb.int/v1/disasters?offset=0&limit=1&preset=latest'}, u'next': {u'href': u'https://api.reliefweb.int/v1/disasters?offset=1&limit=1&preset=latest'}}, u'totalCount': 2911, u'href': u'https://api.reliefweb.int/v1/disasters?preset=latest&limit=1', u'time': 2, u'data': [{u'href': u'https://api.reliefweb.int/v1/disasters/44109', u'fields': {u'name': u'Vanuatu: Monaro Volcano - Sep 2017'}, u'score': 1, u'id': u'44109'}]}
# print response_text['data']
# print response_text['data'][0]['href']
#
# #disaster = add_data_to_disaster('try',response_text['data'][0]['href'])
# disaster = {u'count': 1, u'links': {u'self': {u'href': u'https://api.reliefweb.int/v1/disasters/44109'}, u'collection': {u'href': u'https://api.reliefweb.int/v1/disasters'}}, u'totalCount': 1, u'href': u'https://api.reliefweb.int/v1/disasters/44109', u'time': 3, u'data': [{u'fields': {u'status': u'alert', u'current': False, u'description': u"On 23 September 2017, the Vanuatu Meteorology & GeoHazards Department (VMGD) increased the activity level for Monaro volcano on Ambae island, Penama province to Level 4: a moderate eruption state. With this situation, flying rocks and volcanic gas will affect the Red Zone which is about 6.5km radius around the volcano's crater. Villages located further from the volcano's centre can expect unusual volcanic hazards and ash falls around the island especially in villages exposed to prevailing trade winds direction. Acid rain may also be expected which may damage garden crops. VMGD has advised that the activity may increase, or decrease, at any time without warning. Evacuations have begun for people living in high risk areas. The Vanuatu government has requested that partner agencies be ready to support the response in the coming days.\r\n\r\nThe provincial government authorities are currently evacuating people in high-risk areas \u2013 as of 24 September, 3,000 people had been moved to safer areas on the island. As of 25 September evening, Penama provincial authorities had a record of approximately 6,800 people in evacuation centres on Ambae with an additional 900 people who have yet to be evacuated. Host communities and provincial authorities are currently supporting evacuee needs. The Provincial Disaster Committee is currently leading the response on the ground. The National Disaster Management Office advises that further evacuations are likely to occur if the situation escalates. ([IFRC, 26 Sep 2017](https://reliefweb.int/node/2240594))\r\n\r\n###Useful Links   \r\n- [Vanuatu Meteorology & Geo-Hazards Dept: Alert Bulletin - Ambae](http://www.vmgd.gov.vu/vmgd/index.php/geohazards/volcano/alert-bulletin#manaroVoui)   \r\n- [Vanuatu National Disaster Management Office: Volcanic Activity - Ambrym & Ambae](https://ndmo.gov.vu/volcanic-activity)\r\n- [Vanuatu Red Cross: Facebook page](https://www.facebook.com/VanuatuRedCross/)", u'glide': u'VO-2017-000140-VUT', u'url': u'https://reliefweb.int/taxonomy/term/44109', u'country': [{u'name': u'Vanuatu', u'primary': True, u'iso3': u'vut', u'href': u'https://api.reliefweb.int/v1/countries/249', u'location': {u'lat': -16.26, u'lon': 167.72}, u'id': 249}], u'url_alias': u'https://reliefweb.int/disaster/vo-2017-000140-vut', u'description-html': u'<p>On 23 September 2017, the Vanuatu Meteorology &amp; GeoHazards Department (VMGD) increased the activity level for Monaro volcano on Ambae island, Penama province to Level 4: a moderate eruption state. With this situation, flying rocks and volcanic gas will affect the Red Zone which is about 6.5km radius around the volcano&#39;s crater. Villages located further from the volcano&#39;s centre can expect unusual volcanic hazards and ash falls around the island especially in villages exposed to prevailing trade winds direction. Acid rain may also be expected which may damage garden crops. VMGD has advised that the activity may increase, or decrease, at any time without warning. Evacuations have begun for people living in high risk areas. The Vanuatu government has requested that partner agencies be ready to support the response in the coming days.</p>\n\n<p>The provincial government authorities are currently evacuating people in high-risk areas \u2013 as of 24 September, 3,000 people had been moved to safer areas on the island. As of 25 September evening, Penama provincial authorities had a record of approximately 6,800 people in evacuation centres on Ambae with an additional 900 people who have yet to be evacuated. Host communities and provincial authorities are currently supporting evacuee needs. The Provincial Disaster Committee is currently leading the response on the ground. The National Disaster Management Office advises that further evacuations are likely to occur if the situation escalates. (<a href="https://reliefweb.int/node/2240594">IFRC, 26 Sep 2017</a>)</p>\n\n<h3>Useful Links</h3>\n\n<ul>\n<li><a href="http://www.vmgd.gov.vu/vmgd/index.php/geohazards/volcano/alert-bulletin#manaroVoui">Vanuatu Meteorology &amp; Geo-Hazards Dept: Alert Bulletin - Ambae</a><br></li>\n<li><a href="https://ndmo.gov.vu/volcanic-activity">Vanuatu National Disaster Management Office: Volcanic Activity - Ambrym &amp; Ambae</a></li>\n<li><a href="https://www.facebook.com/VanuatuRedCross/">Vanuatu Red Cross: Facebook page</a></li>\n</ul>\n', u'featured': False, u'primary_country': {u'location': {u'lat': -16.26, u'lon': 167.72}, u'iso3': u'vut', u'href': u'https://api.reliefweb.int/v1/countries/249', u'id': 249, u'name': u'Vanuatu'}, u'date': {u'created': u'2017-09-23T00:00:00+00:00'}, u'primary_type': {u'code': u'VO', u'id': 4615, u'name': u'Volcano'}, u'type': [{u'code': u'VO', u'primary': True, u'id': 4615, u'name': u'Volcano'}], u'id': 44109, u'name': u'Vanuatu: Monaro Volcano - Sep 2017'}, u'id': u'44109'}]}
#
# print disaster['data']
# print disaster['data'][0]['fields'].keys()
#
# print disaster['data'][0]['id']





