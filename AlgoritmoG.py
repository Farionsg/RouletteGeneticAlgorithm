import random
import math


def funcionObjetivo(crom):
    return crom[0] + (2 * crom[1]) + (3 * crom[2]) + (4 * crom[3]) - 30

def generarPoblacion(numPoblacion, generacion):
    individuos = []
    for i in range(numPoblacion):
        individuos.append([random.randint(1, 30) , random.randint(1, 30), random.randint(1, 30), random.randint(1, 30)])
    seleccion(individuos, generacion)

def poblacionEjemplo():
    individuos = [[12, 5, 23, 8], [2, 21, 18, 3], [10, 4, 13, 14], [20, 1, 10, 6], [1, 4, 13, 19], [20, 5, 17, 1]]
    seleccion(individuos)


def seleccion(individuos, generacion):
    fitness = []
    fitnessTotal = 0
    probability = []
    cProbability = []
    acumulado = 0
    rangemm = []
    randomNumbers = []

    print("Individuos: ")
    print(*individuos, sep="\n")
    print()

    for i in range(len(individuos)):
        try:
            fitness.append( 1 / (1 + funcionObjetivo(individuos[i])))
            fitnessTotal += fitness[i]
        except:
            print("Division entre 0")

    for i in range(len(individuos)):
        try:
            probability.append( fitness[i] / fitnessTotal )
            acumulado += probability[i]
            cProbability.append(acumulado)
            randomNumbers.append(random.randint(0, 1000)/1000)
        except:
            print("Falla por no tener totalFitness")
    
    for i in range(len(randomNumbers)):
        for j in range(len(cProbability)):   
            if randomNumbers[i] < cProbability[0]:
                rangemm.append(individuos[0])
                break    
            try:
                if randomNumbers[i] > cProbability[j] and randomNumbers[i] < cProbability[j+1]:
                    rangemm.append(individuos[j+1])
                    break
            except:
                print("Falla al escoger individuos")
    
    mutacion(rangemm, generacion)


def mutacion(individuos, generacion):
    randomNumbers = []
    sCrossOver = []
    crossOverPoint = []
    indvMut = []
    indcMut = 0
    cTotal = 0
    numMutations = 0
    randomNumMutations = []

    print("Individuos seleccionados: ")
    print(*individuos, sep="\n")
    print()

    for i in range(len(individuos)):
        randomNumbers.append(random.randint(0, 1000)/1000)
        if randomNumbers[i] < 0.25:
            sCrossOver.append(i)
    random.shuffle(sCrossOver)
    for i in range(len(sCrossOver)):
       crossOverPoint.append(random.randint(1, len(sCrossOver)))
     
    for i in range(len(individuos)+1):
        try:
            mutacion = individuos[i-1]
        except:
            print("Falla por falta de individuos")
        if i in sCrossOver:
            for j in range(len(sCrossOver)):
                mutacionAux = individuos[sCrossOver[indcMut] - 1][:]
                indcMut += 1
                if j < crossOverPoint[indcMut-1]:                  
                    for k in range(crossOverPoint[indcMut-1]):
                        try:
                            mutacionAux[k] = mutacion[k]
                        except:
                            print("Falla por falta de individuos")
                    break
            indvMut.append(mutacionAux)
        else:
            try:
                indvMut.append(mutacion)
            except:
                print("Fin del Programa!")
    try:
        indvMut.pop(0)
    except:
        print("Lista vacia")                  

    for indv in indvMut:
        for n in indv:
            cTotal+=1
    
    #Mutation Rate 10%
    numMutations = math.floor(0.1 * cTotal)
    for i in range(numMutations):
        randomNumMutations.append([random.randint(0, len(individuos)-1), random.randint(0, len(individuos[i])-1)])

    print("Mutacion en los lugares: ")
    print(randomNumMutations)
    print()

    for i in range(numMutations):
        indvMut[randomNumMutations[i][0]][randomNumMutations[i][1]] = random.randint(0,30)
    print("Final de la generacion: ")
    print(*indvMut, sep="\n")
    print()
    print("Funcion objetivo f(x) = ((a + 2b + 3c + 4d) - 30)")
    for i in range(len(indvMut)):
        print(funcionObjetivo(indvMut[i]))
    print()
    generacion += 1
    print("Generacion Actual: ", generacion)
    opcion = True
    while opcion:
        print("Continuar con la siguiente generacion? (S/N)")
        resp = input()
        c = str.lower(resp[0])
        if c == 's':
            seleccion(indvMut, generacion)
            opcion = False
        elif c == 'n':
            break
        else:
            print("No se ingreso un valor valido, porfavor vuelva a intentar. (S/N)")
                    

def algoGenetico():
    programa = True
    opcion = True
    generacion = 0
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("             ___       __        _______   ______   .______      __  .___________.___  ___.   ______        _______.")
    print("            /   \     |  |      /  _____| /  __  \  |   _  \    |  | |           |   \/   |  /  __  \      /       |")
    print("           /  ^  \    |  |     |  |  __  |  |  |  | |  |_)  |   |  | `---|  |----|  \  /  | |  |  |  |    |   (----`")
    print("          /  /_\  \   |  |     |  | |_ | |  |  |  | |      /    |  |     |  |    |  |\/|  | |  |  |  |     \   \    ")
    print("         /  _____  \  |  `----.|  |__| | |  `--'  | |  |\  \----|  |     |  |    |  |  |  | |  `--'  | .----)   |   ")
    print("        /__/     \__\ |_______| \______|  \______/  | _| `._____|__|     |__|    |__|  |__|  \______/  |_______/    ")
    print("                                                                                                                      ")
    print("                _______  _______ .__   __.  _______ .___________.__    ______   ______        _______.")
    print("               /  _____||   ____||  \ |  | |   ____||           |  |  /      | /  __  \      /       |")
    print("              |  |  __  |  |__   |   \|  | |  |__   `---|  |----|  | |  ,----'|  |  |  |    |   (----`")
    print("              |  | |_ | |   __|  |  . `  | |   __|      |  |    |  | |  |     |  |  |  |     \   \    ")
    print("              |  |__| | |  |____ |  |\   | |  |____     |  |    |  | |  `----.|  `--'  | .----)   |   ")
    print("               \______| |_______||__| \__| |_______|    |__|    |__|  \______| \______/  |_______/    ")
    print("                                                                                                     ")
    print("-----------------------------------------------------------------------------------------------------------------------------")

    print("Bienvenidos a esta demostracion de un algoritmo genetico.")
    print("Esta aplicacion trata de demostrar el uso de la programacion para representar la evolucion de una poblacion.")
    print("Le gustaria iniciar con el programa?(S/N)")

    while opcion:
        resp = input()
        c = str.lower(resp[0])
        if c == 's':
            programa = True
            opcion = False
        elif c == 'n':
            programa = False
            opcion = False
        else:
            print("No se ingreso un valor valido, porfavor vuelva a intentar. (S/N)")

    while programa:
        print("Inserte el numero de pobladores que desea: ")
        numPoblacion = input()
        if numPoblacion.isnumeric():
            generarPoblacion(int(numPoblacion), generacion)
            programa = False
        else:
            print("No se ingreso un valor valido, porfavor vuelva a intentar.")

algoGenetico()