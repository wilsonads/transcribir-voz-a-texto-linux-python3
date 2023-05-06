import speech_recognition as sr
import tkinter as tk
import pyperclip
from playsound import playsound

def reconocer_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Habla ahora...")
        audio = r.listen(source)
    
    try:
        texto = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {texto}")
        cuadro_texto.delete('1.0', tk.END)
        cuadro_texto.insert(tk.END, texto)
        pyperclip.copy(texto)
        # Reproducir el sonido
        playsound('beep.mp3')
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError:
        print("No se puede conectar con el servicio de reconocimiento de voz")

root = tk.Tk()
root.title("Reconocimiento de Voz")
root.geometry("12000x6000")

# Cambiar el modo de color a oscuro
root.configure(bg="#000000")

boton = tk.Button(root, text="Hablar", command=reconocer_audio)
# Cambiar el modo de color a oscuro para el botón
boton.configure(bg="#ffffff", fg="#000000")
boton.pack()

cuadro_texto = tk.Text(root, height=3)
# Cambiar el modo de color a oscuro para el cuadro de texto
cuadro_texto.configure(bg="#000000", fg="#ffffff")
cuadro_texto.pack()

root.mainloop()
