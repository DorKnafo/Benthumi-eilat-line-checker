import requests,time
from bs4 import BeautifulSoup
import os

lastline = 0

while True:
    try:
        ans = requests.get("http://eilat.dorbass.com/torshow.php")
        soup = BeautifulSoup(ans.content, 'html.parser')
        h3 = soup.find_all("h3")[0]
        line = int(str(h3.contents[0]).strip())
        if line > lastline:
            if os.name == 'posix':
                os.system('say -v "Good news" You are next in line')
            else:
                print('\a') #beep
            print "%s line: %d"%(time.strftime("%H:%M"),line)
        lastline = line
    except:
        print "Error checking server. Trying again in 30 seconds."
    time.sleep(30)
