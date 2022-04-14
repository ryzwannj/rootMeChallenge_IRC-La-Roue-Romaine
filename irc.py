import socket
import math
from time import sleep
import codecs


host = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
botname = "candy"
nick = "xwHelOlowx"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Connecting to the server:", host)
irc.connect((host, port))
sleep(1)
irc.send(("USER " + nick + " " + nick + " " + host + " " + nick + '\r\n').encode('utf-8'))
sleep(1)
irc.send(("NICK " + nick + '\r\n').encode('utf-8'))
sleep(1)
irc.send(("JOIN " + channel + '\r\n').encode('utf-8'))
sleep(2)
irc.send(("PRIVMSG "+ botname +" :"+ "!ep3" + "\r\n").encode('utf-8'))

running = True
while running:
    response = irc.recv(1024).decode("utf-8", "ignore")
    print(response)
    if response.startswith(":Candy!Candy@root-me.org PRIVMSG"):
        f1 = response.replace(":Candy!Candy@root-me.org PRIVMSG " + nick + " :", "")
        print(f1)
        results = codecs.encode(f1, 'rot13')
        print(results)

        irc.send(("PRIVMSG "+ botname +" :"+ "!ep3 -rep " + results +"\r\n").encode('utf-8'))


        



