import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as kaynak:
    print("Bir sey söyleyin! (eng.)")
    ses = r.listen(kaynak)


try:
    print("Sphinx'in anladıgı: " + r.recognize_sphinx(ses))
except sr.UnknownValueError:
    print("Sphinx bir cikarimda bulunamadi.")

result = r.recognize_sphinx(ses)

url = f"https://www.google.com.tr/search?q={result}"
webbrowser.open_new_tab(url)

