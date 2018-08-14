
""" 
this is a module,多行注释
"""
import re

from urllib import request
# BeautifulSoup:解析数据结构 推荐库 Scrapy:爬虫框架
#爬虫，反爬虫，反反爬虫
#ip 封
#代理ip库
class Spider():
    url='https://www.panda.tv/cate/lol'
    root_pattern='<div class="video-info">([\s\S]*?)</div>'
    name_pattern='</i>([\s\S]*?)</span>'
    number_pattern='<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r=request.urlopen(Spider.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
        a=1

    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_html:
            name=re.findall(Spider.name_pattern,html)
            number=re.findall(Spider.number_pattern,html)
            anchor={'name':name,'number':number}
            anchors.append(anchor)
        return anchors

    def __refine(self,achors):
        l=lambda anchor:{'name':anchor['name'][0].strip(),'number':anchor['number'][0]}
        return map(l,achors)

    def __sort(self,anchors):
        
        anchors=sorted(anchors,key=self.__sord_seed,reverse=True)
        return anchors

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('rank '+str(rank+1)+':'+anchors[rank]['name']
            +'    '+anchors[rank]['number']
            )
            

    def __sord_seed(self,anchor):
        r=re.findall('\d*',anchor['number'])
        number= float(r[0])
        if '万' in anchor['number']:
            number*=10000
        return number

    def go(self):
        htmls=self.__fetch_content()
        anchors=self.__analysis(htmls)
        anchors=list(self.__refine(anchors))
        anchors=self.__sort(anchors)
        self.__show(anchors)

splider=Spider()
splider.go()
