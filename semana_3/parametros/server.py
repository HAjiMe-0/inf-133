from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Manejo de parámetros de consulta "query parameters" en la URL
from urllib.parse import urlparse, parse_qs, parse_gs
estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]

def do_GET(self):
    parsed_path = urlparse(self.path)
    query_params = parse_qs(parsed_path.query)

    if parsed_path.path == "/estudiantes":
        if "nombre" in query_params:
            nombre = query_params["nombre"][0]
            estudiantes_filtrados = [
                estudiante
                for estudiante in estudiantes
                if estudiante["nombre"] == nombre
            ]
            if estudiantes_filtrados != []:
                self.response_handler(200, estudiantes_filtrados)
            else:
                self.response_handler(204, [])
        else:
            self.response_handler(200, estudiantes)