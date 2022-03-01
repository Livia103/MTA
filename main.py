
import proxy_library
import sys
import logging
import socket
import socketserver




def create_file():
    F = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(format=F, filename='proxy-udp.log', level=logging.INFO, datefmt='%H:%M:%S')

    h_name = socket.gethostname()
    logging.info(h_name)

def ip_address():

    if len(sys.argv) > 1:
        ip = sys.argv[1]
        print("IP address:", ip)
    else:
        sys.exit()

    return ip


if __name__ == "__main__":

    create_file()
    ip = ip_address()

    proxy_library.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ip, proxy_library.PORT)
    proxy_library.topvia = "Via: SIP/2.0/UDP %s:%d" % (ip, proxy_library.PORT)
    server = socketserver.UDPServer((proxy_library.HOST, proxy_library.PORT), proxy_library.UDPHandler)
    server.serve_forever()

