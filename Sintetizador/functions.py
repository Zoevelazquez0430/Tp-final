import numpy as np

def constant(t, param):
    """
    The constant function returns a constant value.
    
    param t: Determine the time at which the function is evaluated
    param param: Define the constant value that will be returned
    return: int 
    """
    return 1

def linear(t, param):
    """
    The linear function takes a scalar t as input 
    
    param t: Scale the time
    param param: Scale the output of the linear function
    return: The value of the slope
    """
    M = t/param[0]
    return M 

def invlinear(t, param):
    """
    The invlinear function is defined as:
        y = (x-param[0])/param[2] + param[3]
    
    
    param t: Scale the output of the function
    param param: Scale the output of the function
    return: The maximum value of 1, which is the same as the invlogistic function
    """
    M= max(1-(t/param[0]), 0)
    return M

def sin(t, param):
    """
    The sin function takes a time t and a parameter par and returns the value of sin(t*par).
    
    param t: Represent the time, and param is used to represent the amplitude of the sin function
    param param: Control the amplitude of the wave
    return: A value that is a function of t
    """
    M= 1+param[0]*np.sin(param[1]*t)
    return M

def exp (t, param):
    """
    The exp function takes a parameter t and returns the value of e**t.
    The function is useful for computing values of an exponential curve.
    
    param t: Define the time point at which the function is evaluated
    param param: Pass the parameters of the exponential function
    return: The exponential of t with the given paramete
    """
    M= np.exp((5*(t-param[0]))/param[0])
    return M

def invexp(t,param):
    """
    The invexp function returns the inverse exponential of its input.
    The function is defined as: 
        f(t) = exp(-t)
    
    param t: Define the time of the function
    param param: Define the parameters of the invexp function
    return: The inverse of the exponential function with parameters t and param
    """
    M= np.exp((-5*t)/param[0])
    return M

def quartcos(t,param):
    """
    The quartcos function returns the cosine of a variable t multiplied by a quartic polynomial.
    
    param t: Define the time of the function
    param param: Define the amplitude of the cosine function
    return: The value of the quartic cosine function with parameters t and param
    """
    M= np.cos((np.pi*t)/2*param)
    return M

def quartsin(t,param):
    """
    The quartsin function returns the value of a quartic sine curve at time t. 
    The function parameters are:
        t (required): the time parameter, in seconds. 
        param (optional): a tuple containing up to three values that modify the behavior of the curve.  

    param t: Represent the time
    param param: Pass the parameters of the function
    return: The value of the sinusoid for a given time and parameter
    """
    M= np.sin((np.sin*t)/2*param[0])
    return M

def halfcos(t,param):
    """
    The halfcos function returns the value of a half-cosine function with amplitude 1 and period T.  
    
    param t: Define the time at which the function is evaluated
    param param: Set the amplitude of the wave
    return: The value of the half cosine function at time t with a given parameter
    """
    M= ((1+np.cos((np.pi*t)/param[0]))/2)
    return M

def halfsin(t,param):
    """
    The halfsin function returns the value of a half-period sine function with amplitude param[0], and angular frequency param[2].
    The time variable used is t, which can be either a single number or an array.
    
    param t: Represent time
    param param: Pass in the parameters of the halfsin function
    return: A value that is half the sine of t
    """
    M= ((1+np.cos(np.pi((t/param[0])-1/2)))/2)
    return M

def log(t,param):
    """
    The log function takes a parameter t and returns the natural log of that value.
    
    param t: Scale the function
    param param: Pass the parameters of the log function
    return: The natural logarithm of the input
    """
    M= np.log(((9*t)/param[0])+1)
    return M

def invlog(t,param):
    """
    The invlog function is a function that takes in a time and parameter, 
    and returns the value of the inverse logistic function. 
    
    param t: Calculate the m value
    param param: Determine the value of m
    return: A value of -9 for all values of t that are less than the parameter,
    and 0 for all values greater than or equal to the parameter
    """
    if t<param:
        M= np.log(((-9*t)/param[0])+10)
    elif t>=param:
        M= 0
    return M

def tri(t, param):
    """
    The tri function returns the value of a triangle function with parameters: 
        t (time), param[0] (midpoint), param[2] (height) and param[3] (width). 
 
    
    param t: Determine the position of the point on the line
    param param: Define the parameters of the function
    return: The value of m
    """
    if t< param[1]:
        M=(t*param[2])/param[1]
    else:
        M=((t-param[1])/(param[1]-param[0]))+ param[2]
    return M
    
def pulses(t, param):
    """ 
    param t: Define the time of the pulse
    param param: Define the pulse shape
    return: The value of the pulse function at a given time
    """
    m= (t/param[0]) - np.floor(t/param[0])
    M= np.min(abs(((1-param[2])/param[1])*(m-param[0]+param[1]))+param[2])
    return M