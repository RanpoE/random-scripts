from pytube import YouTube

video_link = 'https://www.youtube.com/watch?v=Pws-CsNdS8M'

video = YouTube(video_link)

video.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
