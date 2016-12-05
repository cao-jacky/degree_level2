import numpy as np
import matplotlib.pyplot as plt

f = np.poly1d([1,1,1,-1]) # x^3 - 1
fp = np.polyder(f)
def newton(i, guess):
    a = np.empty(guess.shape,dtype=int)
    a[:] = i
    j = np.abs(f(guess))>.00001
    if np.any(j):
        a[j] = newton(i+1, guess[j] - np.divide(f(guess[j]),fp(guess[j])))
    return a

npts = 1000
x = np.linspace(-10,10,npts)
y = np.linspace(-10,10,npts)
xx, yy = np.meshgrid(x, y)
pic = np.reshape(newton(0,np.ravel(xx+yy*1j)),[npts,npts])
plt.imshow(pic)
plt.show()
