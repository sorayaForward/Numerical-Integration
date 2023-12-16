
# methode des rectanlges a gauche (aire inf)
def methodeAgauche(f,a,b,n): 
    h = (b-a)/n # le pas
    s = 0
    for i in range(n): 
        s += f(a + i*h)
    return h*s

# methode des rectanlges a droite (aire sup)
def methodeAdroite(f,a,b,n): 
    h = (b-a)/n # le pas
    s = 0
    for i in range(n):
        s += f(a + (i+1)*h)
    return h*s

# methode des rectanlges au milieu
def methodeMilieu(f,a,b,n): 
    h = (b-a)/n # le pas
    s = 0
    for i in range(n):
        s += f((a+i*h + a+(i+1)*h)/ 2)
    return h*s

# methode de trapeze composite 
def trapezGeneralise(f,a,b,n):
    h = (b-a)/n # le pas
    s = 0
    for i in range(n):
        s += f(a + i*h)
    return h/2*(f(a) + f(b) + 2*s)

# methode de simpson composite 
def simpsonGeneralise(f, a, b, n):
    m = n // 2
    h = (b - a) / n  # Le pas est calculé correctement ici
    s1 = 0
    s2 = 0
    for i in range(1, m+1):
        s1 += f(a + (2 * i - 1) * h)
    for i in range(1, m):
        s2 += f(a + 2 * i * h)
    return h / 3 * (f(a) + f(b) + 4 * s1 + 2 * s2)
