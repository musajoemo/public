import math
import scipy
import numpy as np

result = 0.0
cdf = 0.0

"""
This is the an implementation to calculate Cummulative Density Function (CDF) and Option Price (in Black-Scholes Model) using the Pseudocode
from the Primer of Mathematics for Financial Engineering by Dan Stefanica.  I will check to see how the
result compares to Matlab's Financial Instrument ToolBox at a later time.  But for now this is just an 
implementation of the code from the above book.  Black-Scholes is an analytical formula and good for valuing instruments
which cannot be exercised before maturity such as European Call or Put.  To value options such as American Put or call which can
be exercised prior to maturity, you may have to use binomial models or trees.  Check out Financial Engineering and Risk Management
on Coursera, the course gave a good treatment of these topics.  I will post codes for building binomial lattices later.
"""
def cumm_dens_function(t):
    z = abs(t)
    y = 1/(1 + 0.2316419*z)
    a1 = 0.319381530 
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429
    
    cdf = 1 - math.exp(-t**2/2)*(a1*y + a2*y**2 + a3*y**3 + a4*y**4+a5*y**5)/math.sqrt(2*math.pi)
    
    if t > 0:
        result = cdf
    else:
        result = 1 - cdf
        
    return result

"""
This is an alternative implementation to calculate CDF using scipy.
This implementation is more straight forward.
"""
def cumm_dens_function_scipy(t):
    return scipy.stats.norm.cdf(t)

"""
Black-Scholes for European Call and Put
"""

def blackScholes(t,S,K,T,a,r,q,Type):
    #t = beginning time
    #S = Spot Price
    #K = Strike
    #T = Maturity
    #a = volatility
    #r = constant interest rate
    #q = continous dividend rate of the underlying asset
    #Type can be call or put - enter as strings e.g. 'call' or 'put'
    call = 0.0
    put = 0.0
    d1 =0.0
    d2 = 0.0
    S = float(S)
    K = float(K)
    
    d1 = (np.log(S/K) +(r - q + a**2/2)*(T - t))/(a*math.sqrt(T-t))
    d2 = d1 - (a*math.sqrt(T-t))
    
    call = S*math.exp(-q*(T-t))*cumm_dens_function_scipy(d1) - K*math.exp(-r*(T-t))*cumm_dens_function_scipy(d2)
    put = K*math.exp(-r*(T-t))*cumm_dens_function_scipy(-d2) - S*math.exp(-q*(T-t))*cumm_dens_function_scipy(-d1)
    
    if Type == 'call':
        return call
    else:
        return put
        
#Sample Calls
print ""
print "The value of a call with the given parameters is : " + str(blackScholes(0,42.0,40.0,0.5,0.3,0.05,0.03,'call'))
print ""
print "The value of a put with the given parameters is : " + str(blackScholes(0,42.0,40.0,0.5,0.3,0.05,0.03,'put'))

        
    
    
    
    
