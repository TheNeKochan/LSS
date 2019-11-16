import threading
import socket


nc = socket.socket()


class CONTROL(threading.Thread):
    def __init__(self):
        self.state = []
        self.state.append(0)
        self.state.append(0)
        super(CONTROL, self).__init__()

    def run(self):
        nc.bind(("127.0.0.1", 45001))
        nc.listen(1)
        while True:
            conn, addr = nc.accept()
            try:
                conn.send(bytearray(self.state))
            except:
                pass
            else:
                conn.close()

    def setstate(self, state):
        self.state[1] = int(state)
