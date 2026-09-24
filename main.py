import time
from valores import *
from metodosSimulador import *
step_count = 0
listaEdificios = []

def step(seconds = 3):
    global step_count, listaEdificios
    #construir
    edificio = input("Escribe lo que quieres construír, sin tildes: ")
    #comprobamos si se puede
    if comprobarDependencia(edificio, DEPENDENCIAS, listaEdificios):
        listaEdificios.append(edificio)
    else:
        print(f"no se pudo construir {edificio}")
    print(f"edificios actuales: {listaEdificios}")
    time.sleep(3)
    step_count += 1
    print(f"Step: {step_count}, cada step toma {seconds} segs")

while step_count <= 1000:
    step()