import json
import time
from licsber.wisedu.get_session import *
import schedule


#信息门户账号,密码,手机号 (必填)
EHALL_USER = ''
EHALL_PWD = ''
PHONE_NUMBER = ''


LOGIN_URL = 'http://authserver.njit.edu.cn/authserver/login?service=http%3A%2F%2Fehall.njit.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.njit.edu.cn%2Fnew%2Findex.html'
GET_URL = 'http://ehallapp.njit.edu.cn/publicapp/sys/lwNjitHealthInfoDailyClock/index.do#/healthClock'
QUERY_URL = 'http://ehallapp.njit.edu.cn/publicapp/sys/lwNjitHealthInfoDailyClock/modules/healthClock/V_LWPUB_JKDK_QUERY.do'
TIME_URL = 'http://ehallapp.njit.edu.cn/publicapp/sys/lwpub/api/getServerTime.do'
SAVE_URL = 'http://ehallapp.njit.edu.cn/publicapp/sys/lwNjitHealthInfoDailyClock/modules/healthClock/T_HEALTH_DAILY_INFO_SAVE.do'

URL_DICT = { 'LOGIN_URL': LOGIN_URL, 'GET_URL': GET_URL, 'QUERY_URL': QUERY_URL, 'TIME_URL': TIME_URL, 'SAVE_URL': SAVE_URL }


#公网访问(二选一)
s = get_wisedu_session(URL_DICT['LOGIN_URL'], EHALL_USER, EHALL_PWD)

s.get(URL_DICT['GET_URL'])

#查询个人信息: 学号, 姓名, 院系编号, 学院名称
res = s.post(URL_DICT['QUERY_URL'])
info_dict = json.loads(res.text)['datas']['V_LWPUB_JKDK_QUERY']['rows'][0]

user_id = info_dict['USER_ID']
user_name = info_dict['USER_NAME']
dept_code = info_dict['DEPT_CODE']
dept_name = info_dict['DEPT_NAME']

#获取服务器时间，可改为本地时间
#时间格式: 2021-09-26 09:51:06
res = s.post(URL_DICT['TIME_URL'])
date = json.loads(res.text)['date']
date = str(date).replace('/','-')

#data_am: 上午提交的信息; data_pm: 下午提交的信息
#BY3字段决定了打卡类型, 001:晨间打卡, 002:晚间打卡
data_am = {
    "USER_ID":user_id,
    "USER_NAME":user_name,
    "DEPT_CODE":dept_code,
    "DEPT_NAME":dept_name,
    "PHONE_NUMBER":PHONE_NUMBER,
    "FILL_TIME":date,
    "BY3": "001",
    "CLOCK_SITUATION":"江苏省南京市江宁区南京工程学院",
    "TODAY_SITUATION":"001",
    "TODAY_VACCINE_CONDITION":"002",
    "TODAY_BODY_CONDITION":"011",
    "TODAY_TEMPERATURE":"002",
    "TODAY_HEALTH_CODE":"001",
    "TODAY_TARRY_CONDITION":"001",
}

data_pm = data_am.copy()
data_pm['BY3'] = '002'



#上午打卡
def morning():
    res = s.post(URL_DICT['SAVE_URL'], data=data_am)
    print(res.text)
#下午打卡
def afternoon():
    res = s.post(URL_DICT['SAVE_URL'], data=data_pm)
    print(res.text)

schedule.every().day.at("07:30").do(morning)
schedule.every().day.at("13:30").do(afternoon)

while 1:
    schedule.run_pending()
    time.sleep(1)

