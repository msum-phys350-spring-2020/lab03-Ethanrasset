#This is nice, I acidently did this part in part 1.

def trapezoidal_rule_loop(a, b, func, N=10):
    """
    Caclculate the definite integral of the function ``func`` from
    ``a`` to ``b`` using the trapezoidal rule.

    Parameters
    ----------

    a : float
        Lower limit of integration.

    b : float
        Upper limit of integration.

    func : function
        The integrand that we want to find the area of.

    N: int, optional
        Number of intervals to use in the trapezoidal rule.
    
    Returns
    -------
        total:float
            An estimant of the integral, or the area under the curve of the function that we input.

    """
    
    h=(b-a)/N
    total_bef=0
    for ct in range(0,N):
        #the test function can be changed out for any function at any time.
        total_bef+=func(a+h*ct)+func(a+h*(ct+1))
        total=(h/2)*total_bef
    return total

# Simpson's rule function


def simpsons_rule(a,b,func,N=10):
    """
    This function is going to use the simps import, to
    find an approximation of the integral, func.

    Parameters
    ----------
    a:float
        lower limit of the integral
    b:float
        upper limit of the integral
    func:function
        This is the function that we want to integrate
    N:int, optional
        This is the number of sections that we are bracking the
        graph into.

    Returns
    -------
    float
        Estimated area under the curve using the simpson's rule.
    """
    import scipy.integrate as sim
    import numpy as np
    #The impute for the functon of this one is going to be the formula we want to integrate.
    x = np.linspace(a,b,N+1)
    y=np.empty(len(x),float)
    for it in range(0,len(x)):
        y[it]=func(x[it])
    #The simps rule takes two imputs, a function and an array. 
    approximation = sim.simps(y,x)
    return approximation
