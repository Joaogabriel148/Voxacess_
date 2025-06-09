<h1 align="center"> VoxAcess</h1>

## :memo: Descrição
Projeto criado para a matéria de Tópicos integradores em C.C

## :books: Contextualização
* <b>Contextualização </b>: A aplicação em si e um assistente virtual que tem como funcionalidades: abrir aplicativos, fazer pesquisas e etc.

## :wrench: Tecnologias utilizadas
* Python
* Tkinter

## : Interface Gráfica
<img src='img\Captura de tela 2025-06-08 193853.png'>

## :game_die: Etapa Das Análises
- interface gráfica
  - Interface gráfica criada a partir de uma biblioteca do python chamada de Tkinter
  
```python
    self.root = root
            self.root.title("VoxAcess")
            self.root.geometry("300x500")
            self.root.configure(bg="#1e1e1e")
            self.root.resizable(False, False)
            self.root.iconbitmap(r"C:\\Faculdade\\7 Periodo\\VoxAcess\\img\\VoxAcessimg.ico")

            pygame.mixer.init()
            self.recognizer = sr.Recognizer()
             
            # Campo superior com botão de configuração
            self.top_frame = tk.Frame(root, bg="#1e1e1e")
            self.top_frame.pack(fill="x", padx=10, pady=(10, 0))
    ...
    ...
```

- Logica do Microfone
  - analiza se o comando por voz e valido e o manda para a outra etapa
  
```python
  def listen_command(self):
        try:
            with sr.Microphone() as source:
                self.feedback_label.config(text="🎧 Ouvindo...")
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
```
- Execução de comandos
  - O que faz: Verifica qual comando foi acionado e age de acordo com o comando
  
```python
  def execute_command(self, command):
        if "abrir chrome" in command:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "abrir google" in command:
            webbrowser.open("https://www.google.com")

        elif "abrir youtube" in command:
            webbrowser.open("https://youtube.com")
        ...
        ...
```
## Lista de comandos
* abrir chrome
* abrir google
* abrir youtube
* tocar
* pesquise
* abrir bloco de notas
* é hora de codar
* abrir calculadora
* Abra o Whatsapp
* que horas são
* sair


## :handshake: Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Joaogabriel148">
        <sub>
          <b>Joaogabriel148</b>
        </sub>
      </a>
    </td>
  </tr>
</table>