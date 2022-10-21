import http.server as http
import asyncio
import websockets
import socketserver
import sys
from datetime import datetime as dt
from loggerd import Logger

def server():
    loggr = Logger.Datalogger("server")
    server_address = ('0.0.0.0', 8000)
    if sys.version_info[1] < 7:
        class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.HTTPServer):
            pass
        httpd = ThreadingHTTPServer(server_address, http.SimpleHTTPRequestHandler)
    else:
        httpd = http.ThreadingHTTPServer(server_address, http.SimpleHTTPRequestHandler)
    loggr.LOG("Server started")
    httpd.serve_forever()

def socket(manager):
    loggr = Logger.Datalogger("socket")
    async def handler(websocket, path):
        loggr.LOG("Socket opened")
        try:
            while True:
                await asyncio.sleep(0.033) # 30 fps
                await websocket.send(manager[0].tobytes())
        except websockets.exceptions.ConnectionClosed:
            loggr.LOG("Socket closed")

    loggr.LOG("Starting socket handler")
    start_server = websockets.serve(ws_handler=handler, host='0.0.0.0', port=8585)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()