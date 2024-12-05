from pydub import AudioSegment
from pydub.silence import detect_silence, detect_nonsilent

original_audio_path = "C:/Users/PickleRick/Desktop/Infosys springboard/Material/audio1.mp3"
new_audio_path = "C:/Users/PickleRick/Desktop/Infosys springboard/Material/converted.mp3"

# Load the original and new audio
original_audio = AudioSegment.from_file(original_audio_path)
new_audio = AudioSegment.from_file(new_audio_path)

# Analyze the original audio for silence
silences = detect_silence(original_audio, min_silence_len=200, silence_thresh=-40)
nonsilent_sections = detect_nonsilent(original_audio, min_silence_len=200, silence_thresh=-40)

# Function to extract and align sections
def align_audio(original_sections, new_audio):
    aligned_audio = AudioSegment.silent(duration=0)  # Start with empty audio
    new_audio_pos = 0  # Keep track of position in new audio

    for start, end in original_sections:
        # Extract the corresponding duration from the new audio
        duration = end - start
        if new_audio_pos + duration <= len(new_audio):
            aligned_audio += new_audio[new_audio_pos:new_audio_pos + duration]
            new_audio_pos += duration
        else:
            # Loop the new audio if it runs out
            remaining = duration
            while remaining > 0:
                chunk = min(remaining, len(new_audio) - new_audio_pos)
                aligned_audio += new_audio[new_audio_pos:new_audio_pos + chunk]
                remaining -= chunk
                new_audio_pos = (new_audio_pos + chunk) % len(new_audio)

        # Add silence after each section
        aligned_audio += AudioSegment.silent(duration=200)  # Match original pause length

    return aligned_audio

# Match the nonsilent sections and align the new audio
aligned_audio = align_audio(nonsilent_sections, new_audio)

# Save the adjusted audio
aligned_audio.export("C:/Users/PickleRick/Desktop/Infosys springboard/Material/matched_audio.mp3", format="mp3")
print("Audio matched and saved as 'matched_audio.mp3'")
