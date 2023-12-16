from urllib import response
import requests

api_id = '17462195'

api_key ='223e2054578ee92dd4871086cd2962e'


nutrition_header ={

    'x-app-id':api_id,
    'x-app_key': api_key,
    'Content_Type':'application/json'
}

nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutrition_json = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response = requests.post(url=nutrition_endpoint,json=nutrition_json,headers=nutrition_header)
print(response.text)