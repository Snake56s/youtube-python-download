from pytube import YouTube, exceptions, Playlist
import os

def Descargar(url,tipo):
    if not os.path.exists("descargas/"):
        os.makedirs("descargas/audio")
        os.makedirs("descargas/video")
    try:
        yt = YouTube(url)
        destino = "descargas/video/"
        if(tipo == "Video"):
            tipo = "mp4"
            destino = "descargas/video/"
            streams = yt.streams.filter(progressive=True, file_extension=tipo).order_by('resolution').desc().first().download(output_path=destino)
        else:
            tipo = "mp3"
            destino = "descargas/audio/"
            streams = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            out_file = streams.download(output_path=destino)
            base, ext = os.path.splitext(out_file)
            new_file = base+ '.mp3'
            os.rename(out_file,new_file)  
        return True
    except exceptions.RegexMatchError:
        return False


def descargar_play_list(url,tipo):
    playlist = Playlist(url)
    if not os.path.exists("descargas/"):
        os.makedirs("descargas/audio")
        os.makedirs("descargas/video")
    try:
        destino = "descargas/video/"
        if(tipo == "Video"):
            tipo = "mp4"
            destino = "descargas/video/"
            print('Number of videos in playlist: %s' % len(playlist.video_urls))
            for video in playlist.videos:
                titulo = video.title
                print("Descargando video "+titulo)
                video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first().download(output_path=destino)
                print("Descargado: "+titulo)
        else:
            tipo = "mp3"
            destino = "descargas/audio/"
            for audio in playlist.videos:
                titulo = audio.title
                print("Descargando audio de "+titulo)
                out_file = audio.streams.filter(only_audio=True).order_by('abr').desc().first().download(output_path=destino)
                base, ext = os.path.splitext(out_file)
                new_file = base+ '.mp3'
                os.rename(out_file,new_file)
        return True
    except exceptions.RegexMatchError:
        return False
    