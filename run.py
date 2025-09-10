import os
import threading
import subprocess
from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Esta função responde ao Render para mostrar que estamos vivos."""
    return 'ModMail bot is running!'

def run_flask():
    """Esta função inicia o servidor web."""
    # O Render fornece a porta na variável de ambiente PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def run_modmail():
    """Esta função inicia o ModMail."""
    # Usamos subprocess para rodar o comando `python -m modmail`
    subprocess.run(["python", "-m", "modmail"])

if __name__ == '__main__':
    # Criamos "threads" para rodar ambos os processos simultaneamente
    flask_thread = threading.Thread(target=run_flask)
    modmail_thread = threading.Thread(target=run_modmail)

    print("Iniciando servidor web do Flask...")
    flask_thread.start()
    
    print("Iniciando o ModMail...")
    modmail_thread.start()

    flask_thread.join()
    modmail_thread.join()
