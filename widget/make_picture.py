import openai
import requests
import json
from io import BytesIO
from PIL import Image
import os
from pathlib import Path

openai.organization = "org-vv0KaJTL3IYxLPNCW6KBNrKh"
openai.api_key      = "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"

# ユーザーのホームディレクトリのパスを取得する
home_dir = str(Path.home())

# 一時ファイルの保存先ディレクトリを作成する
temp_dir = os.path.join(home_dir, "temp")
os.makedirs(temp_dir, exist_ok=True)

# 一時ファイルの保存先パスを指定する
temp_file = os.path.join(temp_dir, "file.png")

# Read the image file from disk and resize it
image = Image.open("/Users/yamamotokenta/Desktop/myprojects/mail_tool/widget/picture/rina.png")
width, height = 256, 256
image = image.resize((width, height))

# Convert the image to a BytesIO object
byte_stream = BytesIO()
image.save(byte_stream, format='PNG')
byte_array = byte_stream.getvalue()

# Save BytesIO to a temporary file
with open(temp_file, "wb") as f:
    f.write(byte_stream.getvalue())

# Open the temporary file
with open(temp_file, "rb") as f:
    response = openai.Image.create_variation(
        image=f,
        n=1,
        size="1024x1024"
    )
# Delete the temporary file
# os.remove(temp_file)
image_url = response['data'][0]['url']
image_data = requests.get(image_url).content
with open("/Users/yamamotokenta/Desktop/myprojects/mail_tool/widget/picture/chat-gpt-generated-image.jpg", "wb") as f:
    f.write(image_data)
# return image_url