#Declaracion de librerias

import pandas as pd

#Importacion de los archivos

quiz1 = pd.read_csv("quiz_1.csv")
quiz2 = pd.read_csv("quiz_2.csv")
quiz3 = pd.read_csv("quiz_3.csv")
quiz4 = pd.read_csv("quiz_4.csv")
quiz5 = pd.read_csv("quiz_5.csv")
#Unificacion de lo 5 archivos
data_quiz = pd.concat(map(pd.read_csv, [quiz1, quiz2, quiz3, quiz4, quiz5]))


#Convertir a diccionario data_quiz a tipo list
class quizes:

    def __init__(self, data):
        self.quiz = data.values.tolist()


datos = quizes(data_quiz)

#print(datos.quiz)


#unificacion y eliminacion de repetidos con sumas de los totales
class quiz_app:

    def __init__(self, data):
        new_diccionario = {}
        pc = {}
        for i in data:

            r = i[4].split()
            p = int(r[0])
            if i[2] in new_diccionario.keys():
                new_diccionario[i[2]] += i[5]
                pc[i[2]] += p
            else:
                new_diccionario[i[2]] = i[5]
                pc[i[2]] = p

        self.pcj = pc
        self.dataQuiz = new_diccionario


respuesta = quiz_app(datos.quiz)

#print(respuesta.pcj)


#Class ganador
class ganador:

    def __init__(self, datos, d):
        #muestra los jugadores que tuvieron un porcentaje mayor de 70.0 % de Accuracy
        print('JUGADORES CON MAS DE 70% DE ACCURACY')
        for r in datos.keys():
            res = d[r] / 5
            if res > 70.0:
                print(r, res, '%')
        print('')
        print('')
        max_value = None
        #muestra el ganador con mayor puntaje de Score
        print('JUGADOR GANADOR')
        for t in datos.keys():
            res = datos[t]
            if (max_value is None or res > max_value):
                max_value = res

        print('ganador con: ', max_value, 'es : ', t)


ganador1 = ganador(respuesta.dataQuiz, respuesta.pcj)