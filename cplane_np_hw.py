import cplane_np
import numpy as np
import matplotlib.pyplot as plt
import numba as nb



def julia(c):
    @nb.vectorize([nb.int32(nb.complex128)])
    def func510(z):
        if abs(z) > 2:
            return 1
        n = 1
        mag = abs(z)
        while mag < 2 and n < 1000:
            z = z**2 + c
            mag = abs(z)
            n += 1
        if n == 1000:
            return 0
        else:
            return n
    return func510
            
class JuliaPlane(cplane_np.ArrayComplexPlane):
    def gen_plane(self,c):
        '''make it plane'''
        self.plane =  []
        #xs-----------------------------------------------------------------------------
        self.dx = (self.c[1]-self.c[0])/(self.c[2]-1)
        multi = np.array(list(range(0,self.c[2]))*self.c[-1])  #array with index + 1, ylen times
        multi = multi * self.dx #multiply by dx to get how much to add
        multi = self.c[0] + multi
        #ys-----------------------------------------------------------------------------
        self.dy = (self.c[-2]-self.c[-3])/(self.c[-1]-1)
        vec_y = np.array(list(range(0,self.c[-1])))
        vec_y = np.repeat(vec_y,self.c[2])
        vec_y =  (self.c[-3] + vec_y*self.dy)*1j

        #together------------------------------------------------------------------------
        self.plane = multi + vec_y
#         print(self.plane.reshape(self.c[2],self.c[-1]).transpose())
        return self.plane.reshape(self.c[2],self.c[-1]).transpose()
    def __init__(self,d,c = (-2,2,500,-2,2,500)):
        self.c = c
        self.fs = []
        print("init fx")
        self.plane = self.gen_plane(self.c)
#         self.plane = np.vectorize(julia(self.plane))
#         f = np.vectorize(julia(c = d))
        f = julia(c = d)
        self.plane =  f(self.plane)
#         print("------------------------------")
#         print(self.plane)
    def toCSV(self):
        print("PLA")
        print(self.plane)
        np.savetxt("510.csv",self.plane, header = 'xmax is: ' + str(self.c[0]) + 'xmin is: ' + str(self.c[1]) + 'xlen is: ' + str(self.c[2]) +
                   'ymax is: ' + str(self.c[3]) + 'ymin is: ' + str(self.c[4]) + 'ylen is: ' + str(self.c[5])) 
    def fromCSV(self):
        csv = np.array(list(i  for i in (open('510.csv', 'rb'))))
        print(csv)
#         self.c = csv[1]
    def show(self):
        #need x of  reals, y of complex, but now they're all reals...
#         print(self.plane)
        plt.imshow(self.plane,  cmap = plt.cm.hot, interpolation = 'bicubic', extent = [self.c[0], self.c[1], self.c[3], self.c[4]])
        