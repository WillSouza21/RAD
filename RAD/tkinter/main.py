import tkinter as tk
import modelo as crud
from tkinter import ttk

class PrincipalBD():
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.janela = win

        self.treeProdutos = ttk.Treeview(self.janela, columns=("Código do produto", "Nome", "Preço"), show="headings")

        self.treeProdutos.heading("Código do produto", text= "Código do produto:")
        self.treeProdutos.heading("Nome", text= "Nome")
        self.treeProdutos.heading("Preço", text= "Preço")
        self.treeProdutos.pack()

        self.lblNome= tk.Label(self.janela, text="Nome:")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblPreço= tk.Label(self.janela, text="Preço:")
        self.lblPreço.pack()
        self.entryPreço = tk.Entry(self.janela)
        self.entryPreço.pack()

        self.btnCadastrar = tk.Button(self.janela, text="Adicionar produtos", command=self.CadastrarProduto)
        self.entryPreço.pack()

    def CadastrarProduto(self):
        try:
            name = self.entryNome.get()
            price = float(self.entryPreco.get())
            self.objBD.inserirDados(name, price)

            self.entryNome.delete(0,tk.END)
            self.entryPreço.delete(0,tk.END)
        except:
            print("Não foi possível fazer o cadastro")


janela = tk.Tk()
product_app = PrincipalBD(janela)
janela.title("Bem vindo a aplicação de banco de dados")
janela.configure(bg='darkseagreen1')
janela.geometry("900x700")
janela.mainloop()