from PIL import Image
import pyautogui
import pytesseract
import time
import re


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Enhance the image by reducing its color depth


def enhance_image(image):
    image = image.convert("L")
    image = image.point(lambda x: 0 if x < 128 else 255, "1")
    image.save("enhanced.png")
    return image


# Take a screenshot and save it to a file


def take_screenshot(x, y, width, height, file_name):
    image = pyautogui.screenshot(region=(x, y, width, height))
    image.save(file_name)

# Convert an image to a string using Tesseract


def img_to_string(image):

    return pytesseract.image_to_string(image)

# Search for a number in a list of words


def find_number(words):
    for word in words:
        digits = re.findall(r"\d", word)
        if digits:
            number = "".join(digits)
            return number
    return None

# Sentinel function that searches for a specific number in the screen


def centinela():

    # Take a screenshot and save it to a file
    take_screenshot(680, 390, 300, 250, "screenshot.png")

    # Open the image file and enhance it
    image = Image.open("screenshot.png")
    image = enhance_image(image)

    # Convert the image to a string
    text = img_to_string(image)

    print(text)

    # Split the text into words
    words = text.split()

    # Search for a number in the list of words
    number = find_number(words)

    # If a number is found, write it in the application and terminate the function
    if number is not None:
        print(f"Found number: {number} ")
        pyautogui.press("enter")
        pyautogui.write(f"/centinela {number}")
        pyautogui.press("enter")
        return

# Main function that executes the sentinel function in an infinite loop


def main():
    print("Running centinela.")
    while True:
        centinela()
        time.sleep(1)


# Run the main function
if __name__ == "__main__":
    main()
