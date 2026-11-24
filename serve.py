"""Local-only static server. The browser performs all scenario and data calculations."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
if __name__ == '__main__':
    root=Path(__file__).resolve().parent
    print('Day One: http://127.0.0.1:8770',flush=True)
    ThreadingHTTPServer(('127.0.0.1',8770),partial(SimpleHTTPRequestHandler,directory=str(root))).serve_forever()
