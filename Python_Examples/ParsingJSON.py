import json
jsonStream = open("C:\\Users\\070951\\Documents\\GitExample3\\Data_Examples\\ExampleJSON.json","r")
jsonObj = json.load(jsonStream)

print(jsonObj['People'])
print(jsonObj['People'][0])