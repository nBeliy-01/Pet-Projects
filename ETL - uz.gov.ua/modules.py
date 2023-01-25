import numpy as np
import pandas as pd
import requests
from datetime import datetime 
from bs4 import BeautifulSoup, SoupStrainer

### Function which extract all data in each cell
def extract(url):

    req = requests.get(url)
    source = req.text
    
    stations_info = SoupStrainer(class_="c-trains-by-station")
    soup = BeautifulSoup(source, "lxml", parse_only=stations_info)

    table_elems = []
    for elem in soup.find_all("td"):
        table_elems.append(elem.string)

    return table_elems

### Function which choose all necessary information about rout and write into DataFrame
def transform(elems):
    
    table_stations = []
    arrival = []
    departure = []
    stations_idx = np.arange(1, len(elems), 7)
    arrival_idx = np.arange(4, len(elems), 7)
    departure_idx = np.arange(5, len(elems), 7)

    for i in range(len(elems)):
        if i in stations_idx:
            table_stations.append(elems[i])
        elif i in arrival_idx:
            arrival.append(elems[i])
        elif i in departure_idx:
            departure.append(elems[i])

    departure_stations = [table_stations[index].split()[0] for index in range(len(table_stations))]
    arrival_stations = [table_stations[index].split()[1] for index in range(len(table_stations))]

    data = pd.DataFrame({
        "Departure station" : departure_stations,
        "Arrival station" : arrival_stations,
        "Departure time" : departure,
        "Arrival time" : arrival
    })

    return data

### Function which write all data into .csv file
def load(data, file_name):
    
    data.to_csv(f"{file_name}.csv", index=False)
    print(f"Data has written to file '{file_name}' successfully!")
    
    return None

### Log function, shows process status
def log(message):
    
    timestamp_format = "%d-%m-%Y %H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open("logfile.txt", "a") as file: 
        file.write(timestamp + ', ' + message + '\n')

    return None
