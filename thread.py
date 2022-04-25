import threading
import time
N = 10
T = 60
def funcao():
    for i in range(N):
        print(i,"Execução")
        
    time.sleep(1)
        


print("Inicio")
for i in range(T):
    print(i)
    threading.Thread(target=funcao).start()
    
print("Fim")