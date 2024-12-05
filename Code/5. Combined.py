
#MP4 to MP3
from moviepy import VideoFileClip

def get_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)

    video.audio.write_audiofile(audio_path)



#MP3 to text
import torch
from transformers import pipeline

def get_text_from_audio(audio_path):
    whisper = pipeline("automatic-speech-recognition", "openai/whisper-large-v3", torch_dtype=torch.float16, device="cuda:0")

    transcription = whisper(audio_path)
    return transcription



#Text to Text
from dotenv import load_dotenv
import os
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def text_translation(google_api_key, transcription):
    desired_lang = input("Enter the language you want the translation: ")

    summary_prompt = """
    You are a translator where you have given an input: {input_text}
    And you need to translate this input text into {desired_language} language.
    """

    prompt_template = PromptTemplate(input_variables=["input_text", "desired_language"], template=summary_prompt)

    # Initialize the LLM with the API key
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=google_api_key
    )

    # Set up the chain
    chain = prompt_template | llm | StrOutputParser()

    # Invoke the chain
    res = chain.invoke({
        "input_text": transcription["text"],
        "desired_language": desired_lang
    })
    
    return res

if __name__ == "__main__":

    #MP4 to MP3
    video_path = "C:/Users/PickleRick/Desktop/Infosys springboard/Material/video1.mp4"
    audio_path = "C:/Users/PickleRick/Desktop/Infosys springboard/Material/audio1.mp3"

    get_audio_from_video(video_path, audio_path)



    #Mp3 to Text
    transcription = get_text_from_audio(audio_path)
    print(f"Extracted text from the audio: {transcription['text']}")


    #Text to text translation
    res = text_translation(google_api_key, transcription)

    print(res)
