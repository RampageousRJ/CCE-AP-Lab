import json

json_obj = {
    "Name": "Rishabh", 
    "Branch":"CCE", 
    "Roll No.":20, 
    "Registration No.":210953080
    }

dumped = json.dumps(json_obj)
print(dumped + " " + str(type(dumped)))
print(json.loads(dumped), str(type(json.loads(dumped))))