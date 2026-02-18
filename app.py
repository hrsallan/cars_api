from flask import Flask, make_response, jsonify, request
from database import inicializar_banco, buscar_carros, buscar_carro_por_id, adicionar_carro, remover_carro

app = Flask(__name__)

# ------------------------------------------------------
# Inicializar Banco de Dados
# ------------------------------------------------------
try:
    inicializar_banco()
    print("Banco Iniciado! Sucesso!")
except Exception as error:
    print(f"Erro Encontrado! {error}")

# ------------------------------------------------------
# Rota para buscar carros
# ------------------------------------------------------
@app.route('/carros', methods=['GET'])
def get_carros():
    try:
        carros = buscar_carros()
        return make_response(jsonify(carros), 200)
    except Exception as error:
        return make_response(jsonify({"error": str(error)}), 500)

# ------------------------------------------------------
# Rota para buscar carro por ID
# ------------------------------------------------------
@app.route('/carros/<int:car_id>', methods=['GET'])
def get_carro_por_id(car_id):
    try:
        carro = buscar_carro_por_id(car_id)
        if carro:
            return make_response(jsonify(carro), 200)
        else:
            return make_response(jsonify({"error": "Carro não encontrado"}), 404)
    except Exception as error:
        return make_response(jsonify({"error": str(error)}), 500)
    
# ------------------------------------------------------
# Adicionar carro 
# ------------------------------------------------------
@app.route('/carros', methods=['POST'])
def add_carro():
    try:
        data = request.get_json()
        nome = data.get('nome')
        ano = data.get('ano')
        estilo = data.get('estilo')
        tracao = data.get('tracao')

        if not all([nome, ano, estilo, tracao]):
            return make_response(jsonify({"error": "Todos os campos são obrigatórios"}), 400)

        adicionar_carro(nome, ano, estilo, tracao)
        return make_response(jsonify({"message": "Carro adicionado com sucesso!"}), 201)
    except Exception as error:
        return make_response(jsonify({"error": str(error)}), 500)

# ------------------------------------------------------
# Remover Carro
# ------------------------------------------------------
@app.route('/carros/<int:car_id>', methods=['DELETE'])
def delete_carro(car_id):
    try:
        remover_carro(car_id)
        return make_response(jsonify({"message": "Carro removido com sucesso!"}), 200)
    except Exception as error:
        return make_response(jsonify({"error": str(error)}), 500)

if __name__ == '__main__':
    app.run(debug=True)