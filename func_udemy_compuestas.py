"""
las func son para evitar escribir miles de lineas de codigo...

solo con def y luego llamarlas ahorramos tiempo y escritura

un prog u func bien hecho realmente vale la pena


"""
#def a inic proc funciones
def juego_colores():
    
    #def o inic var o const
    points=0
    color1= input('Ingrese color1: ,')
    color2= input('Ingrese color2: ,')
    
    #operatividad y funcionalidad
    color1_final= color1.lower()
    color2_final=color2.lower()
    
    #estruc cond compuesta
    if (color1_final == 'azul'):
        points = 50
    else:
        points = 5
    #mostrar info
    print(f'Color1: {color1}')
    print(f'Color2: {color2}')
    print(f'Puntos: {points}')
    
#invocar o llamar proc funciones
juego_colores()
    
    
    
    


















