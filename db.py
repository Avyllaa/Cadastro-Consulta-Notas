import psycopg2

class Database:
    def __init__(self):
        self.params = {
            'host': '127.0.0.1',
            'port': 5432,
            'database': 'Escola',
            'user': 'postgres',
            'password': '26042005'
        }
        self.conn = None
        self.cur = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(**self.params)
            self.cur = self.conn.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def adicionar_aluno(self, matricula, nome):
        self.connect()
        sql = "INSERT INTO public.alunos (matricula, nome) VALUES (%s, %s)"
        self.cur.execute(sql, (matricula, nome))
        self.conn.commit()

    def deletar_aluno(self, matricula):
        self.connect()
        sql = "DELETE FROM public.alunos WHERE matricula = %s"
        self.cur.execute(sql, (matricula,))
        self.conn.commit()

    def adicionar_nota(self, matricula, disciplina, nota):
        self.connect()
        sql = "INSERT INTO public.notas (matricula, disciplina, nota) VALUES (%s, %s, %s)"
        self.cur.execute(sql, (matricula, disciplina, nota))
        self.conn.commit()

    def atualizar_nota(self, matricula, disciplina, nova_nota):
        self.connect()
        sql = "UPDATE public.notas SET nota = %s WHERE matricula = %s AND disciplina = %s"
        self.cur.execute(sql, (nova_nota, matricula, disciplina))
        self.conn.commit()

    def deletar_nota(self, matricula, disciplina):
        self.connect()
        sql = "DELETE FROM public.notas WHERE matricula = %s AND disciplina = %s"
        self.cur.execute(sql, (matricula, disciplina))
        self.conn.commit()

    def consultar_notas(self, matricula):
        self.connect()
        sql = "SELECT disciplina, nota FROM public.notas WHERE matricula = %s"
        self.cur.execute(sql, (matricula,))
        return self.cur.fetchall()