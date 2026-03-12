import http.server, socketserver

PORT = 5173
DIR  = "/Users/marie/Desktop/Projet Quizz des Camilles"

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)
    def log_message(self, *a): pass  # suppress noisy logs

with socketserver.TCPServer(("", PORT), H) as s:
    s.serve_forever()
