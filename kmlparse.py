# Google Earth kml文件根属性一定要设置为<kml xmlns:dc="http://www.opengis.net/kml/2.2">才能解析成功 默认的是xmlns，必须加上dc
# 2019年9月7日 17:21:55
# Https://ROCEYS.CN

import sys
import xml.etree.ElementTree as kml

print(sys.getfilesystemencoding())
nodels = kml.parse("googlemaps.kml")

i = 0
with open("sb.txt", "wt", encoding="utf-8") as wfile:
    for item in nodels.iterfind('Document/Folder/Placemark'):
        name = item.findtext('name')
        print(name, file=wfile)
        print("\n", file=wfile)
        i += 1
        if i == 337:
            break
