from lxml import etree as ET
# Get the XML Data
stream = open('C:\\Users\\070951\\Documents\\GitExample3\\Data_Examples\\ExampleXML.xml','r')

# Parse the data into an ElementTree object
xml = ET.parse(stream)

# Get root of Element object from the Element Tree
root = xml.getroot()

for e in root:

    # Prints the specific Value of element "Id"
    print(e.get("Id"))

    # Prints the elemet tree object to string
    print(ET.tostring(e))
    print("")

    #Prints each element within the Element Tree
    for i in e:
        print(ET.tostring(i))
    print("")

