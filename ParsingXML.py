from xml.etree.ElementTree import etree as ET

# Get the XML Data
stream = open('ExampleXML.xml','r')

# Parse the data into an ElementTree object
xml = ET.parse(stream)

# Get root of Element object from the Element Tree
root = xml.getroot()

for e in root:
    print(e.get("Id"))
    print(ET.tostring(e))
    print("")
    for i in e:
        print(ET.tostring(i))
    print("")
    
