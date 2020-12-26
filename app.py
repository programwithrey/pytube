from tkinter import *
import pytube

#function
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:/Users/Admin/Desktop/Video")
        notif.config(fg="green",text = "Your video was complete")
    except Exception as e:
        print(e)
        notif.config(fg="red",text = "Your video could not be downloaded")

#main
master = Tk()
master.title("Youtube Downloader")

#label
Label(master, text = "Download any youtube video", fg = "red", font=("Calibri",15)).grid(sticky=N,padx=100,row=0)
Label(master,text="Enter the video link down below",  font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
notif = Label(master,font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=4)
#Vars
url = StringVar()
#entry
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)
#Button
Button(master,width=20,text = "Download",font=("Calibri",12),command=download).grid(sticky=N,row=3,pady=15)
master.mainloop()
