# lorenz.py - Euler and RK4 methods used on the Lorenz attractor
# Author: Joey Robert <joey@joeyrobert.org>
import argparse
from numpy import * 

rho = 28.0; sigma = 10.0; beta = 8.0/3.0;

def lorenz(X, t):
    ''' Lorenz differential equations '''
    return array([
        sigma*(X[1] - X[0]),
        X[0]*(rho - X[2]) - X[1], 
        X[0]*X[1] - beta*X[2],
    ])

def euler(f, h, t_max, X_i):
    ''' Euler's method ''' 
    t = 0
    X = [array(X_i)]
    while(t < t_max):
        deltaX = f(X[-1], t)
        X.append(X[-1] + h*deltaX)
        t += h
    return X

def rk4(f, h, t_max, X_i):
    ''' Classical 4th-order Runge-Kutta method '''
    t = 0
    X = [array(X_i)]
    while(t < t_max):
        k1 = f(X[-1], t)
        k2 = f(X[-1] + h/2.0*k1, t + h/2)
        k3 = f(X[-1] + h/2.0*k2, t + h/2)
        k4 = f(X[-1] + h*k3, t + h)
        X.append(X[-1] + h/6.0*(k1 + 2*k2 + 2*k3 + k4))
        t += h
    return X

def print_data(X):
    ''' Prints data of the form [array(), ...] to a CSV list '''
    for line in X:
        print ','.join('%0.5f' % i for i in line.tolist())

parser = argparse.ArgumentParser()
parser.add_argument('-m', required=True, choices=('euler', 'rk4'), help='numerical method')
parser.add_argument('-ts', type=float, default=0.01, help='time increment')
parser.add_argument('-t_max', type=float, default=50.0, help='maximum time')
parser.add_argument('-x', nargs=3, type=float, default=[1.0, 1.0, 1.0], help='initial position (x,y,z)')
args = parser.parse_args()

if args.m == 'euler':
    data = euler(lorenz, args.ts, args.t_max, args.x)
elif args.m == 'rk4':
    data = rk4(lorenz, args.ts, args.t_max, args.x)

print_data(data)
