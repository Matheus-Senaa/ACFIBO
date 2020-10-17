import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    anterior = 0
    proxima = 1
    soma = 1

    for n in range (0, 101):
        print(anterior)
        soma = proxima + anterior
        anterior = proxima
        proxima = soma
    
     return anterior

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
