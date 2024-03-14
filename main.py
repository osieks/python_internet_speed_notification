from win10toast import ToastNotifier
import speedtest   
import datetime

toast = ToastNotifier()
st = speedtest.Speedtest() 

output = ""

output = output + "Download: " + str(st.download()/1000/1000)+ " Mbit\n"
#output = output + "Download: " + str(st.download()/1024/1024)+ " Mbit\n"
print(output)

output = output+ "Upload: " + str(st.upload()/1000/1000) + " Mbit\n"
#output = output+ "Upload: " + str(st.upload()/1024/1024) + " Mbit\n"
print(output)

servernames =[]     
st.get_servers(servernames)   
output = output+ "Ping: " + str(st.results.ping)+ " ms\n"
print(output)
  
toast.show_toast(
    "Speedtest Results",
    output,
    duration = 60,
    icon_path = "c:/Users/mateu/OneDrive/python_internet_speed_notification/icon.ico",
    threaded = False,
)

with open("wyniki.txt", "a") as myfile:
    myfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    myfile.write(output)