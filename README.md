**Project Title: Multilingual OCR and Speech Synthesis Tool**
Overview:
This project enables optical character recognition (OCR) from images, language translation, and text-to-speech synthesis.

Setup:
Ensure Python is installed.
Install dependencies using pip install -r requirements.txt.
Set up Tesseract OCR: Download and install Tesseract OCR and specify the executable path in the code.

Usage:
Run the script: python image_processing.py.
Input the image path when prompted.
View the original text, translated text (e.g., to Hindi), and hear the synthesized speech.

Example:
Image used: 'ELON Musk.jpg'
Dependencies:
Python libraries: sys, PIL, pytesseract, googletrans, pyttsx3.

Configuration:
Set console encoding to UTF-8 for text compatibility.
Tesseract OCR executable path specified for proper integration.
pyttsx3 initialized for text-to-speech conversion.

Note:
Adjust the target language for translation by modifying the target_language parameter.
Customize Tesseract OCR path if necessary.
