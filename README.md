# kb-task-6
YouTube Video Downloader (Python CLI Project)
Project Overview
This Python CLI utility allows you to download YouTube videos directly to your computer using the powerful yt-dlp library. Users simply enter the video URL and destination folder, and the script fetches and saves the highest quality video—including both audio and video—for offline access.

This project was designed to practice API usage, user input handling, error management, and building real-world automation tools in Python.

Features
Downloads any public YouTube video by pasting the video URL

Allows user to set the destination folder for saving videos

Merges best available audio and video streams for full playback compatibility

Handles YouTube Shorts and most video formats robustly

Provides clear status messages and user-friendly error handling

Uses yt-dlp, a modern fork of youtube-dl, for reliable downloads

How to Run
Make sure Python is installed.

Install yt-dlp if you have not already:

text
pip install yt-dlp
Save the script as youtube_downloader.py.

Open a terminal in the script’s directory and run:

text
python youtube_downloader.py
Enter the YouTube video URL and the target folder when prompted.

Example Usage
text
Enter YouTube video URL: https://youtube.com/watch?v=abc123xyz
Enter destination folder: D:\Videos
Download complete!
What I Learned
Leveraged third-party libraries (yt-dlp) for complex web automation

Explored practical user input flow and directory handling

Got hands-on experience with error handling and status reporting

Improved confidence in building real media tools and working with online APIs

Potential Improvements
Add support for playlist downloads or selecting video quality

Display download progress bar

Automate download of captions/subtitles

GUI implementation for cross-platform usability

