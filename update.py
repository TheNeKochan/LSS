import socket, hashlib


allowcmd = ['hash', 'config', 'END']
srv = socket.socket()
srv.bind(("0.0.0.0", 8080))
srv.listen(100)

while True:
    client, _ = srv.accept()
    while 1:
        try:
            cmd = client.recv(10).decode()
            if cmd in allowcmd:
                cfg = open('config.json')
                if cmd == 'hash':
                    client.send(hashlib.md5(cfg.read().encode()).hexdigest().encode())
                    print("Client asked hash of config")
                elif cmd == 'config':
                    client.send(cfg.read().encode())
                    print("Client haven't new version of config, he asked for it")
                elif cmd == 'END':
                    print("Client have newest version of config")
            else:
                client.close()
        except:
            break
