from google import genai
from google.genai import types


client = genai.Client(api_key="AIzaSyDfyZkUdXAj3viiRXfPeK437FMkdksvddI")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=types.Part.from_text(text="What is the capital of France?"),
)

print(response.text)