from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello():
    """
    Un simple saludo
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: El nombre de la persona a saludar
    responses:
      200:
        description: Saludo exitoso
        examples:
          message: "Hola, Mundo!"
    """
    name = request.args.get('name', 'Mundo')
    return jsonify(message=f"Hola, {name}!")

if __name__ == '__main__':
    app.run(debug=True)
