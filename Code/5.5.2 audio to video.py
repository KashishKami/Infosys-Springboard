video_path = "C:/Users/PickleRick/Desktop/Infosys springboard/Material/video1.mp4"
audio_path = "C:/Users/PickleRick/Desktop/Infosys springboard/Material/converted.mp3"


from moviepy import *
videoclip = VideoFileClip(video_path)
audioclip = AudioFileClip(audio_path)

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("C:/Users/PickleRick/Desktop/Infosys springboard/Material/output.mp4")


