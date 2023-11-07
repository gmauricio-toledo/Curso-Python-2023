import numpy as np
import matplotlib.pyplot as plt

def graficar(f,a,b,num=100):
    eje_x = np.linspace(start=a,
                    stop=b,
                    num=num)
    eje_y = [f(x) for x in eje_x]  # Listas de compresión
    plt.figure(figsize=(7,5))
    plt.plot(eje_x,eje_y,color='red')
    plt.axhline(0,color='gray') # Dibujar eje X
    plt.show()

def error_relativo(real, aproximacion):
    return np.abs((real-aproximacion)/real)
    
def falsa_posicion(f,xl,xu,tolerancia):
    '''
    f:      función
    xl:     extremo inferior del intervalo
    xu:     extremo superior del intervalo
    tol:    tolerancia
    '''
    x_m = xl
    error = 2*tolerancia
    errores = []
    aproximaciones = []
    n_iteraciones = 0
    while (error>tolerancia):
        n_iteraciones += 1
        x_m_anterior = x_m # aproximación anterior
        x_m = xu - (f(xu)*(xl-xu))/(f(xl)-f(xu))
        aproximaciones.append(x_m)
        if x_m != 0:
            error = error_relativo(x_m,x_m_anterior)
            errores.append(error)
        test = f(xl)*f(x_m)
        if test<0:
            xu = x_m
        elif test>0:
            xl = x_m
        else:
            error = 0
    return {'raiz': x_m,
            'error': error,
            'iteraciones': n_iteraciones,
            'errores': np.array(errores),
            'aproximaciones': np.array(aproximaciones)
            }

def secante(f,x0,x1,tolerancia):
    '''
    f:      función a la que encontraremos la raiz
    x0:     primera aproximación de la raiz
    x1:     segunda aproximación de la raiz
    tol:    tolerancia
    '''
    error = 2*tolerancia
    n_iteraciones = 0
    errores = []
    aproximaciones = []
    while (error>tolerancia):
        x_next = x1 - f(x1)*(x0-x1)/(f(x0)-f(x1))
        aproximaciones.append(x_next)
        if x1 != 0:
            error = error_relativo(x_next,x1)
            errores.append(error)
        x0 = x1
        x1 = x_next
        n_iteraciones += 1
    return {'raiz': x_next,
            'error': error,
            'iteraciones': n_iteraciones,
            'errores': np.array(errores),
            'aproximaciones': np.array(aproximaciones)
            }
