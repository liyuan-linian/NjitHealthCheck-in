# NJIT Health Check-in

## 版本说明
V1.0: 帮助完成体温打卡，以防缺漏

V2.0: 加入深信服webvpn

v3.0: 修改了一个字节大小错误，添加了定时触发任务

## 文件说明
* `clock.py`: 主程序
* `vpn.py`: 深信服webvpn登录
* `webvpn.py`: 深信服webvpn的url转换
* `get_session.py`: 在licsber.wisedu.get_session.py的基础上增加webvpn环境下的authserver

## 依赖关系
* [liscber 5.5.0](https://github.com/Licsber/licsber-pypi)
* json

## 测试环境
* Python 3.6

## 打卡方式
* 默认公网打卡

## 声明
* 本项目仅供南京工程学院在校生测试使用，使用时请如实申报个人健康信息
* 由于校园网的不稳定因素，本项目偶尔失效
* 禁止将本项目或者与本项目相关的思路用于商用或非法用途！(包括但不限于: 提供有偿的体温打卡服务, 利用webvpn违规爬虫)

Tips:体温打卡可与腾讯云云函数一同食用  
