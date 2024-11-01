How the code works:

1. FetchData(): Takes a city as an input and sends a fetch/get request to API and in case of succesful fetching 
it returns a json file or in case of an error it prints that error. 
2.  extract_save_data(): Information is extracted from the data and relevant information is stored in another 
json file from where the user can retrieve it.
3. Data_Retreival(): takes timestamp and city name from user for which the data is to be retrieved.
4. A while loop is used so that the program runs as long as user does not write quit. User can select search option 
to search for data. In case no option is selected the program will wait for 10 minutes and make another get request
after which it will again ask the user to quit or search. 
