import urllib.request
import gzip
from io import BytesIO
import http.cookiejar
from bs4 import BeautifulSoup as bs

paper_id_list = ["341749", "341806", "341807", "341808", "341756"]

paper_id = "341815"

Cookie_SERVERID = "SERVERID=7a14cc5dbf3856c4bdddd0732b39841f|1604668338|1604666788"

Cookie_JSession = " JSession=db24ad69-0de3-4d52-92c3-1df82b27dfb2; "

headers1 = {
    'Host': 'xxpt.scxfks.com',
    'Origin': 'http://xxpt.scxfks.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.75 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': Cookie_JSession + Cookie_SERVERID
}
headers = {
    'Host': 'xxpt.scxfks.com',
    'Origin': 'http://xxpt.scxfks.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.75 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def study(paper_id):
    url_getAnswer = "http://xxpt.scxfks.com/study/exercise/" + paper_id
    url_ok = "http://xxpt.scxfks.com/study/submitExercise/" + paper_id

    cookie_aff = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie_aff)
    opener = urllib.request.build_opener(handler)

    anwser = {}
    request = urllib.request.Request(url=url_getAnswer,
                                     headers=headers1)
    try:
        # response = urllib.request.urlopen(request)
        response = opener.open(request)
        htmls = response.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        print(htmls)
        html = bs(htmls, 'html.parser')

        ans = html.select('h3 label', class_='anwser')
        q_id = html.select('.item')

        for i in range(0, len(ans)):
            anwser[q_id[i].get('qid')] = ans[i].get('val')

        print(anwser)
    except urllib.error.URLError as e:
        print(e.reason)

    cookieStr = ""
    for item in cookie_aff:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"
    print(cookieStr)
    headers["Cookie"] = Cookie_JSession + cookieStr

    data = urllib.parse.urlencode(anwser).encode('utf-8')
    print(data)
    req = urllib.request.Request(url_ok, data, headers)
    with opener.open(req) as resp:
        htmls = resp.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        print(htmls)


study(paper_id)
