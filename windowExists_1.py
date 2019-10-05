from win32 import win32gui as w
from datetime import datetime, date
import time
today = date.today()

# datetime object containing current date and time
str2 = ""
var1 = 1
while True:
    now = datetime.now()
    file2 = open(str(today.year)+"_"+str(today.month)+"_"+str(today.day)+".txt","a+")
    str_1 = w.GetWindowText (w.GetForegroundWindow())
    str1 = "Following is the activity going on |" + str_1 + "| Date & Time: |" + str(now)
    
    
    if var1 == 1:
        file2.write(str1 + "\n")    
        str_2 = w.GetWindowText (w.GetForegroundWindow())
        var1 = 0
    #time.sleep(5) 
    if str_2 != str_1:
        #print(str_2 + "---" + str_1)
        str2 = "Following is the activity going on |" + str_1 + "| Date & Time: |" + str(now)
        file2.write(str2 + "\n")
        #print(str1)
        str_2 = str_1
        file2.close()
