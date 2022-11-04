# Import python modules
import json

# Import third party modules
import openai


class DallE:
    def __init__(self):
        self.api_key = self.get_api_key()

    def create_images(self, prompt: str, size: str, n: int) -> list:
        """
        Create an image using the Dall-E model.

        Args:
            prompt (str): The text prompt for creating the image.
            size (str): The dimensions of the image to be created. E.g.
                "1024x1024".
            n (int): The number of images to be created.

        Returns:
            list: A list of urls to the images.
        """
        openai.api_key = self.api_key

        # The response from the API
        response = openai.Image.create(prompt=prompt, size=size, n=n)

        # Get all the urls of the images
        image_urls = []
        for image in response["data"]:
            image_urls.append(image["url"])

        # Print the url of the image
        return image_urls

    def get_api_key(self) -> str:
        """
        Get the API key from the auth file.

        Returns:
            str: The API key.
        """
        with open("auth.json") as f:
            settings = json.load(f)
            return settings["apiKey"]
