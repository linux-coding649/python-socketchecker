import socket

print('Welcome to SocketTester!')
print('If you want to exit, type \'exit\' when prompted.')

while True:
    stt = input('Socket / Port to test: ')
    if stt == 'exit':
        exit()
    try:
        stt = int(stt)
    except ValueError:
        print('Unknown Port Number / Input is not a number.')
        continue
    print('Trying Port TCP/'+str(stt))
    tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tsock.bind(('0.0.0.0', stt))
        ngood = False
    except OSError:
        print('Port: TCP/'+str(stt)+', Socket is in use, or Socket Binding [ERRNO 13: Permission Denied]')
        ngood = True
    except OverflowError:
        print('Port: TCP/'+str(stt)+', not a port, requested port is not in the 0 - 65535 range.')
        ngood = True
    if not ngood:
        print('Port: TCP/'+str(stt)+', Socket is not used.')
    tsock.close()
    print('Trying UDP/'+str(stt))
    usock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        usock.bind(('0.0.0.0', stt))
    except OSError:
        print('Port: UDP/'+str(stt)+', Socket is in use, or Socket Binding [ERRNO 13: Permission Denied]')
        usock.close()
        continue
    except OverflowError:
        print('Port: UDP/'+str(stt)+', not a port, requested port is not in the 0 - 65535 range.')
        usock.close()
        continue
    print('Port: UDP/'+str(stt)+', Socket is not used.')
    usock.close()
