from http.server import HTTPServer, BaseHTTPRequestHandler
import json
estuduante =[
    {
        "id":1,
        "nombre":"",
        "apellido":"",
        "carrera":
    }
]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiante':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estuduante).encode('utf-8'))