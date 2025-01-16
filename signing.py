import requests  # 导入requests库，用于发送HTTP请求
import json  # 导入json库，用于处理JSON数据
import time   # 导入time库，用于时间控制

#习讯云签到脚本
import datetime

# 获取当前日期
today = datetime.date.today()

# 获取今天是星期几（0表示星期一，6表示星期天）
weekday = today.weekday()

# 创建一个简单的数组来表示星期几
weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
   
data={'account':'220723233',#账号
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'5.1.5',
      'key':'',
      'model':'SM-G955N',
      'password':'Zrc200409020309!',#密码
      'platform':'2',
      'registration_id':'160a3797c8437218079',
      'request_source':'3',
      'school_id':'2025',#学校代码
      'system':'4.4.2',
      'uuid':'48:45:20:B9:D7:19'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com/login/api?from=app&version=5.1.5&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)#登陆成功后返回的信息
token=login_data['data']['token']

#经度
longitude = 'wPnoaLJc1SbCjDvRCTqRu5FNj3CDf2Eq7qoNNbPGVkVQA8P3B287msb1S5v3nuX47MSBZgvSpyzvqNin537e1WkHWAFuncOKq8rgyeVQP8DMt0FBzRto8XH99aSQWoTo1tdtzaYAv/c1EPYzeQo75QciPS9snO5394dJNU3ufJkIQAifD4/lvpGWwW3LYg8Julq9ojaQX4oNLHjE9HPdQbdxMI1TNyY+W6rAPuOkxjd43s1/yPJRhct0cgNHJezHhg6/gf8lZOEn0KRlfBhlaUnbjE8Y4myHA7k0RGq5EgHXAVwDy747X34d3LpfJaf7Yi9EoW4qm9MosY7yzSWixw=='
#维度
latitude = 'jeWPu8yfLOIcVnOWLSCIlB1rt9BkpS63bDUEc7gYPKmh0eNsF0KizsTh2481iwlaZWDD+yeCG9y41XPvEp+K6npflFRK7q2dY6NvMqIXqFFD855hvUCsSLrWWPz32/y+y+nN9SIANIQNDSeZ7ZfYOgXPZjknedUrSghHxP10wVZit5B34gTfi5wLt9dY3kRAkOb8OtNnIVj11VYlBQQyYAkchYLkBwVdNSF44v3wg9/usDz4q4vlk8/FSsnPpitdha5LlaOt4if2mpKlB8mIm7NnflTuVjY4vDZUwHr86qnxWnuT3XIotrYfVxQzIGBF8rQGhkHD2wUtc40uwy7Nmw=='
time.sleep(3)

sign_url='https://api.xixunyun.com/signin_rsa?token='+token+'&entrance_year=0&graduate_year=0&school_id=2025'
sign_data={'address':'浙江省嘉兴市桐乡市乌镇镇直通乌镇产业园',#签到地址
           'address_name':'直通乌镇产业园',#签到地点名称
           'change_sign_resource':'0',
           'comment':'',
           'latitude':latitude,
           'longitude':longitude,
           'remark':'0',
    }
if weekdays[weekday] == '星期日':
    print('今天无需签到')
else:
      sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
      sign=json.loads(sign_request.text)
      print(sign)

