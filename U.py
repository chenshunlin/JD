import urllib
import urllib2
import re
import json
import sys
import time
import requests
#输出中文+字符串报错
#reload(sys)
#sys.setdefaultencoding('utf-8')
def get_bs():
    #商品编号
    code = ['3205226', '7191760', '422539', '7202389']
    goods = [u'爱他美奶粉', u'西数硬盘2T', u'伊利奶粉', u'纸尿片']
    desp='  '
    n=0
    for x in code: 
        #请求地址
        url='https://p.3.cn/prices/mgets?skuIds=J_'+x
        #print (url)
        #获取地址
        request=urllib2.Request(url)
        #打开连接
        response=urllib2.urlopen(request)
        content=response.read()
        #print (content)
        result=json.loads(content)
        jsons=result[0]
        desp=desp+ goods[n] +u': ' + jsons['p'] +u'元\r\n\n'+'  ' #两个空格是换行
        n=n+1
        time.sleep(3)
        
    
    
    #print (desp)
    
    
    api = "https://sc.ftqq.com/SCU136378T227abd8c63d90e561dae11e27453d19a5fdacb239de7e.send"
    title = u"关注的商品价格"
    data = {
    "text":title,
    "desp":desp
    }
    req = requests.post(api,data = data)

if __name__ == "__main__":
    get_bs()
