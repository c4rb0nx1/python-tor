''' 
method 2 : using http.client , socks proxy and socket.

Note : instead of using http.client you can use bs4 or scrapy. 
'''
import http.client
import socks
import socket

# Configure the SOCKS proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

# Create an HTTP client
conn = http.client.HTTPSConnection("check.torproject.org") #url goes here

# Send a request
conn.request("GET", "/")

# Get the response
response = conn.getresponse()
data = response.read()

# Your crawler code here
print(data)   #prints if you are connected.
