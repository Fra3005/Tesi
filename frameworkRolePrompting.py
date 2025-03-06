from openai import OpenAI
import google.generativeai as genai
import os
from mistralai import Mistral



# client = OpenAI(api_key="sk-HYwxyT0_NRhwziNbDIqsYKmH-SEkek7EGnKMh9yBqYT3BlbkFJx_qo2qgvWrVOJxpzYvL7_7D6e4R-ZKFXe8G02eItQA")

# api_key_gemini="AIzaSyCKgTS3C2QriLCElWp2_pr3qo6TwumrdlE"
# genai.configure(api_key=api_key_gemini)

#Role prompting Llama


#Role prompting Gemini
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(prompt)
# print(response.text)

#Role prompting gpt-4o-mini
# stream = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": prompt}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

#Role prompting Gpt 3.5
# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     messages=[{"role": "user", "content": prompt}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")





