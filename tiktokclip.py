from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime

# Get the URL of the YouTube video from the user
video_url = input("Enter the URL of the YouTube video: ")

# Download the highest resolution stream from YouTube
yt = YouTube(video_url)
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# Cut the video into clips
video_clip = VideoFileClip(video)
duration = video_clip.duration

# Get the current timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Ask the user if they want to clip the whole video or just a single clip
clip_option = input("Do you want to clip the whole video or just a single clip? (Enter 'whole' or 'single'): ")

if clip_option == "whole":
    # Ask the user for a custom name for the whole clips
    custom_name = input("Enter a custom name for these whole clips: ")

    # Ask the user for the desired length of each clip
    clip_length = int(input("Enter the desired length of each clip (in seconds): "))

    # Clip the whole video into clips of desired length with a custom name and part number
    for i in range(0, int(duration), clip_length):
        start_time = i
        end_time = min(i + clip_length, duration)
        clip = video_clip.subclip(start_time, end_time)
        part_number = i // clip_length + 1
        clip.write_videofile(f"clip_{custom_name}_part{part_number}_{timestamp}.mp4")
elif clip_option == "single":
    # Ask the user for the start and end times of the clip
    start_time = float(input("Enter the start time of the clip (in seconds): "))
    end_time = float(input("Enter the end time of the clip (in seconds): "))

    # Ask the user for a custom name for the single clip
    custom_name = input("Enter a custom name for this single clip: ")

    # Create a single clip with a custom name
    clip = video_clip.subclip(start_time, end_time)
    clip.write_videofile(f"clip_{custom_name}_{timestamp}.mp4")
