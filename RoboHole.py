import time
import webbrowser
import os
import requests

browserExe = "iexplore.exe"
url = 'https://youtube.com'
#url = 'gestyy.com/ee27TQ'
testurl = 'https://httpbin.org/ip'

proxies = {'http': '52.204.10.67:80'}
r = requests.get(testurl, proxies=proxies)



i = 0
p = 0

def OpenUrl():
    r = requests.get(testurl, proxies=proxies)
    temp = r.html
    # f = open("home.html", "a")
    # f.write(temp)
    # f.close()
    webbrowser.open_new(temp)

while i <= 2000:
    OpenUrl()
    
    i += 1
    time.sleep(6)
    if (i % 5 == 0):
        time.sleep(2)
        os.system("taskkill /f /im "+browserExe)