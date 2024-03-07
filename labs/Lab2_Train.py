import requests
import csv
from xml.dom.minidom import parseString
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# check it works
print (doc.toprettyxml()) #output to console comment this out once you know it works

# Store the xml in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)