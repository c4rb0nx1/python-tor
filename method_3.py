from stem import Signal
from stem.control import Controller
import socket
import socks

# Configure the SOCKS proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

# Function to request a new Tor identity
def renew_tor_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password") #change it with your hash or password here.
        controller.signal(Signal.NEWNYM)

# Your code goes here
