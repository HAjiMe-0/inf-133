from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return ", ()!", format(nombre)
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="https://localhost:8000/",
    action="https://localhost:8000/",
    namespace="https://localhost:8000/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "saludar",
    saludar,
    returns=("saludo":str),
    args=("nombre":str),
)
server = HTTPServer(("0,0,0,0", 8000),SOAPHandler)
server.dispatcher= dispatcher
print("servidor SOAP iniciado en https://localhost:8000/")
server.serve_forever()