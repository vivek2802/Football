import numpy as np
import matplotlib
from numpy import genfromtxt
from matplotlib import pyplot as plt

def leftwinger():
    c=[]
    e=[]
    C=[]
    E=[]
    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'LW')
    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,18])+int(ratings[i+1,19])+int(ratings[i+1,20])+int(ratings[i+1,21])+int(ratings[i+1,24])+
                  int(ratings[i+1,25])+int(ratings[i+1,26])+int(ratings[i+1,28])+int(ratings[i+1,29])+int(ratings[i+1,30])+int(ratings[i+1,31])+
                  int(ratings[i+1,32])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+int(ratings[i+1,36])+int(ratings[i+1,37])+
                  int(ratings[i+1,38])+int(ratings[i+1,40])+int(ratings[i+1,41])+int(ratings[i+1,42])+int(ratings[i+1,43])+int(ratings[i+1,44])+int(ratings[i+1,45])+int(ratings[i+1,46])]])
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            print('Best left winger is=',c[j][0])
leftwinger()

def rightwinger():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'RW')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,18])+int(ratings[i+1,19])+int(ratings[i+1,20])+int(ratings[i+1,21])+
                  int(ratings[i+1,25])+int(ratings[i+1,26])+int(ratings[i+1,28])+int(ratings[i+1,29])+int(ratings[i+1,30])+int(ratings[i+1,31])+
                  int(ratings[i+1,32])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+int(ratings[i+1,36])+int(ratings[i+1,37])+
                  int(ratings[i+1,38])+int(ratings[i+1,40])+int(ratings[i+1,41])+int(ratings[i+1,42])+int(ratings[i+1,43])+int(ratings[i+1,44])+int(ratings[i+1,45])+int(ratings[i+1,46])]])
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best right winger is=',c[j][0]
    print(*Best_right_winger)
rightwinger()


def striker():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'ST')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,39])+int(ratings[i+1,19])+int(ratings[i+1,20])+int(ratings[i+1,24])+
                                       int(ratings[i+1,25])+int(ratings[i+1,26])+int(ratings[i+1,29])+int(ratings[i+1,33])+
                                       int(ratings[i+1,34])+int(ratings[i+1,35])+int(ratings[i+1,36])+int(ratings[i+1,37])+
                                       int(ratings[i+1,38])+int(ratings[i+1,40])+int(ratings[i+1,41])+int(ratings[i+1,42])+
                                       int(ratings[i+1,43])+int(ratings[i+1,44])+int(ratings[i+1,45])+int(ratings[i+1,46])]])
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best striker is=',c[j][0]
    print(*Best_right_winger)
striker()

def Centermidfielder():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'CAM')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,18])+int(ratings[i+1,19])+int(ratings[i+1,20])+int(ratings[i+1,21])+
              int(ratings[i+1,25])+int(ratings[i+1,26])+int(ratings[i+1,28])+int(ratings[i+1,29])+int(ratings[i+1,30])+int(ratings[i+1,31])+
              int(ratings[i+1,32])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+int(ratings[i+1,36])+int(ratings[i+1,37])+
              int(ratings[i+1,38])+int(ratings[i+1,40])+int(ratings[i+1,41])+int(ratings[i+1,42])+int(ratings[i+1,43])+int(ratings[i+1,44])+int(ratings[i+1,45])+int(ratings[i+1,46])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best Center attacking midfielder is=',c[j][0]
    print(*Best_right_winger)
Centermidfielder()

def Rightmidfielder():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'RCM')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,18])+int(ratings[i+1,19])+int(ratings[i+1,20])+int(ratings[i+1,21])+
              int(ratings[i+1,25])+int(ratings[i+1,26])+int(ratings[i+1,28])+int(ratings[i+1,29])+int(ratings[i+1,30])+int(ratings[i+1,31])+
              int(ratings[i+1,32])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+int(ratings[i+1,36])+int(ratings[i+1,37])+
              int(ratings[i+1,38])+int(ratings[i+1,40])+int(ratings[i+1,41])+int(ratings[i+1,42])+int(ratings[i+1,43])+int(ratings[i+1,44])+int(ratings[i+1,45])+int(ratings[i+1,46])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best right midfielder is=',c[j][0]
    print(*Best_right_winger)
Rightmidfielder()

def Leftmidfielder():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
#print(ratings[:,5])
    a=(ratings[1:,5]==b'LCM')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,18])+int(ratings[i+1,19])+int(ratings[i+1,20])+int(ratings[i+1,21])+
              int(ratings[i+1,25])+int(ratings[i+1,26])+int(ratings[i+1,28])+int(ratings[i+1,29])+int(ratings[i+1,30])+int(ratings[i+1,31])+
              int(ratings[i+1,32])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+int(ratings[i+1,36])+int(ratings[i+1,37])+
              int(ratings[i+1,38])+int(ratings[i+1,40])+int(ratings[i+1,41])+int(ratings[i+1,42])+int(ratings[i+1,43])+int(ratings[i+1,44])+int(ratings[i+1,45])+int(ratings[i+1,46])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best left midfielder is=',c[j][0]
    print(*Best_right_winger)
    print(max(e))
Leftmidfielder()


def rightback():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'RB')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,21])+int(ratings[i+1,22])+int(ratings[i+1,23])+
                                       int(ratings[i+1,27])+int(ratings[i+1,29])+int(ratings[i+1,30])+
                                       int(ratings[i+1,31])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+
                                       int(ratings[i+1,36])+int(ratings[i+1,38])+int(ratings[i+1,39])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best RIGHT BACK is=',c[j][0]
    print(*Best_right_winger)
    print(max(e))
rightback()


def leftback():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'LB')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,21])+int(ratings[i+1,22])+int(ratings[i+1,23])+
                                       int(ratings[i+1,27])+int(ratings[i+1,29])+int(ratings[i+1,30])+
                                       int(ratings[i+1,31])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+
                                       int(ratings[i+1,36])+int(ratings[i+1,38])+int(ratings[i+1,39])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best LEFT BACK is=',c[j][0]
    print(*Best_right_winger)
    print(max(e))
leftback()

def rightcenterback():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'RCB')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,21])+int(ratings[i+1,22])+int(ratings[i+1,23])+
                                       int(ratings[i+1,27])+int(ratings[i+1,29])+int(ratings[i+1,30])+
                                       int(ratings[i+1,31])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+
                                       int(ratings[i+1,36])+int(ratings[i+1,38])+int(ratings[i+1,39])]])
            
            
            c=c+d
    
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best RIGHT CENTER BACK is=',c[j][0]
    print(*Best_right_winger)
    print(max(e))
rightcenterback()

def leftcenterback():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'LCB')
    print(ratings[1:,5])

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,21])+int(ratings[i+1,22])+int(ratings[i+1,23])+
                                       int(ratings[i+1,27])+int(ratings[i+1,29])+int(ratings[i+1,30])+
                                       int(ratings[i+1,31])+int(ratings[i+1,33])+int(ratings[i+1,34])+int(ratings[i+1,35])+
                                       int(ratings[i+1,36])+int(ratings[i+1,38])+int(ratings[i+1,39])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best LEFT CENTER BACK is=',c[j][0]
    print(*Best_right_winger)
    print(max(e))
leftcenterback()

def goalkeeper():
    c=[]
    e=[]
    C=[]
    E=[]

    ratings=np.genfromtxt('Desktop/football.csv',delimiter=',',dtype=None)
    a=(ratings[1:,5]==b'GK')

    for i in range(len(a)):
        if a[i]==True:
            d=([[str(ratings[i+1,0])]+[int(ratings[i+1,47])+int(ratings[i+1,48])+int(ratings[i+1,49])+
                                       int(ratings[i+1,50])+int(ratings[i+1,51])]])
            
            
            c=c+d
    for j in range(len(c)):
        e=e+[c[j][1]]
        if c[j][1]==max(e):
            Best_right_winger='Best GOALKEEPER is=',c[j][0]
    print(*Best_right_winger)
    print(max(e))   
goalkeeper()



    
    
    


                      
