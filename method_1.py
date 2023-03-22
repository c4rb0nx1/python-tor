import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050",
}
url = input("enter your URL: ")
response = requests.get(url, proxies=proxies)
content = response.content
print(content)

# Your code goes here....
