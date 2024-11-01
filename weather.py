import requests, json
import time
import datetime




def fetch_data(city):
    try:
        weatherAPI='http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+apikey  + '&units=metric'
        response=requests.get(weatherAPI)
        response.raise_for_status()         #check for HTTP errors in case of unsuccessful get request
        data=response.json()             
        #print(data)
        return data
        
    except requests.RequestException as e:      #print error
        print(f"Error fetching data: {e}")
        return None




def extract_save_data(data):

    temperature=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    feels_like=data["main"]["feels_like"] 
    name=data["name"]
    time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')     #convert time 

    dictionary = {
    "City_Name":name,
    "Temprature": f"{temperature} °C",
    "Humidity": f"{humidity} %",
    "Temprature_feels_like":f"{feels_like} °C",
    "Time": time
    }


    try:
        with open(file_path, 'r', encoding='utf-8') as file:  
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(dictionary)             #the data from API is stored in dictionary

    with open(file_path, 'w', encoding='utf-8') as file:          #write new data in json file
        json.dump(existing_data, file, indent=4, ensure_ascii=False)        #degree sybmol was stored as \u00b0  in json so using utf-8 and ascii false to include it 

    print(f"Data appended to {file_path} at {time}")






def Data_Retreival(user_time, city):

    with open(file_path, 'r', encoding='utf-8') as file:
        data_search = json.load(file)   #reading exsisting json file

    for entry in data_search:
        if entry['Time'] == user_time and entry['City_Name'].lower() == city.lower():    # match data entries
            return entry

    print("No data found for the provided timestamp and city")
    return None




apikey="ef2c3f26fe52b454b3823dd41d4b4963"       #API key from Open weather API 
city=input("Enter City name:")   #Data for any city can be fetched from API and stored in Json for future requests. In this case it might be better to assign one city to city variable
file_path="Data.json"


stop=False
   
while not stop:

    data = fetch_data(city)             #json file is returned to data from function fetch data
    if data is not None:
        extract_save_data(data)


    print("\nType 'search' to look up data by timestamp or 'quit' to exit.")
    user_input = input("Enter your choice: ").strip().lower()
    
  

    if user_input == 'search':
        user_provided_time = input("Enter the timestamp (YYYY-MM-DD hh:mm) to search: ")
        user_city = input("Enter the city to search: ")
        Requested_Weather_data = Data_Retreival(user_provided_time, user_city)

        if Requested_Weather_data:
            print("Requested Data found:", Requested_Weather_data)

    
    elif user_input == 'quit':          #In case of a live app. this while loop should run indefinately but we need a way out of program.
            stop = True
    
    else:
            print("Invalid input. Please type 'search' or 'quit'")



    if not stop:
   
        time.sleep(600)     #wait for 10 minutes

    

    












