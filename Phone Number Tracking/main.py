import phonenumbers
from test import number
###Get Region
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number , "CH")
print (geocoder.description_for_number(ch_nmber,"en"))

###Get Service Provider name
from phonenumbers import carrier
service_nmber = phonenumbers.parse(number , "RO")
print (carrier.name_for_number(service_nmber,"en"))

### Get Timezone
from phonenumbers import timezone
phoneNumber = phonenumbers.parse("+919876543210")
timeZone = timezone.time_zones_for_number(phoneNumber) 
print(timeZone)
