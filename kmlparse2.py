# Google Earth kml文件根属性一定要设置为<kml xmlns:dc="http://www.opengis.net/kml/2.2">才能解析成功 默认的是xmlns，必须加上dc
# 2019-09-13 21:17:45
# Https://ROCEYS.CN

import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="googlemaps.kml")
root = tree.getroot()

print(root[0][0].text)
serbia = []
bosnia = []
lists = []

i = -1
with open("2019-09-13-serbiabosnia-bak.md", "wt", encoding="utf-8") as wfile:
    for elem in tree.iter(tag='Folder'):

        for country in elem:
            name = country.findtext('name')
            styleUrl = country.findtext('styleUrl')
            _data = {}

            if name != None:
                _data['name']=name
                print('### '+name,file=wfile)

            if styleUrl != None:
                _data['StyleUrl']=styleUrl
                print(styleUrl, file=wfile)

            for mark in country.iterfind('ExtendedData'):

                for data in mark.iter(tag='Data'):
                    attribName = data.get('name')
                    value = data.findtext('value')
                    desc = source = plan = other = picurl = urls = None

                    if attribName == '说明':
                        desc = value.strip()
                        _data['desc']=desc
                        print(desc, file=wfile)
                        print('\n', file=wfile)

                    elif attribName == '行程':
                        plan = value
                        _data['plan']=plan

                    elif attribName == 'Source':
                        source = value.strip()
                        _data['source']=source
                        print('来源：'+source+'\n',file=wfile)

                    elif attribName == 'gx_media_links':
                        picurl = value
                        urls = picurl.split(' ')
                        _data['picurls']=urls
                        for url in urls:
                            print(url, file=wfile)
                            print('\n', file=wfile)
                    else:
                        other = value

            for point in country.iterfind('Point'):
                gps = point[0].text.strip()
                gps = ','.join(gps.split(',')[-2:-4:-1])
                if gps != None:
                    # print('### '+name+'（'+gps+'）',file=wfile)
                    print('\n```js\nGPS:' + gps + '\n```', file=wfile)
                    _data['gps']=gps

            print('\n***\n',file=wfile)
            lists.append(_data)

            if i < 0 :
                serbia.append(_data)
            else:
                bosnia.append(_data)
        i += 1
        if i == 1:
            break

print(serbia)
print(bosnia)


def convertXML(lists,sfile):
    for pros in lists:
        if 'name' in pros.keys():
            n = pros['name']
            if n.find('（波黑）') > -1 or n.find('塞尔维亚Serbia') > -1 :
                print('## '+ n +'\n',file=sfile)
            else:
                print('### '+ n +'\n',file=sfile)

        if 'desc' in pros.keys():
            print('> '+pros['desc'].replace('\n','')+'\n',file=sfile)

        if 'picurls' in pros.keys():
            # print('```js',file=sfile)
            print('详情照片（有些是路标指示图有些是美食景点照片/需要翻墙）：',file=sfile)
            print('\n', file=sfile)
            for i,pl in enumerate(pros['picurls']):
                print('[图片'+str(i)+']('+pl+')',file=sfile)
                print('\n',file=sfile)

            # print('```\n',file=sfile)

        if 'StyleUrl' in pros.keys():
            print(pros['StyleUrl']+'\n', file=sfile)

        if 'gps' in pros.keys():
            # print(pros['gps'])
            print('> gps:需要精确经纬度文件的请联系本人获取\n',file=sfile)

        if 'source' in pros.keys():
            print('数据来源：'+pros['source']+'\n',file=sfile)
            print('***\n', file=sfile)
    return


with open("2019-09-13-serbiabosnia.md", "wt", encoding="utf-8") as sfile:
    print('---',file=sfile)
    print('layout: default',file=sfile)
    print('title: 塞尔维亚波黑景点网红餐厅酒店地标纪念碑旅行指南',file=sfile)
    print('subtitle: Serbia Bosnia and Herzegovina Attractions（Contain Precise GPS Coordinates）',file=sfile)
    print('apptitle: 塞尔维亚波黑景点网红餐厅酒店地标纪念碑旅行指南小红书马蜂窝穷游',file=sfile)
    print('category: blog',file=sfile)
    print('description: 该文是通过本人Google My Maps一键生成。',file=sfile)
    print('permalink: /:categories/:year/:month/:day/:title',file=sfile)
    print('author: ROCEYS',file=sfile)
    print('date: 2019/09/14',file=sfile)
    print('---',file=sfile)
    convertXML(serbia,sfile)
    convertXML(bosnia,sfile)

with open("2019-09-14-serbia.md", "wt", encoding="utf-8") as sfile:
    print('---',file=sfile)
    print('layout: default',file=sfile)
    print('title: 塞尔维亚景点网红餐厅酒店地标纪念碑旅行指南',file=sfile)
    print('subtitle: Serbia Attractions（Contain Precise GPS Coordinates）',file=sfile)
    print('apptitle: 塞尔维亚景点网红餐厅酒店地标纪念碑旅行指南小红书马蜂窝穷游',file=sfile)
    print('category: blog',file=sfile)
    print('description: 该文是通过本人Google My Maps一键生成。',file=sfile)
    print('permalink: /:categories/:year/:month/:day/:title',file=sfile)
    print('author: ROCEYS',file=sfile)
    print('date: 2019/09/14',file=sfile)
    print('---',file=sfile)
    convertXML(serbia,sfile)

with open("2019-09-14-bosnia.md", "wt", encoding="utf-8") as sfile:
    print('---',file=sfile)
    print('layout: default',file=sfile)
    print('title: 波黑景点网红餐厅酒店地标纪念碑旅行指南',file=sfile)
    print('subtitle: Bosnia and Herzegovina Attractions（Contain Precise GPS Coordinates）',file=sfile)
    print('apptitle: 波斯尼亚和黑塞哥维那景点网红餐厅酒店地标纪念碑旅行指南小红书马蜂窝穷游',file=sfile)
    print('category: blog',file=sfile)
    print('description: 波斯尼亚和黑塞哥维那，该文是通过本人Google My Maps一键生成。',file=sfile)
    print('permalink: /:categories/:year/:month/:day/:title',file=sfile)
    print('author: ROCEYS',file=sfile)
    print('date: 2019/09/14',file=sfile)
    print('---',file=sfile)
    convertXML(bosnia,sfile)

