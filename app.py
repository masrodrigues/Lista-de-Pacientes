from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__)

#conexão com banco de dados

conn = sqlite3.connect("gestao_pacientes.db")
cursor = conn.cursor()

# Criação de tabelas se não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idades INTEGER,
        sexo TEXT,
        cpf TEXT UNIQUE,
        endereco TEXT,
        telefone TEXT
        )
               ''')
conn.commit()
conn.close()

@app.route('/')
def index():
        conn = sqlite3.connect("gestao_pacientes.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pacientes')
        pacientes = cursor.fetchall()
        conn.close()
        return render_template('index.html', pacientes=pacientes)
    
@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form == ['nome']
        idade = request.form == ['idade']
        sexo = request.form == ['sexo']
        cpf = request.form == ['cpf']
        endereco = request.form == ['endereco']
        telefone = request.form == ['telefone']
        
        conn = sqlite3.connect('gestao_pacientes.db')
        cursor = conn.cursor()
        cursor.execute('''
                        INSERT INTO pacientes (
                        VALUES(?, ?, ?, ?, ?, ?)
                       ''',(nome,idade, nome, cpf, endereco, telefone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('novo_paciente.html')

@app.route('/limpar_pacientes')
def limpar_pacientes():
    conn = sqlite3.connect('gestao_pacientes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pacientes')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)