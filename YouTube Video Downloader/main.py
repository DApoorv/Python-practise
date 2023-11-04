'''
YouTube Video Downloader
Author: Ayushi Rawat
'''

#import the package

from pytube import YouTube


all_url=['https://youtu.be/npr48D72TlE', 'https://youtu.be/W8We0tKTmQ0', 'https://youtu.be/d4nsGrZTL98', 'https://youtu.be/auNGYPLoULc',
'https://youtu.be/mHTnEvWUrgk', 'https://youtu.be/Qz4LC9Pmo7Y', 'https://youtu.be/Vxz6FbfmaYA', 'https://youtu.be/haarhMEQVrs',
'https://youtu.be/4qLti8otrlI', 'https://youtu.be/Zs8H4uNKFSI', 'https://youtu.be/CUY-46gMXSw', 'https://youtu.be/ORzVHZlCP1U']
for i in range(len(all_url)):
    my_video = YouTube(all_url[i])

    print("*********************Video Title************************")
    #get Video Title
    print(my_video.title)

    print("********************Tumbnail Image***********************")
    #get Thumbnail Image
    print(my_video.thumbnail_url)

    print("********************Download video*************************")
    #get all the stream resolution for the 
    for stream in my_video.streams:
        print(stream)

    #set stream resolution
    my_video = my_video.streams.get_highest_resolution()

    #or
    #my_video = my_video.streams.first()

    #Download video
    my_video.download()