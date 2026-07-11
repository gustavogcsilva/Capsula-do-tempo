import pytest
import requests

BASE_URL = "http://localhost:5000"
mensagens = []

def test_post_mensagem():
    new_mensage = {"mensagem": "Olá, esse é seu primeiro teste!"}
    response = requests.post(f"{BASE_URL}/enviar", json=new_mensage)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['mensagem'] == new_mensage['mensagem']
    assert response_json['status'] == 'Mensagem recebida com sucesso.'

