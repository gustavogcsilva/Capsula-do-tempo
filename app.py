from flask import Flask, jsonify, request

app = Flask(__name__)

dados_capsulas = []

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

    nova_capsula = {
        'id': len(dados_capsulas) + 1,
        'mensagem': data['mensagem'],
        'destino': data['data_gatilho'],
        'status': 'pendente'
    }
    dados_capsulas.append(nova_capsula)
    return jsonify({
        'mensagem': nova_capsula['mensagem'],
        'status': 'mensagem recebida com sucesso.',
        'id_capsula': nova_capsula['id']
    })


@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(dados_capsulas), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Servidor está funcionando corretamente.'}), 200


if __name__ == '__main__':
    app.run(debug=True)