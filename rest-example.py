from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = [
        {'name': "Roger", 'balance': 500},
        {'name': "Hanne Lene", 'balance': 650},
        {'name': "Jeanette", 'balance': 200}
    ]

@app.route("/")
def helloworld():
    return "<a href='/accounts'>You will find the API example at this URL /accounts</a>"

@app.route("/accounts", methods=["GET"])
def getAccounts():
    return jsonify(accounts)

@app.route("/account/<id>", methods=["GET"])
def getAccount(id):
    id = int(id) -1
    return jsonify(accounts[id])

@app.route("/account", methods=["POST"])
def addAccount():
    name = request.json['name']
    balance = request.json['balance']
    data = {'name': name, 'balance': balance}
    accounts.append(data)

    return jsonify(data)

if __name__ == '__main__':
    app.run('0.0.0.0','8080')
