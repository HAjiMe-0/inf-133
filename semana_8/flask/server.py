# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)


# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1=int(request.args.get("num1"))
    num2=int(request.args.get("num2"))
    if not num1 and num2:
        return (
            jsonify({"error": "Se requiere los numeros en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡La suma es = {num1+num2}!"})

@app.route("/palindromo", methods=["GET"])
def palindromo():
    palabra=request.args.get("palabra")
    if not palabra:
        return (
            jsonify({"error": "Se requiere la palabra en los parámetros de la URL."}),
            400,
        )
    if palabra==palabra[::-1]:
        return jsonify({"mensaje": f"¡La palabra {palabra} es palindromo!"})
    else:
        return jsonify({"mensaje": f"¡La palabra {palabra} no es palindromo!"})
    
@app.route("/vocal", methods=["GET"])
def vocal():
    palabra=request.args.get("palabra")
    if not palabra:
        return (
            jsonify({"error": "Se requiere la palabra en los parámetros de la URL."}),
            400,
        )
    if palabra.isalpha():
        return jsonify({"mensaje": f"¡La palabra {palabra} es vocal!"})
    else:
        return jsonify({"mensaje": f"¡La palabra {palabra} no es vocal!"})

# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":    
    app.run()
    