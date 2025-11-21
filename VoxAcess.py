import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr # a biblioteca para o reconhecimento de voz
import os
import webbrowser
from datetime import datetime
from ttkbootstrap import Style
from ttkbootstrap.widgets import LabelFrame
from PIL import Image, ImageTk
from playsound import playsound
import pygame
import threading
import pywhatkit

class VoiceAssistantApp:
    # Configuração inicial da aplicação-------------------------------------------------------------------------------------
    def __init__(self, root):
            self.root = root
            self.root.title("VoxAcess")
            self.root.geometry("300x500")
            self.root.configure(bg="#1e1e1e")
            self.root.resizable(False, False)
            self.root.iconbitmap(r"C:\\Faculdade\\7 Periodo\\VoxAcess\\img\\VoxAcessimg.ico")

            pygame.mixer.init()
            self.recognizer = sr.Recognizer()
            
            # Campo superior com botão de configuração-----------------------------------------------------------------------
            self.top_frame = tk.Frame(root, bg="#1e1e1e")
            self.top_frame.pack(fill="x", padx=10, pady=(10, 0))

            self.top_entry = tk.Entry(self.top_frame, font=("Arial", 12), bg="#2a2a2a", fg="white", relief="flat")
            self.top_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 5))

            self.settings_icon = tk.Label(self.top_frame, text="⚙️", bg="#1e1e1e", fg="white", font=("Arial", 12))
            self.settings_icon.pack(side="right")

            # Área de resposta
            self.feedback_frame = tk.Frame(root, bg="#2a2a2a")
            self.feedback_frame.pack(padx=20, pady=30, fill="both", expand=True)

            self.feedback_label = tk.Label(
                self.feedback_frame,
                text="Clique no microfone para começar...",
                bg="#2a2a2a",
                fg="white",
                font=("Italic", 15),
                wraplength=250,
                justify="center"
            )
            self.feedback_label.place(relx=0.5, rely=0.5, anchor="center")

            # Botão de microfone
            mic_img = Image.open(r"C:\Faculdade\7 Periodo\VoxAcess\img\VoxAcessimg.ico").resize((70, 70))
            self.mic_icon = ImageTk.PhotoImage(mic_img)

            self.mic_button = tk.Button(
                root,
                image=self.mic_icon,
                bg="#1e1e1e",
                bd=0,
                activebackground="#333",
                command=self.on_mic_press,
            )
            self.mic_button.pack(pady=30)
        

    def on_mic_press(self):
        self.mic_button.config(bg="#333")
        self.root.after(150, lambda: self.mic_button.config(bg="#1e1e1e"))

        # Inicia a escuta com som (em thread separada para não travar UI)
        threading.Thread(target=self.play_and_listen).start()

    def play_and_listen(self):
        try:
            playsound(r"C:\Faculdade\7 Periodo\VoxAcess\buttom.mp3")  
        except:
            pass  
        self.listen_command()

    def listen_command(self):
        try:
            with sr.Microphone() as source:
                self.feedback_label.config(text="Ouvindo...")
                self.root.update()
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio, language="pt-BR").lower()
                self.feedback_label.config(text=f"Comando: {command}")
                self.execute_command(command)
        except sr.UnknownValueError:
            self.feedback_label.config(text="Não entendi. Repita, por favor.")
        except sr.RequestError:
            self.feedback_label.config(text="Erro no serviço de voz.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def execute_command(self, command):
        if "abrir chrome" in command:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "abrir google" in command:
            webbrowser.open("https://www.google.com")

        elif "abrir youtube" in command:
            webbrowser.open("https://youtube.com")
        
        elif "tocar" in command:
            music = command.replace("tocar", "").strip()
            pywhatkit.playonyt(music)
        
        elif "pesquise" in command:
            query = command.replace("Pesquisar", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "abrir bloco de notas" in command:
            os.system("notepad.exe")
         
        # elif "é hora de codar" in command: 
        #     self.feedback_label.config(text="Hora de codar! Vamos lá!")
        #     os.startfile("C:\Users\joaog\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")

        elif "abrir calculadora" in command:
            os.system("calc.exe")
        
        elif "Abra o Whatsapp" in command:
            webbrowser.open("https://web.whatsapp.com")

        elif "que horas são" in command:
            agora = datetime.now().strftime("%H:%M")
            self.feedback_label.config(text=f"Agora são {agora}")

        elif "sair" in command:
            self.root.quit()

        else:
            self.feedback_label.config(text="Comando não reconhecido.")

# Inicia a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()