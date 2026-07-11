from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/buscar', methods=['GET'])
def analisar_mensagem():
    mensagem = request.args.get('mensagem')
    if not mensagem:
        return jsonify({'error': 'Parâmetro "mensagem" é obrigatório.'}), 400

    resultado = {
        'mensagem': mensagem,
        'analise': 'Esta é uma análise fictícia da mensagem.'
    }

    return jsonify(resultado)

@app.route('/enviar', methods=['POST'])
def enviar_mensagem():
    data = request.get_json()
    if not data or 'mensagem' not in data:
        return jsonify({'error': 'Corpo da requisição deve conter o campo "mensagem".'}), 400

    mensagem = data['mensagem']
    resultado = {
        'mensagem': mensagem,
        'status': 'Mensagem recebida com sucesso.'
    }
    return jsonify(resultado), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Servidor está funcionando corretamente.'}), 200


if __name__ == '__main__':
    app.run(debug=True)