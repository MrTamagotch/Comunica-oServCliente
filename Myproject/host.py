from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        return jsonify({"message": "Requisição GET recebida!"})
    
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": "Requisição POST recebida!", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
