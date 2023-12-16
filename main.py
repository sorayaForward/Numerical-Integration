from scipy.integrate import quad
import matplotlib.pyplot as plt
import functions as f
import methodes as mt
import numpy as np

nombre_de_points = [10, 20, 40, 100, 150] # nbr sous intervales
functions = [f.f1, f.f2, f.f3, f.f4]
intervals = [[-np.pi, np.pi], [0, 3 * np.pi/2], [0, 1], [0, 2 * np.pi]] # les bornes d'integration pour chaque fonction
integrales = [[[0 for _ in range(5)] for _ in range(4)] for _ in range(len(nombre_de_points))] # [f1(m1,m2,m3,m4,m5)      f2              f3               f4
                                                                                               # [[idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%2, 0]], n=10
                                                                                               # [[idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%2, 0]], n=20
                                                                                               # [[idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%2, 0]], n=40
                                                                                               # [[idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%2, 0]], n=100
                                                                                               # [[idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%idx, 0], [idx//2, idx%2, idx//2, idx%2, 0]]  n=150
                                                                                               # ]

quads = []  # f1 | f2 | f3 | f4
errors = [[[0 for _ in range(5)] for _ in range(4)] for _ in range(len(nombre_de_points))]

# Calcule des integrales + les erreurs (integral approchee / integral reel)
for i, func in enumerate(functions):
    I, err = quad(func, intervals[i][0], intervals[i][1])
    quads.append(I)
    for j, n in enumerate(nombre_de_points):
        integrales[j][i][0] = mt.methodeAdroite(func, intervals[i][0], intervals[i][1], n)
        errors[j][i][0] =  abs(integrales[j][i][0]/I)
        integrales[j][i][1] = mt.methodeAgauche(func, intervals[i][0], intervals[i][1], n)
        errors[j][i][1] =  abs(integrales[j][i][1]/I)
        integrales[j][i][2] = mt.methodeMilieu(func, intervals[i][0], intervals[i][1], n)
        errors[j][i][2] =  abs(integrales[j][i][2]/I)
        integrales[j][i][3] = mt.trapezGeneralise(func, intervals[i][0], intervals[i][1], n)
        errors[j][i][3] =  abs(integrales[j][i][3]/I)
        integrales[j][i][4] = mt.simpsonGeneralise(func, intervals[i][0], intervals[i][1], n)
        errors[j][i][4] =  abs(integrales[j][i][4]/I)

################################# Presentation #################################
x = 0
y = 0
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid for four plots
fig.suptitle('Evolution de l\'erreur d\'intégration des différentes méthodes pour différentes fonctions')
for idx in range(len(functions)):
    axs[idx//2, idx%2].plot(nombre_de_points, [errors[0][idx][0],errors[1][idx][0],errors[2][idx][0],errors[3][idx][0],errors[4][idx][0]], label="rectangles droites")
    axs[idx//2, idx%2].legend()
    axs[idx//2, idx%2].plot(nombre_de_points, [errors[0][idx][1],errors[1][idx][1],errors[2][idx][1],errors[3][idx][1],errors[4][idx][1]], label="rectangles gauches")
    axs[idx//2, idx%2].legend()
    axs[idx//2, idx%2].plot(nombre_de_points, [errors[0][idx][2],errors[1][idx][2],errors[2][idx][2],errors[3][idx][2],errors[4][idx][2]], label="rectangles milieu")
    axs[idx//2, idx%2].legend()
    axs[idx//2, idx%2].plot(nombre_de_points, [errors[0][idx][3],errors[1][idx][3],errors[2][idx][3],errors[3][idx][3],errors[4][idx][3]], label="trapezes")
    axs[idx//2, idx%2].legend()
    axs[idx//2, idx%2].plot(nombre_de_points, [errors[0][idx][4],errors[1][idx][4],errors[2][idx][4],errors[3][idx][4],errors[4][idx][4]], label="simpsons")
    axs[idx//2, idx%2].legend()
    axs[idx//2, idx%2].set_xlabel('Valeurs de n')
    axs[idx//2, idx%2].set_ylabel('Erreurs f'+str(idx+1))

# Presenter chaque fonction avec la surface a calculer
x = 0
y = 0
x_intervals = [np.linspace(-np.pi,np.pi,100), np.linspace(0,3*np.pi/2, 100), np.linspace(0, 1, 100), np.linspace(0,2*np.pi, 100)]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Representation des surfaces a calculer leurs integral')
for idx, fun in enumerate(functions):
    # Plot the graphs in each subplot
    axs[idx//2, idx%2].plot(x_intervals[idx], fun(x_intervals[idx]))
    axs[idx//2, idx%2].fill_between(x_intervals[idx], 0, fun(x_intervals[idx]), alpha=0.3, color='green')
    axs[idx//2, idx%2].set_xlabel('x')
    axs[idx//2, idx%2].set_ylabel('f'+str(idx+1))


n = 10
colors = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink']
for i, fun in enumerate(functions):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Representation des trapèzes et rectangles pour fonction '+str(i+1))
    for j in range(len(functions)):
        axs[j//2, j%2].plot(x_intervals[i], fun(x_intervals[i]))
    axs[0,0].set_title('Rectangles a droite')
    axs[0,1].set_title('Rectangles a gauche')
    axs[1,0].set_title('Rectangles a milieu')
    axs[1,1].set_title('Trapezes')
    x_values = np.linspace(intervals[i][0], intervals[i][1], n+1)
    for i, color in enumerate(colors): # or for i in range(n)
    # Rectangles a droite
        axs[0,0].fill_between([x_values[i], x_values[i+1]],[fun(x_values[i]), fun(x_values[i])], facecolor=color, alpha=0.5)
    # Rectangles a gauche
        axs[0,1].fill_between([x_values[i], x_values[i+1]],[fun(x_values[i+1]), fun(x_values[i+1])], facecolor=color, alpha=0.5)
    # Rectangles au milieu
        # Calculate midpoints between intervals
        midpoints = (x_values[:-1] + x_values[1:]) / 2
        axs[1,0].fill_between([x_values[i], x_values[i+1]], [fun(midpoints[i]), fun(midpoints[i])], facecolor=color, alpha=0.5)
    # Trapezes
        x_trapezoid = [x_values[i], x_values[i+1], x_values[i+1], x_values[i], x_values[i]]
        y_trapezoid = [0, 0, fun(x_values[i+1]), fun(x_values[i]), 0]
        axs[1, 1].fill(x_trapezoid, y_trapezoid, facecolor=color, alpha=0.5)
plt.tight_layout() # Adjust layout
plt.show()


