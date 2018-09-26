mkdir Temperaturas
cd Temperaturas
wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt
cp ../tempdata.txt ./
#Para los datos de Antartida, guardar en un archivo llamado menorque30.txt, los a~nos en los que en al menos uno de los meses, la temperatura fue menor a -30 grados Celsius.

awk '{for(j = 2;j<(NF-1);j++){if($j<-30){print $1break} }}'tempdata.txt > menorque30.txt

#Para los datos de Antartida, guardar en un archivo llamado menorque6.txt, los a~nos en los que las temperaturas medias de todos los meses fueron menores a -6 grados Celsius.

sed -e "s/       /      0/g" tempdata.txt|awk '{if($14!="" && $14<=-6) print $1}' > menorque6.txt

#Guardar en un archivo llamado junio.txt todas las temperaturas medias del mes junio.

sed -e "s/       /      0/g" tempdata.txt| awk '{print $7}'|tail -n +3 > junio.txt

#Imprimir en la terminal el numero total de a~nos en los que la temperatura media fue mayor a -15 grados Celsius.

echo "El total de años en los cuales la temperatura media fue mayor a -15 grados celcius es:" sed -e "s/       /      0/g" tempdata.txt | sed -e "s/*//g"|awk '{if($14!="" && $14>=-15) print $1 }'| tail -n +2

#Borrar el archivo tempdata.txt.
rm tempdata.txt

#Correr el script de python.
python MartinezValencia_temp.py

wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt

