# Importação das bibliotecas necessárias para a aplicação
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS  # Importação do middleware para permitir solicitações de origens diferentes
import re  # Importação do módulo de expressões regulares para manipulação de texto
from unidecode import unidecode  # Importação para remover acentos
from flask import Flask, request, jsonify
import requests
import json
import os
# Criação de uma instância do aplicativo Flask
app = Flask(__name__)
CORS(app)  # Aplicação do middleware CORS para permitir solicitações de origens diferentes

# Carrega os dados do arquivo JSON
with open('static/responses.json', 'r', encoding='utf-8') as file:
    responses = json.load(file)

with open('static/clubes.json', 'r', encoding='utf-8') as file:
    clubes_data = json.load(file)

@app.route('/posicoes', methods=['GET'])
def get_posicoes():
    try:
        with open('static/posicoes.json', 'r', encoding='utf-8') as file:
            posicoes = json.load(file)
        return jsonify(posicoes)
    except FileNotFoundError:
        return jsonify({'error': 'O arquivo posicoes.json não foi encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao processar a requisição: {str(e)}'}), 500
    
@app.route('/clubes', methods=['GET'])
def obter_clubes():
    return jsonify(clubes_data)

@app.route("/")
def index():
    # Adicionando a configuração de Content Security Policy
    response = app.response_class(
        response=render_template("index.html"),
        status=200,
        mimetype='text/html'
    )
    response.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-inline' 'unsafe-eval';"
    return response

with open('static/campeoes.json', 'r', encoding='utf-8') as file:
    campeoes_data = json.load(file)
    
@app.route('/get_campeoes/<int:ano>', methods=['GET'])
def get_campeoes(ano):
    if str(ano) in campeoes_data:
        return jsonify(campeoes_data[str(ano)])
    else:
        return jsonify({"error": f"Nenhum campeão encontrado para o ano {ano}"}), 404
    
with open('static/maiorCampeao.json', 'r', encoding='utf-8') as file:
    maiorCampeao_data = json.load(file)
    
@app.route('/get_maior_campeao', methods=['GET'])
def get_maiorCampeao():
    try:
        return jsonify(maiorCampeao_data)
    except Exception as e:
        return jsonify({"error": f"Falha na busca dos maiores campeões: {str(e)}"}), 500
    
    
@app.route("/obter_dados_api", methods=["GET"])
def obter_dados_api():
    try:
        # Primeiro, obtenha o status do mercado para descobrir a rodada atual
        status_url = 'https://api.cartola.globo.com/mercado/status'
        status_response = requests.get(status_url)

        if status_response.status_code != 200:
            return jsonify({"error": "Falha ao obter o status do mercado do Cartola"}, 500)

        status_data = status_response.json()
        current_round = status_data.get('rodada_atual')

        if not current_round:
            return jsonify({"error": "Não foi possível determinar a rodada atual do Cartola"}, 500)

        # Agora, busque os atletas pontuados da rodada atual
        pontuados_url = f'https://api.cartola.globo.com/atletas/pontuados/{current_round}'
        response = requests.get(pontuados_url)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": f"A solicitação à API de pontuados para a rodada {current_round} falhou"}, 500)

    except Exception as e:
        return jsonify({"error": str(e)}, 500)
   
@app.route("/pesquisar_atletas/<nome>", methods=["GET"])
def pesquisar_atletas(nome):
    try:
        # Faça uma solicitação à API externa para obter a lista de atletas
        url = 'https://api.cartola.globo.com/atletas/mercado'
        response = requests.get(url)

        if response.status_code == 200:
            # A solicitação à API externa foi bem-sucedida
            data = response.json()

            # Filtrar os atletas cujo nome contenha o valor fornecido
            atletas_encontrados = [atleta for atleta in data['atletas'] if nome.lower() in atleta['apelido'].lower()]

            return jsonify(atletas_encontrados)
        else:
            # A solicitação à API externa falhou
            return jsonify({"error": "A solicitação à API falhou"}, 500)  # Resposta de erro com código 500
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer
        return jsonify({"error": str(e)}, 500)


@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("user_message")

    # Normalize the user's message
    normalized_user_message = unidecode(re.sub(r'[^\w\s]', '', user_message)).lower()

    # Create a lookup dictionary with normalized keys
    normalized_responses = {unidecode(re.sub(r'[^\w\s]', '', k)).lower(): v for k, v in responses.items()}

    # Find the response
    bot_response = normalized_responses.get(normalized_user_message, "Desculpe! Não consegui compreender sua mensagem, pode repetir?")

    return jsonify({"bot_response": bot_response})


# Rota para servir arquivos estáticos (por exemplo, CSS e JavaScript)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Execução do aplicativo se este arquivo for o ponto de entrada
if __name__ == "__main__":
    app.run(debug=True)