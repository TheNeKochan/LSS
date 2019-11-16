import threading  # Библиотека потоков


class ThreadJob(threading.Thread):  # Класс обработки срабатываий таймера
    def __init__(self, callback, event, interval):
        self.callback = callback
        self.event = event
        self.interval = interval
        self.killed = False
        super(ThreadJob, self).__init__()

    def run(self):
        while (not self.event.wait(self.interval)) and (not self.killed):
            self.callback()

    def kill(self):
        self.killed = True


ids = {}  # Переменная для хранения его ID


def setinterval(callback, interval, id):  # Создание прерывания setinterval(функция исполняемая каждое срабатывание, t в мсек, id любое значение)
    if id not in ids.keys():
        ids[id] = ThreadJob(callback, threading.Event(), float(interval / 1000.0))
        ids[id].setDaemon(True)
        ids[id].start()
        return 0
    else:
        return 1


def delinterval(id):  # Функция удаления обработчика
    try:
        ids[id].kill()
        return 0
    except:
        return 1
