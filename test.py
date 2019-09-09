from urllib.request import urlopen
import xml.etree.ElementTree as kml

nodels = kml.parse("test.kml")
root = nodels.getroot()
print(str(root))

n1 = nodels.findtext("channel/title")
print("tile is :>>>>"+str(n1))

for item in nodels.iterfind('channel/item'):
    name = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(name)
    print(date)
    print(link)
    print()
