import matplotlib.pyplot as plt
import numpy as np
import math

w = np.zeros((3,1))

print(w)

phi1 = np.array([1,2,2,3,5])
phi2 = np.array([3,2,1,1,4])
a = np.array([0,1,0,0,1])


plt.figure()
plt.scatter(1,3, c="red", marker="o")
plt.scatter(2,2, c="blue", marker="x")
plt.scatter(2,1, c="red", marker="o")
plt.scatter(3,1, c="red", marker="o")
plt.scatter(5,4, c="blue", marker="x")


def pi(n):
    return 1 / (1 + math.exp( - ( w[0] + w[1] * phi1[n] + w[2] * phi2[n] ) ))

def gsum(numberw, ps):
    if numberw == 0:
        return sum([ps[n]-a[n] for n in range(5)])
    elif numberw == 1:
        return sum([phi1[n] * (ps[n] - a[n]) for n in range(5)])
    else:
        return sum([phi2[n] * (ps[n] - a[n]) for n in range(5)])

#def updatew():
#    w[0] = w[0] - gsum(0)
#    w[1] = w[1] - gsum(1)
#    w[2] = w[2] - gsum(2)
def f(t):
    return - (w[1] * t + w[0]) / w[2]


for i in range(1):
    pis = [pi(n) for n in range(5)]
    w[0] -= gsum(0, pis)
    w[1] -= gsum(1, pis)
    w[2] -= gsum(2, pis)
    print(w)
    if i % 200 == 0:
        t1 = np.arange(0.0, 5.0, 0.1)
        plt.plot(t1, f(t1), label=i)


    # print(w)

#0.5 - 0.5 x - 0.5 y = 0
# y = - x + 1




plt.legend()

plt.draw()

plt.show()

