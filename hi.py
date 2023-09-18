import requests
import os

# Define the URL of the shared file on Google Drive
file_url = 'https://drive.google.com/file/d/1YqDPIWrfx1TGGRO58jRakCTFuQVz1a67/view'

# Define the local file path where you want to save the downloaded model
local_file_path = 'inception123.tflite'

# Download the file from Google Drive
response = requests.get(file_url)

# Check if the request was successful
if response.status_code == 200:
    # Save the downloaded content to the local file
    with open(local_file_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {local_file_path} successfully.")
else:
    print("Failed to download the file.")
