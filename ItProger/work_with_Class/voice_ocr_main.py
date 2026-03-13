import pytesseract
import speech_recognition as sr
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1.0)

    while True:
        print("Ready for command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-US').lower()
            print(f"Command: {command}")

            if "write file" in command:
                img = Image.open("photo.png")
                text = pytesseract.image_to_string(img, lang='eng')
                with open("image_text.txt", "w", encoding="utf-8") as file:
                    file.write(text)
                print("Saved to image_text.txt")

            elif "read file" in command:
                with open("image_text.txt", "r", encoding="utf-8") as file:
                    print(f"Content:\n{file.read()}")

            elif "exit" in command:
                print("Goodbye!")
                break
            else:
                print(f"Unknown: '{command}'. Available: write file, read file, exit.")

            time.sleep(1)

        except sr.UnknownValueError:
            pass