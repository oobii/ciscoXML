from urllib.request import Request, urlopen
import ssl
import xml.dom.minidom

# https://github.com/CiscoDevNet/coding-skills-sample-code

# This restores the same behavior as before.
context = ssl._create_unverified_context()

req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
response = urlopen(req, context=context)
responseString = response.read().decode("utf-8")
dom = xml.dom.minidom.parseString(responseString)
xml = dom.toprettyxml()
print(xml)
floor_element = dom.firstChild
if floor_element.hasChildNodes :
    child = floor_element.firstChild
    while child is not None:
        if child.tagName == 'AccessPoint' :
            output = child.tagName + ": " + child.getAttribute('name') + '\t eth: ' + child.getAttribute('ethMacAddress')
            print(output)
        child = child.nextSibling
response.close()
