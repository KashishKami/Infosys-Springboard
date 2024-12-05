from moviepy import VideoFileClip

# Load the video file
video = VideoFileClip("C:/Users/PickleRick/Desktop/Infosys springboard/Material/video1.mp4")

# Extract and save the audio as MP3
video.audio.write_audiofile("C:/Users/PickleRick/Desktop/Infosys springboard/Material/audio1.mp3")