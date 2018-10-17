#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;
double method(double x, double v, double dt);
int main(){
  double x0,v,k,tmax,dt;
  x0 = 0;
  v = 1;
  k = 1;
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
    x[i+1] = method(x[i], ve[i], dt);
    ve[i+1] = method(ve[i],-k*x[i],dt);
    cout<<x[i+1]<<endl;
  }

return 0;
}


double method(double x, double v, double dt){
  return x + v*dt;
}
double a(double x){
  return -x;
}
