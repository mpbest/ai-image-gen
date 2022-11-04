# Import local libraries
from DallE import DallE


def main():
    # Create an instance of the DallE class
    dall_e = DallE()

    # Text prompt for creating image
    prompt = """
    A dog is running in the grass.
    """
    # The dimensions of the image to be created
    size = "1024x1024"
    # The number of images to be created. Between 1 & 10.
    n = 1

    # Create the images
    image_urls = dall_e.create_images(prompt=prompt, size=size, n=n)

    # Print the url of the images
    for url in image_urls:
        print("\n")
        print(url)


if __name__ == "__main__":
    main()
