import pafy
url=input("Coloque a url do video do youtube:")
video= pafy.new(url)

audio = video.getbestaudio()

audios.download()

