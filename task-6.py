import yt_dlp

url = input("Enter YouTube video URL: ")
folder = input("Enter destination folder: ")

ydl_opts = {
    'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Save to folder with original title
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download complete!")
except Exception as e:
    print("Error:", e)
