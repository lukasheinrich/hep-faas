import numpy as np
import json

def truth(x):
    xv, yv = x[:,0],x[:,1]
    '''more wiggles in physics case'''
    def xsec(xv,yv):
        return 12*np.exp(-xv/2)+((0.1*np.cos(10*yv+1)))+((0.2*np.cos(15*xv)))

    def eff(xv,yv):
        return np.tanh((1.3*xv-yv)+1)

    def stats(nevents):
        return (1-np.tanh((nevents-5)))/2.

    def event_yield(xv,yv):
        return xsec(xv,yv) * eff(xv,yv)

    def analysis(xv,yv):
        return stats(event_yield(xv,yv))

    return 3*(np.log(analysis(xv,yv)) - np.log(0.05))

def handle(st):
    x = json.loads(st)
    return truth(np.asarray(x['X'])).tolist()
