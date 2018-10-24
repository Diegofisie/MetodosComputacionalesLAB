#include <iostream>
#include <fstream>
using namespace std;
/*Punto 1 */
#define N 200
#define pi 3.14159265358979323846264338327950288
float dx = 8*pi/N;
double func_prime_1(double x, double y1, double y2);
double func_prime_2(double x, double y1, double y2, double b);
/*Punto 2 */
int main(){
    ofstream myfile;
    myfile.open ("RK4Diego.txt");
double *x = new double[N];
double *y1 = new double[N];
double *y1p = new double[N];
double *y2 = new double[N];
double *y2p = new double[N];
double b1 = 0;
double b2 = 3;

x[0] = 0;
y1[0], y2[0], y1p[0], y2p[0] = 1;
/*Punto 3 y 4*/
for (int i = 1; i < N; i++){
    double k_1_prime1 = func_prime_1(x[i-1],y1[i-1], y1p[i-1]);
    double k_1_prime2 = func_prime_2(x[i-1],y1[i-1], y1p[i-1], b1);
    
    double x1 = (x[i-1]+ (dx/2.0));
    double y1_1 = y1[i-1]+ (dx/2.0) * k_1_prime1;
    double y2_1 = y1p[i-1]+ (dx/2.0) * k_1_prime2;
    double k_2_prime1 = func_prime_1(x1, y1_1, y2_1);
    double k_2_prime2 = func_prime_2(x1, y1_1, y2_1, b1);
    
    double x2 = (x[i-1] + (dx/2.0));
    double y1_2 = y1[i-1] + (dx/2.0) * k_2_prime1;
    double y2_2 = y1p[i-1] + (dx/2.0) * k_2_prime2;
    double k_3_prime1 = func_prime_1(x2, y1_2, y2_2);
    double k_3_prime2 = func_prime_2(x2, y1_2, y2_2, b1);
    
    double x3 = x[i-1] + dx;
    double y1_3 = y1[i-1]+ dx * k_3_prime1;
    double y2_3 = y1p[i-1] + dx * k_3_prime2;
    double k_4_prime1 = func_prime_1(x3, y1_3, y2_3);
    double k_4_prime2 = func_prime_2(x3, y1_3, y2_3, b1);
    
    double average_k_1 = (1.0/6.0)*(k_1_prime1 + 2.0*k_2_prime1 + 2.0*k_3_prime1 + k_4_prime1);
    double average_k_2 = (1.0/6.0)*(k_1_prime2 + 2.0*k_2_prime2 + 2.0*k_3_prime2 + k_4_prime2);
    x[i] = x[i-1] + dx;
    y1[i] = y1[i-1] + dx * average_k_1;
    y1p[i]= y1p[i-1] + dx * average_k_2;

}

/* Para Y2*/
for (int i = 1; i < N; i++){
    double k_1_prime1 = func_prime_1(x[i-1],y2[i-1], y2p[i-1]);
    double k_1_prime2 = func_prime_2(x[i-1],y2[i-1], y2p[i-1],b2);
    
    double x1 = (x[i-1]+ (dx/2.0));
    double y1_1 = y2[i-1]+ (dx/2.0) * k_1_prime1;
    double y2_1 = y2p[i-1]+ (dx/2.0) * k_1_prime2;
    double k_2_prime1 = func_prime_1(x1, y1_1, y2_1);
    double k_2_prime2 = func_prime_2(x1, y1_1, y2_1,b2);
    
    double x2 = (x[i-1] + (dx/2.0));
    double y1_2 = y2[i-1] + (dx/2.0) * k_2_prime1;
    double y2_2 = y2p[i-1] + (dx/2.0) * k_2_prime2;
    double k_3_prime1 = func_prime_1(x2, y1_2, y2_2);
    double k_3_prime2 = func_prime_2(x2, y1_2, y2_2,b2);
    
    double x3 = x[i-1] + dx;
    double y1_3 = y2[i-1]+ dx * k_3_prime1;
    double y2_3 = y2p[i-1] + dx * k_3_prime2;
    double k_4_prime1 = func_prime_1(x3, y1_3, y2_3);
    double k_4_prime2 = func_prime_2(x3, y1_3, y2_3,b2);
    
    double average_k_1 = (1.0/6.0)*(k_1_prime1 + 2.0*k_2_prime1 + 2.0*k_3_prime1 + k_4_prime1);
    double average_k_2 = (1.0/6.0)*(k_1_prime2 + 2.0*k_2_prime2 + 2.0*k_3_prime2 + k_4_prime2);
    x[i] = x[i-1] + dx;
    y2[i] = y2[i-1] + dx * average_k_1;
    y2p[i]= y2p[i-1] + dx * average_k_2;
    myfile << x[i] << " " << y1[i] << " " << y2[i] << endl;
    
}
    myfile.close();
  return 0;
}


/* Punto 5 ===== Cual programa?*/


double func_prime_1(double x, double y1, double y2){
return y2;
}
double func_prime_2(double x, double y1, double y2, double b){
return -y1*y1 - y2;
}

