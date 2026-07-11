import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_post_mensagem():
    # Incluí os campos que o Flask precisa para a cápsula do tempo
    new_message = {
        "mensagem": "Olá, esse é seu primeiro teste!",
        "destinatario": "gustavo@email.com",
        "data_gatilho": "2026-12-31"
    }
    response = requests.post(f"{BASE_URL}/enviar", json=new_message)
    assert response.status_code == 200
    
    response_json = response.json()
    # Verifica se o ID foi gerado (como um número inteiro)
    assert isinstance(response_json['id_capsula'], int)
    assert response_json['mensagem'] == new_message['mensagem']
    assert response_json['status'].lower() == 'mensagem recebida com sucesso.'

def test_get_mensagem():
    texto_mensagem = "Olá, esse é seu primeiro teste!"
    # Corrigido para passar a variável string correta
    response = requests.get(f"{BASE_URL}/buscar", params={"mensagem": texto_mensagem})
    assert response.status_code == 200
    
    response_json = response.json()
    assert response_json['mensagem'] == texto_mensagem
    assert 'analise' in response_json  # Rota /buscar do seu Flask retorna 'analise'

def test_get_status():
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    response_json = response.json()
    # Ajustado para bater exatamente com a frase que está no seu app.py original
    assert response_json['status'] == 'Servidor está funcionando corretamente.'

# Adicionado o 'test_' no início para o pytest coletar esta função
def test_listar_mensagens():
    response = requests.get(f"{BASE_URL}/mensagens")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)