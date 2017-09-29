from mysql_controller import *
from validator_reliefWEB import *

mysql_connection = MySQL_connector("emergps_master","emergps", "localhost")

response = pulling_new_data_from_endpoint()['data'][0]['href']

if not mysql_connection.is_retrieved_disaster_new(response):
     disasters = retrieve_ad_data_of_disaster(response)
     mysql_connection.add_disaster(disasters)
     print "Adding disaster"
else:
     print "Already inside"






