from utils import readOpenAIConfig
from opeanai import OpenAI


class opean_ai_class():
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
        {"role": "system", "content": "You are a creative video script generator. Create a concise YouTube Shorts/TikTok video text from the following text pulled from a Reddit post:"},
        {"role": "user", "content": reddit_text}
      ]
    )

    print(completion.choices[0].message)


# TEST
Json_obj_test = {
  "data": "TIL director Michel Gondry found Jim Carrey's emotional state after a breakup \"so beautiful, so broken\" that he asked him to stay that way for one year to fit his character in Eternal Sunshine of the Spotless Mind"
}
op_class = opean_ai_class()
op_class.text_to_tiktok_text(Json_obj_test)