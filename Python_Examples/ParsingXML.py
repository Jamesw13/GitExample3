from lxml import etree as ET
import xmltodict
# Get the XML Data
stream = open('C:\\Users\\070951\\Documents\\GitExample3\\Data_Examples\\ExampleXML.xml','r')

# Parse the data into an ElementTree object
xml = ET.parse(stream)

# Get root of Element object from the Element Tree
root = xml.getroot()

for e in root:

    # Prints the specific Value of element "Id"
    print(e.get("Id"))
    print(e.get("FirstName"))
    # Prints the elemet tree object to string
    print(ET.tostring(e))
    print("")

    #Prints each element within the Element Tree
    for i in e:
        print(ET.tostring(i))
    print("")


# Parse the XML file into an 'Ordered Dict'
stream2 = open('C:\\Users\\070951\\Documents\\GitExample3\\Data_Examples\\ExampleXML.xml','r')
try:
    xml2 = xmltodict.parse(stream2.read())
except xmltodict.expat.ExpatError:
    print("Your XML Parser Is Fooked!")
for e in xml2["People"]["Person"]:
    print(e)

#for e in xml:
 #   print(e)
