import socket
import random
from machine import Pin
from time import sleep

led_RED = Pin(5, Pin.OUT)
led_GREEN = Pin(4, Pin.OUT)
led_BLUE = Pin(0, Pin.OUT)

CONTENT = """\
HTTP/1.0 200 OK
Content-Type: text/html
<html>
  <head>
  </head>
  <body>
    <p>Hello #%d from MicroPython!</p>
    <a href="/toggle_red">Click here to toggle red LED hooked to pin 5</a><br>
    <a href="/toggle_green">Click here to toggle green LED hooked to pin 4</a><br>
    <a href="/toggle_blue">Click here to toggle blue LED hooked to pin 0</a>
  </body>
</html>
"""

def toggle_red():
    led_RED.value(1 - led_RED.value())

def toggle_green():
    led_GREEN.value(1 - led_GREEN.value())

def toggle_blue():
    led_BLUE.value(1 - led_BLUE.value())


def main():
    s = socket.socket()
    ai = socket.getaddrinfo(wlan.ifconfig()[0], 8080)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://10.59.1.166:8080/")

    l = [toggle_red(), toggle_green(), toggle_blue()]

    counter = 0
    while True:
        sock, addr = s.accept()
        print("Client address:", addr)
        stream = sock.makefile("rwb")
        req = stream.readline().decode("ascii")
        method, path, protocol = req.split(" ")
        print("Got", method, "request for")

        if path == "/toggle_red":
            toggle_red()
        elif path == "/toggle_green":
            toggle_green()
        elif path == "/toggle_blue":
            toggle_blue()


        while True:
            h = stream.readline().decode("ascii").strip()
            if h == "":
                break
            print("Got HTTP header:", h)
        stream.write(CONTENT % counter)
        stream.close()
        sock.close()
        counter += 1
        print()
