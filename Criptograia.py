from cryptography.fernet import Fernet
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class Cripto(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título
        titulo = Label(text="Criptografia de Arquivos", font_size=24, size_hint=(1, None), height=40)
        layout.add_widget(titulo)

        # Campo de entrada para o nome do arquivo
        self.nome_arquivo_input = TextInput(hint_text="Digite o nome do arquivo", multiline=False, size_hint=(1, None), height=30)
        layout.add_widget(self.nome_arquivo_input)

        # Botão para gerar a chave
        btn_gerar_chave = Button(text="Gerar Chave", size_hint=(1, None), height=40)
        btn_gerar_chave.bind(on_release=self.gerar_chave)
        layout.add_widget(btn_gerar_chave)

        # Botões para criptografar e descriptografar
        btn_criptografar = Button(text="Criptografar", size_hint=(1, None), height=40)
        btn_criptografar.bind(on_release=self.criptografar_arquivo)
        layout.add_widget(btn_criptografar)

        btn_descriptografar = Button(text="Descriptografar", size_hint=(1, None), height=40)
        btn_descriptografar.bind(on_release=self.descriptografar_arquivo)
        layout.add_widget(btn_descriptografar)

        # Label de status
        self.status_label = Label(text="", size_hint=(1, None), height=40)
        layout.add_widget(self.status_label)

        return layout


    def gerar_chave():
        try:
            chave = Fernet.generate_key()
            with open("chave.key", "wb") as chave_arquivo:
                chave_arquivo.write(chave)
            self.status_label.text = "Chave gerada e salva como 'chave.key'."
        except Exception as e:
            self.status_label.text = f"Erro ao gerar chave: {e}"

    def carregar_chave():
        try:
            return open("chave.key", "rb").read()
        except FileNotFoundError:
                self.status_label.text = "Chave não encontrada. Gere uma chave primeiro."
                return None
        except Exception as e:
                self.status_label.text = f"Erro ao carregar chave: {e}"
                return None

    def criptografar_arquivo(nome_arquivo):
        chave = carregar_chave()
        f = Fernet(chave)

        with open(nome_arquivo, "rb") as arquivo:
            dados = arquivo.read()

        dados_criptografados = f.encrypt(dados)

        with open(nome_arquivo, "wb") as arquivo:
            arquivo.write(dados_criptografados)

        print(f"{nome_arquivo} criptografado com sucesso.")

    def descriptografar_arquivo(self):
        nome_arquivo = self.ids.nome_arquivo_input.text
        if not os.path.exists(nome_arquivo):
            self.ids.status_label.text = "Arquivo não encontrado."
            return

        chave = self.carregar_chave()
        if chave is None:
            self.ids.status_label.text = "Erro ao carregar chave para descriptografar."
            return

    try:
        
        f = Fernet(chave)

        with open(nome_arquivo, "rb") as arquivo:
            dados_criptografados = arquivo.read()

        dados = f.decrypt(dados_criptografados)

        with open(nome_arquivo, "wb") as arquivo:
            arquivo.write(dados)

        self.ids.status_label.text = f"{nome_arquivo} descriptografado com sucesso."
    
    except Exception as e:
        self.ids.status_label.text = f"Erro ao descriptografar: {e}"

    def main():
        while True:
            acao1 = input("Aperte 4 para gerar uma chave ou Q para sair! ")
            
            if acao == '1':
                    nome_arquivo = self.nome_arquivo_input.text
                    if os.path.exists(nome_arquivo):
                        criptografar_arquivo(nome_arquivo)
                    else:
                        print("Arquivo não encontrado.")

            if acao1 == '4':
                gerar_chave()
                print("Chave gerada e salva como 'chave.key'.")
                confir = 1

            elif acao1 == 'q':
                break

            if confir >= 1:
                acao = input("Escolha uma ação: [1] Criptografar, [2] Descriptografar, [q] Sair: ")
      
            elif acao == '2':
                    nome_arquivo = input("Digite o nome do arquivo a ser descriptografado: ")
                    if os.path.exists(nome_arquivo):
                        descriptografar_arquivo(nome_arquivo)
                    else:
                        print("Arquivo não encontrado.")

            elif acao == 'q':
                break

            else:
                print("Ação inválida.")


    if __name__ == "__main__":
        main()


