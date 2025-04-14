import json
import pandas as pd 

with open('json4.json','r') as file:
    data = json.load(file)
    
# print(data['plpList']['productList'])

result = data['data']
# print(result)
id = []
image = []
name = []
price = []

for result in result:
    id.append(result['_id'])    
    image.append(result['images'][0]['image'])    
    name.append(result['name'])
    price.append(result['price'])
    
    
asoc_df = pd.DataFrame({'id':id, 'name':name ,'image':image,'price':price })

asoc_df.to_excel('Products4.xlsx',index=False)  