import socket
import signal
import sys
#import datetime
import struct
import psutil
#import time
from time import sleep

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_addr, tcp_port))

if __name__ == '__main__':

#order = 0

    while True:
        try: 
            #order == 1
            sleep(2.0)

            #Total de CPU que está em uso
            cpu = psutil.cpu_percent()
            print('CPU Utilization: {}%'.format(cpu))

            #Total de percentagem de memória que está em uso
            memory = psutil.virtual_memory().percent
            print('Percentage of Memory in Usage: {}%\n'.format(memory))

            #packet com a estrutura
            pkt = struct.pack('ff', cpu, memory)
            #enviar a estrutura
            sock.send(pkt)


        except (socket.timeout, socket.error):
            print('Server error. Done!')
            sys.exit(0)


