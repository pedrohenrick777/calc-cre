import time
import os

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def calc_cre(grade, workload):
    chN = 0
    chT = 0
    for i in range(len(grade)):
        chN += grade[i] * workload[i]
        chT += workload[i]

    cre = chN/chT

    return cre

def __init__():

    grades = []
    workloads = []
    while True:
        clean_screen() 
        grade = input('Informe a média da matéria(Fim para encerrar): ')

        if grade.upper() == 'FIM':
            break

        workload = input('Informe a carga horária: ')

        grades.append(int(grade))
        workloads.append(int(workload))

    cre = calc_cre(grades, workloads)
    clean_screen()
    print(f'Seu CRE é: {cre}')
    time.sleep(5)
    repeat = input('Deseja calcular novamente? (S/N) ').upper

    if repeat == 'S':
        __init__()

clean_screen()
print('''
Para calcular o seu CRE, você deve informar a carga horária e média de cada matéria.

Asssim, vai ser feito o calculo a seguir:

CRE = (N1 * H1 + N2 * H2 ...)/(H1 * H2...)

onde:

H = Carga horária
N = Nota

Aperte ENTER para calcular seu CRE.
''')

input()
__init__()