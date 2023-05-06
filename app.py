
import threading
import time


def contagem():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)


def mensagem():
    for i in range(5):
        print("Olá, mundo!")
        time.sleep(2)


t1 = threading.Thread(target=contagem)
t2 = threading.Thread(target=mensagem)

t1.start()
t2.start()

t1.join()
t2.join()

print("Todas as tarefas foram concluídas!")
