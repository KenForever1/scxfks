import urllib.request
import gzip
from io import BytesIO
import http.cookiejar

task = {
    "341683": "275",
    "341684": "275",
    "341695": "276",
    "341696": "276",
    "341706": "277",
    "341750": "281",
    "341777": "288",
    "341778": "289",
    "341779": "290",
    "341780": "290",
    "341781": "290",
    "341782": "290",
    "341783": "290",
    "341809": "293",
    "341811": "294",
    "341812": "295",
    "341813": "296",
    "341798": "292"
}

_course_id = "292"
_chapter_id = "341798"
Cookie_SERVERID = "SERVERID=7a14cc5dbf2846c4ccccc0732b49841f|1604668338|1604666788"

Cookie_JSession = " JSession=db24ad69-0de3-ddds-90c3-1df82b27dfb2; "

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


def study(course_id, chapter_id):
    learn_url = "http://xxpt.scxfks.com/study/course/" + course_id + "/chapter/" + chapter_id
    ok_url = "http://xxpt.scxfks.com/study/learn/" + chapter_id
    cookie_aff = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie_aff)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(url=learn_url,
                                     headers=headers1)
    try:
        # response = urllib.request.urlopen(request)
        response = opener.open(request)
    except urllib.error.URLError as e:
        print(e.reason)

    cookieStr = ""
    for item in cookie_aff:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"
    print(cookieStr)
    headers["Cookie"] = Cookie_JSession + cookieStr

    data = {}
    req = urllib.request.Request(ok_url, data, headers)
    with opener.open(req) as resp:
        htmls = resp.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        print(htmls)
    # id = id + 1


study(_course_id, _chapter_id)
