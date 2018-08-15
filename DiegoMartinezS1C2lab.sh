
			#Visualizar los datos en el archivo descargado
cat notas.txt 
		#N`umero de personas que sacraon entre 4 y 5 en el primer parcial
echo "el n{\'u}mero de personas que tienen la nota entre 4 y 5 es:"
awk '{if ($3 > 4.0 && $3 < 5.0) print ;}' notas.txt | wc -l 
echo "el n{\'u}mero de personas que tienen mas de 15 puntos en el examen final y tienen la nota entre 4 y 5 es:"
awk '{if ($3 > 4.0 && $3 < 5.0 && $6>15) print;}' notas.txt | wc -l
awk '{if ($3 > 4.0 && $3 < 5.0 && $6>15) print;}' notas.txt | wc -l > RES1.txt

	#estudiantes obtuvieron alguna calificaci ́on en 0 y usando la informaci ́on
		#obtenida de el nombre del estudiante que perdi ́o la materia.	
echo "La persona "
grep -w "0" notas.txt | awk '{if($7 < 6.0) print $1,$2;}'
echo "Perdio la materia"

	#cree  un  archivo  de  nombre  RES2.txt  que  contenga  los  apellidos  y
	#notas  de  los  estudiantes  que  obtuvieron  una  nota  mayor  a  8  como  Nota  final,
	#usando este archivo imprima en pantalla cuantos nombres est ́an en esta lista.
awk '{if($7 > 8.0) print $1 ;}' notas.txt > RES2.txt
cat RES2.txt | wc -l  
echo "Personas sacaron una nota mayor a 8 en la final"

#Mueva todos los archivos de texto producidos a una carpeta nueva con el nombre	 RESULTADO
mkdir RESULTADO
mv RES1.txt ./RESULTADO
mv RES2.txt ./RESULTADO



















