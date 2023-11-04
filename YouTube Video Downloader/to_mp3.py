# importing packages
from pytube import YouTube
import os

songs_list = []

for i in range(len(songs_list)):
	yt = YouTube(songs_list[i])

	# extract only audio
	video = yt.streams.filter(only_audio=True).first()

	# check for destination to save file
	destination = 'E:\Ayushi Rawat\Youtube-Projects\YouTube Video Downloader\mp3'

	# download the file
	out_file = video.download(output_path=destination)

	# save the file
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)

	# result of success
	print(yt.title + " has been successfully downloaded.")



