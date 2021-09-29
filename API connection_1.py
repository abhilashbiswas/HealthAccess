"""
HealthAccess team

Primary Author: Abhilash Biswas
Objective: This program takes in 2 parameters a)User's location b)Destination location
           and uses Google Map's API to calculate the distance between the 2 locations
           
           For our app, we can use this program to create a travel time table for all hospitals nearby and then sort it on time 
           to give a ranked set of hospitals

Packages required:
    a. requests (should already be there)
    b. json (should already be there)

Other instructions:
    a. The API KEY used is the author's google cloud API key. We should use that for all Google cloud based API requests but don't share outside of team
    b. The entire code is cased in a program so that the program can be used for our rest of app development
    
"""

def API_distance():
    #Import required files
    import requests
    import json
    
    #Keys
    API_KEY = 'AIzaSyABxu5Q65XqI2ndTkA58OMs75ahlumci10'
    
    #User inputs
    user_address = input('Please enter your current street address: ')
    destination = input('Please enter the destination address: ')   
    
    #Travel time function
    def time(x,y):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        
        search_address = url + 'origins=' + x + '&destinations=' + y \
                                + '&units=imperial&key=' + API_KEY
        
        payload={}
        headers = {}
        
        response = requests.request("GET", search_address, headers=headers, data=payload)
        data = json.loads(response.content.decode('utf-8'))
        
        
        travel_time = data['rows'][0]['elements'][0]['duration']['text']
        
        return travel_time
    
    
    print('Travel time to chosen destination = ',time(user_address,destination))


    
if __name__=='__main__':
    API_distance()    
        

