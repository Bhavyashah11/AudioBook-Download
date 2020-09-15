from pytube import YouTube
import moviepy.editor
import requests
from bs4 import BeautifulSoup
import os
import time

url=input("Enter the url of youtube video: ")
yt=YouTube(url)
youtube=yt.streams.first()     #filter(only_audio=True)
#print(youtube[2])

print("\n--Warning--: The folder should be empty or else an error might occur\n")
path=input("Enter the path where you want to save the audio file or press press 1 to save in the default directory: ")
if path=="1":
    path="Default path"
    video=youtube#[number-1]
    video.download(path)
else:
    video=youtube#[number-1]
    video.download(str(path))
i=0

for file in os.listdir(path):
    new_file="output.mp4"
    os.rename(path+'/'+file,path+'/'+new_file)
    #print(file)

video=moviepy.editor.VideoFileClip(path+"\output.mp4")
audio=video.audio
audio.write_audiofile(path+"\output.mp3")
time.sleep(15)
os.remove(path+"\output.mp4")
print("downloaded")

