#include<iostream>
#include<iomanip>
#include<cmath>
#include <math.h>
#include <fstream>
using namespace std;

double rk2(double y, double v, double dv, double dt, int n);
int main(){
 double x0,yo,km,tmax,dt;
 x0 = 0;
 y0 = 1;
 km = 3;
 tmax = 5;
 dt = 0.01;
 int n = (int)tmax/dt;
 double *x,*ve,*t;
 x = new double[n+1];
 ve = new double[n+1];
 t = new double[n+1];
 x[0] = x0;
 ve[0] = v;
 t[0] = 0;
 for(int i = 0; i<n;i++){
    t[i+1] = t[i] + dt;
    x[i+1] = rk2(x[i], ve[i], dt);
    ve[i+1] = rk2(ve[i],-k*x[i],dt);
}


 return 0;
}

}
double rk2(double y, double v, double dv, double dt, int n){
  return y + n*


}
double a(double x){
  return -x;
}
