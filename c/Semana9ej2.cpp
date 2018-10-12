#include<iostream>
#include<cmath>
using namespace std;
/*Punto 1, imprimir que escriba un numero */
void rellenar(float **a, int filas, int columnas);
void imprimision(float *a,int filas,int columnas);
int main(){
  int numero;
  cout<<"Escriba un numero del 4 al 12 "<<endl;
  cin>>numero;
  if(numero<4 || numero>12){
    cout<<"El numero no esta en el rango indicado"<<endl;
  }
  /*para crear la matriz*/
  float **matriz;
  matriz = new float *[numero+2];
  for(int i = 0; i<numero+2;i++)
    matriz[i] = new float[numero+2];
  rellenar(matriz,numero+2,numero);
  return 0;
}

void rellenar(float **a, int filas, int columnas){
  for (int i = 0; i<filas; i++){
    for(int j = 0; j<columnas;j++){
      a[i][j] = i+j;
    }

  }

}
void imprimision(float *a,int filas,int columnas){
  for(int i = 0; i<columnas; i++){
    cout << "cabeza"<<i<<":"<<a[i]<<endl;
  }
  float sumatoria = 0;
  for(int i = 0;i<filas;i++){
    int seudo_sum = columnas +i;
    sumatoria = sumatoria + *(a + seudo_sum);
  }
  cout<<"suma de la primera columna"<<sumatoria<<endl;

}
