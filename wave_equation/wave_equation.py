# wave_equation.py - FTCS solution to a 2-dimensional circular drum
# Author: Joey Robert <joey@joeyrobert.org>

# Discrete form of the wave equation (Forward-Time Center-Space)
# [f(x,y,t+2tau) + f(x,y,t) - 2f(x,y,t+tau)]/tau^2 = (c/h)^2*[f(x+h,y,t) + f(x-h,y,t) - 2f(x,y,t)]
#                                                  + (c/h)^2*[f(x,y+h,t) + f(x,y-h,t) - 2f(x,y,t)]
