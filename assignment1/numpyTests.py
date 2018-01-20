import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([
        [1, 2],
        [3, 4]])

#print y.shape
m = np.max(y, 1).reshape(2,1)

n = np.max(x)
x = np.exp(x)/np.sum(x,0)
x = x - n
y = y - m

#print np.exp(x)
#print y.shape[0]
z = np.sum(y,1)
y = np.exp(y)/np.sum(y,1)
#print z
x = np.exp(x)/np.sum(x,0)
a =  np.array([[-1001,-1002]])
print a.shape
max = np.max(a, 1)
a = a - max
print max
#print x
#print y.shape, m, y.transpose()