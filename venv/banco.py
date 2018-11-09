import pymysql

class Banco():

    def __init__(self):
        self.con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
        self.cursor = self.con.cursor()

    def insere(self,tabela, colunas, values):
        sql = "INSERT INTO "+tabela+" ("+colunas+") VALUES ("+values+")"
        self.executa(sql)

    def exclui(self, tabela, condicao):
        sql = "DELETE * from "+tabela+" "+condicao
        self.executa(sql)

    def atualiza(self, dia, disciplina, horario):
        sql = "UPDATE from "+dia+" set disciplina='"+disciplina+"', horario='"+horario+"'"
        self.executa(sql)

    def executa(self, sql):
        try:
            self.cursor.execute(sql)
            print("Deu")
            self.con.commit()

        except:
            print("Não deu")
            self.con.rollback()
            print()

        self.con.close()