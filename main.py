# install pyttsx3-python text to speech version 3
# command - pip install pyttsx3
# install PyPDF2
# command - pip install PyPDF2

import pyttsx3
import PyPDF2
speaker = pyttsx3.init()

voices = speaker.getProperty('voices')             # change voice male=0,female=1
speaker.setProperty('voice', voices[1].id)

Book = open('motivation.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(Book)
pages = pdfReader.numPages
print(pages)
for i in range(7,pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)  # take input message to speak
    speaker.runAndWait()  # to speak

