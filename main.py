import sys

# Change console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

from PIL import Image
import pytesseract
from googletrans import Translator
import pyttsx3

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

# Initialize the Translator
translator = Translator()

def extract_text_from_image(image_path):
    # Open the image file using PIL
    img = Image.open(image_path)

    # Use pytesseract to perform OCR on the image and extract text
    text = pytesseract.image_to_string(img)

    # Return the extracted text
    return text

def translate_text(text, target_language='hi'):  # Change 'en' to 'hi' for Hindi
    # Use googletrans library to translate text
    translation = translator.translate(text, dest=target_language)
    
    # Return the translated text
    return translation.text

def convert_text_to_speech(text):
    # Use the text-to-speech engine to convert text to speech
    tts_engine.say(text)
    tts_engine.runAndWait()

# Example usage of the functions
image_path = r'C:\Users\Lenovo\Desktop\New folder\ELON Musk.jpg'
result_text = extract_text_from_image(image_path)

# Print the extracted text
print("Original Text:", result_text)

# Translate the extracted text to Hindi
translated_text = translate_text(result_text, target_language='hi')
print("Translated Text (Hindi):", translated_text)

# Convert the translated text to speech
convert_text_to_speech(translated_text)
