from etl import etl

# url - link for right route
# file_name - name of output .csv file

# url = 'https://www.uz.gov.ua/en/passengers/timetable/?station=23020&by_station=Search'    #Kovel
# url = 'https://www.uz.gov.ua/en/passengers/timetable/?station=47548%2C23092%2C23081%2C23215%2C36921%2C23200&by_station=Search'    #Lviv
url = 'https://www.uz.gov.ua/en/passengers/timetable/?station=23600&by_station=Search'  #Odessa
file_name = 'Odessa statistics'

etl(url=url, file_name=file_name)
