# Punto 3
def slope(x1, y1, x2, y2):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    deltay = float(y2-y1)
    deltax = float(x2-x1)
    if x1 == x2: 
        raise Exception('no se puede dividir entre 0')
    return deltay/deltax

if __name__ == '__main__':
    import doctest
    doctest.testmod()
def intercept(x1, y1, x2, y2):
    """
      >>> intercept(1, 6, 3, 12)
      3.0
      >>> intercept(6, 1, 1, 6)
      7.0
      >>> intercept(4, 6, 12, 8)
      5.0
    """ 
    return float(y1 - slope(x1,y1,x2,y2)*x1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

##### Prueba #####3
print slope(1,2,1,5)
    
   




