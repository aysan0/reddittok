from src.Openai.openai import OpenAI
from ..Reddit.utils import readOpenAIConfig

class opean_ai():
  def __init__(self) -> None:
    pass

  def text_to_tiktok_text(self,json_object):  
    # config
    config = readOpenAIConfig()
    secret = config.get('"api-key"')
    client = OpenAI(api_key=secret)
    # extract string from json
    reddit_text = json_object["data"]

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a creative video script generator. Create a concise YouTube Shorts/TikTok video text from the following Reddit post:"},
        {"role": "user", "content": reddit_text}
      ]
    )

    print(completion.choices[0].message)


# TEST
Json_obj_test = {
  "data": "TIL director Michel Gondry found Jim Carrey's emotional state after a breakup \"so beautiful, so broken\" that he asked him to stay that way for one year to fit his character in Eternal Sunshine of the Spotless Mind"
}
opean_ai_class = opean_ai()
opean_ai_class.text_to_tiktok_text(Json_obj_test)