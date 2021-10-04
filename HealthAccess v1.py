"""
HealthAccess MVP

1. User enters street address
2. User chooses emergency/non emergency
3. If emergency, user gets a table of ranked hospital list
4. If non emergency, same as above but with additional information about each hospital


Program used:
    1. hospitals_list.py
    2. API connection_1.py
    3. hospital_website_finder.py
    4. appt_page_link.py

"""


import API_connection_1 as ac
import hospitals_list as hl
import hospital_website_finder as hwf
import appt_page_link as apl
import pandas as pd


#Developer setting
no_of_results = 5


#Hospital list, categories and all that jazz
hospital_list = pd.read_csv('hospital_list.csv')
hospital_list_sample  = hospital_list.sample(10)        #Because of limited computing power

hospital_categories = pd.read_csv('hospital_categories.csv')

#Dropping categories that don't exist in our sampled list
matched_cat = pd.merge(hospital_categories,hospital_list_sample, on='Category', how = 'inner')
matched_cat = matched_cat['Category'].drop_duplicates()

matched_cat =matched_cat.reset_index(drop = True)

#Ask for user input
user_address = input('Please enter your street address: ')
type = int(input('Please choose 1 for emergency and 2 for non-emergency: '))

#Calculating distances
travel_time_text = []
travel_time_numeric = []

for i in range(0,len(hospital_list_sample)):  
        time = ac.time(user_address,hospital_list_sample['Organization Name'].iloc[i])
        travel_time_text.append(time['text'])
        travel_time_numeric.append(time['value'])
        
hospital_list_sample['travel time text'] = travel_time_text    
hospital_list_sample['travel time value'] = travel_time_numeric 
        
#Dropping invalid values
hospital_list_sample = hospital_list_sample.loc[hospital_list_sample['travel time value'] !=-999]


if type == 1:
    
    
    hospital_list_sample = hospital_list_sample.sort_values('travel time value')
    
    result_headings = ('{:7s}{:^50s}{:^20s}'.format('Choice #','Hospital Name','Travel time'))
    
    print(result_headings)
    for i in range(0,no_of_results):
        print('{:1d}{:>50s}{:>20s}'.format(i+1,hospital_list_sample['Organization Name'].iloc[i],hospital_list_sample['travel time text'].iloc[i]))
        
    
if type == 2:
    print(matched_cat)
    user_category = int(input('Please choose a category of care from the given list: '))
        
    filtered_hospital_list = hospital_list_sample.loc[hospital_list_sample['Category'] == matched_cat[user_category]]
    
    user_display = filtered_hospital_list.head(no_of_results)
    
    hosp_names = []
    for i in range(0,len(filtered_hospital_list)):
        hosp_names.append(filtered_hospital_list['Organization Name'].iloc[i])
    
    websites=[]
    for name in hosp_names:
        websites.append(hwf.hospital_website(name))
    
    appt_urls = []
    for site in websites:
        appt_urls.append(apl.appt_page(site)['appt_link'])
    
    user_display['appointment page'] = appt_urls
    
    result_headings = ('{:7s}{:^50s}{:^20s}{:>40s}'.format('Choice #','Hospital Name','Travel time','appointment page'))
    
    print(result_headings)
    for i in range(0,len(user_display)):
        print('{:1d}{:>50s}{:>20s}{:>40s}'.format(i+1,user_display['Organization Name']
                                                  .iloc[i],user_display['travel time text'].iloc[i],
                                                  user_display['appointment page'].iloc[i]))

    
    
    
    
        
    
        
    
        
        
    
    
                                                                                             
