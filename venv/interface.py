from tkinter import *
import banco

bd = banco.Banco()
class interface():

    def __init__(self):
        self.main()

    def atualizaList(self, lb):
        lb.delete(0, END)
        bd.executa("select * from clientes order by nome asc")
        resultSet = bd.cursor.fetchall()
        i = 1
        for results in resultSet:
            lb.insert(i, [results[0], results[1], results[2], results[3]])
            i += 1
    def clientes(self):

        janelaClientes = Tk()
        janelaClientes.geometry("900x700")
        janelaClientes.title("Cadastro de clientes")
        Label(janelaClientes, text="Cadastro:", font=('Arial', 18), fg="red").place(x=100, y=100)
        Label(janelaClientes, text="Nome: ").place(x=100, y= 150)
        edtNome = Entry(janelaClientes, width= 20)
        edtNome.place(x=100, y= 180)

        Label(janelaClientes, text="CPF: ").place(x=100, y=210)
        edtCPF = Entry(janelaClientes, width=20)
        edtCPF.place(x=100, y=240)

        Label(janelaClientes, text="Email: ").place(x=100, y=270)
        edtEmail = Entry(janelaClientes, width=20)
        edtEmail.place(x=100, y=300)

        Label(janelaClientes, text="Telefone: ").place(x=100, y=330)
        edtTelefone = Entry(janelaClientes, width=20)
        edtTelefone.place(x=100, y=360)
        Button(janelaClientes, text="Cadastrar", command= lambda: bd.insere(
            "clientes",
            "nome, cpf, email, telefone",
            "'"+edtNome.get()+"',"+
            "'"+edtCPF.get()+"',"+
            "'"+edtEmail.get()+"',"+
            "'"+edtTelefone.get()+"'"
                  )
               ).place(x= 100, y= 400)
        Label(janelaClientes, text="Clientes registrados: ").place(x=400, y=70)


        lb = Listbox(janelaClientes, width=70, height=30)
        lb.place(x= 400, y=100)
        self.atualizaList(lb)


        Button(janelaClientes, text="Excluir", command=lambda: bd.exluir("clientes", "WHERE cod = {}".format(lb.sele))



        
        


    def main(self):

        janela = Tk()
        janela.geometry("900x700")
        janela.title("Cadastros")
        Label(janela, text="Seja bem vindo!").place(x= 400, y= 100)

        Button(janela, text="Cadastro de clientes",
               command= lambda: self.clientes()
               ).place(x= 400, y=300)
        Button(janela, text="Cadastro de produtos",
               command=lambda: produtos()
               ).place(x= 400, y=330)







        janela.mainloop()


interface()
