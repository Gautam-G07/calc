import json

people_string='''
{
"people":[
{   
    "name":"John smith",
    "phone":"615",
    "Emails":["@gmail.com"],
    "has license":false
},
{
    "name":"John Doe",
    "phone":"9",
    "Emails":["gg.@gmail.com","Indiawin@gmail.com"],
    "has license":true
}
]
}
'''
data=json.loads(people_string)

print(type(data["people"]))
print(type(data))
for person in data["people"]:
    print(person["name"])
    del person["phone"]
new_string=json.dumps(data,sort_keys=True)
print(new_string)
with open('people.json','w') as f:
    json.dump(data,f)
     