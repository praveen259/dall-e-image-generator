import os
import openai
from config import key

openai.api_key = "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"

response = openai.Image.create(prompt="a white siamese cat",
                               n=1,
                               size="1024x1024")
image_url = response['data'][0]['url']
print(image_url)
