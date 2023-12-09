import requests
from io import BytesIO
from PIL import Image

def download_and_save_image(url, destination_path):
    try:
        # Make a GET request to the image URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the image using PIL
            image = Image.open(BytesIO(response.content))

            # Save the image to the specified destination path
            image.save(destination_path)

            print(f"Image downloaded and saved to {destination_path}")

        else:
            print(f"Error: Unable to download the image. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example: Download an image of a cat
image_url = "https://placekitten.com/200/300"  # You can replace this URL with any image URL
destination_path = "downloaded_image.jpg"  # Change the file name and extension as needed

download_and_save_image(image_url, destination_path)
