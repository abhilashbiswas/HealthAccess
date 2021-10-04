# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:32:08 2021

@author: vidisha chowdhury
"""

# Using NPPES NPI



def hospital_list():
    
    import requests
    import json
    import pandas as pd

    headers = {'Content-Type': 'application/json'}
    
    count = 0
    count_max = 5
     
#    end = 'x'
    
    rows = []
    
    while  count <= 400:
    
        if count< count_max:
                 
            url = 'https://npiregistry.cms.hhs.gov/api/?version=2.0&enumeration_type=NPI-2&taxonomy_description=&first_name=&last_name=&organization_name=&address_purpose=PRIMARY&city=pittsburgh&state=&postal_code=&country_code=&limit=200&'+'skip='+ str(count*200) +'&pretty=on&version=2.0'
            
            response = requests.get(url, headers = headers)
    
            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
            
           
            
            for i in data["results"]:
                
                organization = i["basic"]["organization_name"]
                 
                address = " ".join([
                i["addresses"][0]["address_1"],
                i["addresses"][0]["address_2"],
                i["addresses"][0]["city"],
                i["addresses"][0]["country_name"],
                i["addresses"][0]["postal_code"],
                i["addresses"][0]["state"]
                ])
                telephone = i["addresses"][0]["telephone_number"]
                for j in i["taxonomies"]:
                    if j["primary"] == True:
                        category = j["desc"]   
                rows.append([organization,address, telephone, category])
            
            
            count += 1
#            end = len(data["results"][0]["addresses"][0]["address_1"])
        
        elif count>= count_max:
            
            url = 'https://npiregistry.cms.hhs.gov/api/?version=2.0&enumeration_type=NPI-2&taxonomy_description=&first_name=&last_name=&organization_name=&address_purpose=PRIMARY&city=pittsburgh&state=&postal_code=&country_code=&limit=200&'+'skip='+ str(1000)+'&pretty=on&version=2.0'
    
            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
            
                       
            
            for i in data["results"]:
                
                organization = i["basic"]["organization_name"]
                 
                address = " ".join([
                i["addresses"][0]["address_1"],
                i["addresses"][0]["address_2"],
                i["addresses"][0]["city"],
                i["addresses"][0]["country_name"],
                i["addresses"][0]["postal_code"],
                i["addresses"][0]["state"]
                ])
                telephone = i["addresses"][0]["telephone_number"]
                for j in i["taxonomies"]:
                    if j["primary"] == True:
                        category = j["desc"]   
                rows.append([organization,address, telephone, category])
                
                        
            count += 1
#           end = len(data["results"][0]["addresses"][0])
            
    hospital_data = pd.DataFrame(rows,columns = ["Organization Name", "Address", "Tel-no", "Category"])
    
    hospital_data.drop_duplicates(inplace=True)
    
    hospital_data.to_csv('hospital_list.csv', index = False)
    
    hospital_data["Category"].drop_duplicates().to_csv('hospital_categories.csv', index = False)
    
    return hospital_data 
    

if __name__ == "__main__":
    hospital_list()




