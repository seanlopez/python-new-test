import LC_client_app
import threading,time


client_app = LC_client_app.client_app()

t1 = threading.Thread(target=client_app.run)
t2 = threading.Thread(target=client_app.rece_)


t1.start()
t2.start()
