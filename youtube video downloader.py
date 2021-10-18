from pytube import YouTube

link = input("Please enter the youtube URL : ")
yt = YouTube(link)
videos = yt.streams.all()
#stream all the format available for the video

video = list(enumerate(videos))
#will index all the format available in list starting with zero
for i in video:
    print(i)
    #will print all the format available of video with proper index

print("Please enter the desired option to download the format")
download_option = int(input("Enter the option : "))
#asking user that which format he wanted to download
download_video = videos[download_option]
download_video.download()  #for downloading the video

print("Downloaded Successfully")