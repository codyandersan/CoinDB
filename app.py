from flask import jsonify, Flask, request

from manage_coins import add_coin, get_coins, delete_coin

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/add_coin', methods=['POST'])
def add_coin_route():
    data = request.get_json()
    title = data.get('title')
    dateOfMinting = data.get('dateOfMinting')
    remarks = data.get('remarks')
    
    resp = add_coin(title, dateOfMinting, remarks)

    return jsonify(resp)


@app.route('/get_coins')
def get_coins_route():  

    resp = get_coins()
    return jsonify(resp)
  


@app.route('/delete_coin')
def delete_coin_route():
    objectId = request.args.get('objectId')
    resp = delete_coin(objectId)
    return jsonify(resp)
  


if __name__ == '__main__':
    app.run(debug=True)


