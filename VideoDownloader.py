#Program using Pytube Library to Download youtube video/Audio via URL
# python VideoDownloader.py "(link)" -- the terminal command


from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print("Title :",yt.title)
print("Date Published :", yt.publish_date)


while True:
    Resolution = input("Enter if you want high(H) or Low(L) Resolution or Audio(A) only :")

    if  Resolution == 'H':

            yd = yt.streams.get_highest_resolution()
            break

    elif Resolution == 'L':
            yd = yt.streams.get_lowest_resolution()
            break

    elif Resolution == 'A':
            yd = yt.streams.get_audio_only()
            break
    else:
            continue


yd.download('C:\\Users\\Blues\\Videos\\Downloads') # replace with desired directory to store files
print("Download complete!")



