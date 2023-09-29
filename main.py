from api import bazaar_api
from data_manager import plot_graph
import threading
from time import sleep
import os

def update_data() -> None:
    api = bazaar_api()
    while True:
        api.update_data()
        sleep(60)
        
def runtime_status() -> None:
    # Running... animation
    while True:
        for i in range(4):
            print("Running" + "." * i)
            
            sleep(0.5)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

if __name__ == "__main__":
    thread_1 = threading.Thread(target=update_data)
    thread_2 = threading.Thread(target=runtime_status)
    thread_1.start()
    thread_2.start()
    
    plot_graph("ENCHANTED_BROWN_MUSHROOM")
    