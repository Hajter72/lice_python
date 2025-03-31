from flask import Flask, jsonify
import random

app = Flask(__name__)

# Lista przykładowych cytatów
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Hardships often prepare ordinary people for an extraordinary destiny."
]

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
