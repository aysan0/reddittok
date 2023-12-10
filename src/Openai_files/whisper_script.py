from pathlib import Path
from openai import OpenAI
from utils import readOpenAIConfig


class whisper_class:
    def __init__(self, text) -> None:
        self.text_from_gpt = text

    def text_to_mp3_file(self):
        # config
        config = readOpenAIConfig()
        secret = config.get('"api-key"')
        client = OpenAI(api_key=secret)

        speech_file_path = Path(__file__).parent / "test_speech.mp3"
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=self.text_from_gpt
        )

        response.stream_to_file(speech_file_path)

whisp = whisper_class("Alp aysan is a sexy motherfucker.")
whisp.text_to_mp3_file()