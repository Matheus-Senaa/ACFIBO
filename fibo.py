import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fib(quant):
    seq = [0, 1]
    while len(seq) < quant:
        seq.append(seq[-1] + seq[-2])
    return seq

seq = fib(100)
print(seq)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
