import math

def y( x ): 
       
    return (math.log(x)) ## Function is declared here.
      

def trapezoidal (a, b, n): ## This is the integration method.
    h = (b - a) / n 
    s = (y(a) + y(b)) 
    i = 1
    while i < n: 
        s += 2 * y(a + i * h) 
        i += 1
          
    return ((h / 2) * s) 
  


## Declare the limit boundaries here.
from_limit = 2
to_limit = 3  

## Declare the stepsize of the integration process.
step_size = 6
print ("Value of integral is ", 
     "%.4f"%trapezoidal(from_limit, to_limit, step_size)) 
  
