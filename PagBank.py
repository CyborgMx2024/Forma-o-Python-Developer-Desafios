import tkinter as tk
from tkinter import messagebox, simpledialog

class PagBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PagBank App")
        
        # Variáveis de controle
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

        # Criação da interface
        self.create_widgets()

    def create_widgets(self):
        # Criação dos botões de operação
        self.label = tk.Label(self.root, text="Escolha uma opção:", font=("Helvetica", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.depositar_btn = tk.Button(self.root, text="Depositar", command=self.depositar)
        self.depositar_btn.grid(row=1, column=0, padx=20, pady=10)

        self.sacar_btn = tk.Button(self.root, text="Sacar", command=self.sacar)
        self.sacar_btn.grid(row=1, column=1, padx=20, pady=10)

        self.extrato_btn = tk.Button(self.root, text="Extrato", command=self.extrato_func)
        self.extrato_btn.grid(row=2, column=0, padx=20, pady=10)

        self.sair_btn = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.sair_btn.grid(row=2, column=1, padx=20, pady=10)

        self.resultado = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.resultado.grid(row=3, column=0, columnspan=2, pady=10)

    def depositar(self):
        valor = self.get_valor("Depositar")
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            self.resultado.config(text=f"Depósito realizado: R$ {valor:.2f}")
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

    def sacar(self):
        valor = self.get_valor("Sacar")
        if valor > self.saldo:
            messagebox.showerror("Erro", "Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite:
            messagebox.showerror("Erro", "Operação falhou! O valor do saque excede o limite.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            messagebox.showerror("Erro", "Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            self.resultado.config(text=f"Saque realizado: R$ {valor:.2f}")
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

    def extrato_func(self):
        extrato_texto = "Não foram realizadas movimentações." if not self.extrato else self.extrato
        messagebox.showinfo("Extrato", f"{extrato_texto}\n\nSaldo: R$ {self.saldo:.2f}")

    def get_valor(self, operacao):
        valor_str = simpledialog.askstring("Valor", f"Insira o valor que deseja {operacao.lower()}:")
        try:
            valor = float(valor_str)
            return valor
        except (ValueError, TypeError):
            return -1

if __name__ == "__main__":
    root = tk.Tk()
    app = PagBankApp(root)
    root.mainloop()
