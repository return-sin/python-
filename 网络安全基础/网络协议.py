# requests 比较适用于HTTP/HTTPS
import requests

response = requests.get("http://www.baidu.com")
print(response.status_code)  # 输出状态码
print(response.text)  # 输出网页内容

# socket 比较适用于TCP/UDP
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(1)

print("等待连接...")
client_socket, client_address = server_socket.accept()
print("连接成功")

data = client_socket.recv(1024)
print("收到数据", data.decode("utf-8"))

client_socket.send("Hello, Client".encode("utf-8"))
client_socket.close()

# DNS（域名系统）：将域名转换为IP地址
import socket

domain = "example.com"
ip_address = socket.gethostbyname(domain)
print(f"{domain}的ip是：{ip_address}")
