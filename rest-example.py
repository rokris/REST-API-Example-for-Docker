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
This is what runs when the image is started (i.e. docker run).
# 
## Running In A Container
Running the ```docker run -p 8080:8080 rest-example``` command starts the image in a container. It code uses port 8080, and it is mapped to the local port 8080. Feel free to experiment with this. It will be attached to your command line; that is, it ties up your terminal while it’s running. You can eliminate this by using the --detach option in your command. In that case, the container runs in the background.

You can see the results of the code by running the curl command or opening your browser to http://localhost:8080.
#
## Test PUT
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Shovon", "balance": 100}' http://127.0.0.1:8080/account
```
