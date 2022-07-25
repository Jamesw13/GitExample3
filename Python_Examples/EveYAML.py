import yaml
from yaml import load, load_all

stream = open('C:\\Users\\070951\\Documents\\GitExample3\\Data_Examples\\typeIDs.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))

for i in documents:
    print(type(i))