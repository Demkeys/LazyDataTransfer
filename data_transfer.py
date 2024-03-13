# Description: Lazy script to send/recv upto 64kb of data
# over the network using UDP. This is script doesn't have
# any validation logic so make sure you are providing the
# arguments properly, otherwise the behaviour is undefined.
# This is a very lazy method and should only be used if 
#
# In 'send' mode ip address must be address of target 
# machine. In 'recv' mode the ip address must be address
# of host machine.
#
# Usage:
# Arg 1: mode
# Arg 2: file name
# Arg 3: address (ip address:port)
#
# Example: 
# python data_transfer.py send text01.txt 192.168.8.103:9510
import socket
import sys

if __name__ == '__main__':
    print('Starting program...')
    addr = sys.argv[3].split(':')
    ip = addr[0]
    port = int(addr[1])
    mode = sys.argv[1]
    file_name = sys.argv[2]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if mode == 'send':
        print('Starting sending...')
        with open(file_name, 'rb') as f:
            data = f.read()
            sent_len = sock.sendto(data,(ip,port))
            print(f'{sent_len} bytes read and sent.')
    elif mode == 'recv':
        sock.bind((ip,port))
        print(f'Socket bound to {ip}:{port}.')
        print('Starting receiving...')
        data, recv_addr = sock.recvfrom(65535)
        with open(file_name, 'wb+') as f:
            f.write(data)
            print(f'{len(data)} bytes received and written to file.')
    sock.close()
    print('Ending program')
