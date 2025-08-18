import threading
import os

def show_thread_info():
    # se crea un hilo del SO por cada nuevo threading.Thread, esto corre un mismo Process ID
    # el so intercala y distribuye el proceso en los hilos o cores fisicos
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Process ID: {os.getpid()}")

# Puedes crear más hilos del SO que núcleos físicos
threads = []
for i in range(2):  # 100 hilos del SO
    thread = threading.Thread(target=show_thread_info)
    threads.append(thread)
    thread.start()