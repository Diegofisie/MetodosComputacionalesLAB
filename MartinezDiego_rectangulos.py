
# coding: utf-8

# In[6]:


import numpy as np


# In[13]:


def rectangulos_intersectados(x1,y1,x2,y2,b1,d1,b2,d2):
    #la cordenada en la cual los re tangulos se intersectarán formando un rectangulo entre ellos
    rectangulos = np.zeros([2])
    # booleano para describir si hay intersección o no
    interseccion = False
    if( abs(y1-y2) <= (b1/2 + b2/2) and abs(x1-x2) <= (d1/2 + d2/2)):
        interseccion = True
        rectangulos[0] = min(abs((x2+d2/2)-(x1-d1/2)),abs((x1+d1/2)-(x2-d2/2)))
        rectangulos[1] = min(abs((y2+b2/2)-(y1-b1/2)),abs((y1+b1/2)-(y2-b2/2)))
        
        if( x2+d2/2 <= x1+d1/2 and x2-d2/2 >= x1-d1/2):
            rectangulos[0] = d2
            
        elif (x2-d2/2 <= x1-d1/2 and x2+d2/2 >= x1+d1/2):
            rectangulos[0] = d1
            
        elif( y2+b2/2 <= y1+b1/2 and y2-b2/2 >= y1-b1/2):
            rectangulos[1] = b2
            
        elif(y2-b2/2 <= y1-b1/2 and y2+b2/2 >= y1+b1/2):
            rectangulos[1] = a11
#retorna si hay intersección y las cordenadas en las ciales hay
    return interseccion,rectangulos
#FUncion para saber si los rectangulos se tocan en un solo punto. En este caso las esquinas.
def rectangulos_extremos(x1,y1,x2,y2,b1,d1,b2,d2):
#booleano para saber si hay intersección
    interseccion_extrempos = False
#array con las coordenadas en donde se tocan.
    puntos_se_tocan = np.zeros([2])
    if((x1+d1/2) == (x2-d2/2) and (y1-b1/2.0) == (y2+b2/2)):
        interseccion_extrempos = True
        puntos_se_tocan[0] = (x1+d1/2)
        puntos_se_tocan[1] = (y1-b1/2)
    elif((x1-d1/2) == (x2+d2/2) and (y1+b1/2) == (y2-b2/2)):
        interseccion_extrempos = True
        puntos_se_tocan[0] = (x1-d1/2)
        puntos_se_tocan[1] = (y1+b1/2)
        
    elif((x1+d1/2) == (x2-d2/2) and (y1+b1/2) == (y2-b2/2)):
        interseccion_extrempos = True
        puntos_se_tocan[0] = (x1+d1/2)
        puntos_se_tocan[1] = (y1+b1/2)
                
    elif( (y1-b1/2) == (y2+b2/2) and (x1-d1/2) == (x2+d2/2)):
        interseccion_extrempos = True
        puntos_se_tocan[0] = (x1-d1/2)
        puntos_se_tocan[1] = (y1-b1/2)
        


#restorna si hay una intersección de los rectangulos en un solo punto y la coordenada. 
    return interseccion_extrempos,puntos_se_tocan

#Función para saber si los rctángulos se intesectan en la slineas verticales u horizontales
def interseccion_lateral_horizontal(x1,y1,x2,y2,b1,d1,b2,d2):
    interseccion_lados = False
    coordenada = ['','']
#para verificar la intersección de los rectangulos horizontamnte 
    if(abs(x1-x2) <= (d1/2+d2/2)):
        if((y1+b1/2) == (y2-b2/2)):
            coordenada[0] = "Intersección Horizontal:"
            interseccion_lados = True
            coordenada[1] = "Y0:"+str(y1+b1/2)
        elif((y1-b1/2) == (y2+b2/2)):
            coordenada[0] = "intersección Hotizontal:"
            interseccion_lados = True
            coordenada[1] = "Y0:"+str(y1-a1/2)
#Para verificar si existe interseción de los resctangulos verticalmente
    if(abs(y1-y2) <= (b1/2+b2/2)):
        if((x1+d1/2) == (x2-d2/2)):
            coordenada[0] = "Intersección vertical"
            interseccion_lados = True
            coordenada[1] = "X0:"+str(x1+d1/2)
        elif((x1-d1/2) == (x2+d2/2)):
            coordenada[0] = "Interseccción vertical"
            interseccion_lados = True
            coordenada[1] = "X0:"+str(x1-d1/2)
#retorna si hay una intersección en algulo de los lados y la coordenada en la cual sucede.
    return interseccion_lados, coordenada


# In[14]:


#Para retornar los valores de las coordenadas y las respuestas si los rectangulos se intersectan o no:
def intersecciones_de_los_rectangulos(x1,y1,x2,y2,b1,d1,b2,d2):
    rectangulo_nuevo = rectangulos_intersectados(x1,y1,x2,y2,b1,d1,b2,d2)
    un_punto_rectangulo = rectangulos_extremos(x1,y1,x2,y2,b1,d1,b2,d2)
    interseccion_de_rectas = interseccion_lateral_horizontal(x1,y1,x2,y2,b1,d1,b2,d2)
    if rectangulo_nuevo[0]:
        print ("Los rectangulos se intersectan formando un rectangulo de lados X:" + str(rectangulo_nuevo[1][0]) +",Y:" +str(rectangulo_nuevo[1][1]))
    elif un_punto_rectangulo[0]:
        print ("Los rectangulos se tocan en un solo punto con coordenadas:"+str(un_punto_rectangulo[1][0] +","+str(un_punto_rectangulo[1][1])))
    elif interseccion_de_rectas[0]:
        print ("los rectangulos se intersectan en una recta" + str(interseccion_de_rectas[1][0]) + "Con coordenadas" + str(interseccion_de_rectas[1][1]))
    else:
        print ("Los rectangulos no se intersectan :c")


# In[15]:


#prueba
intersecciones_de_los_rectangulos(1,2,3,4,5,6,7,8)

