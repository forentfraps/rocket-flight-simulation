import numpy as np
from scipy.integrate import odeint
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
G_BIG = 6.67430 * 10 ** (-11)                   #grav constant
PLANET_MASS = 5.972 * 10 ** 24                  #desired planet mass
PLANET_RADIUS = 6371000                         #desired planet radius
AIR_DENSITY = 1.275                             #desired air density
##WIND_SPEED = 0 #                              UNUSED (FOR NOW)
##WIND_ALPHA = math.pi/36                       # UNUSED (FOR NOW)
##WIND_BETA = math.pi/4                         # UNUSED (FOR NOW)
R1_MASS = 5200                                  #rocket components mass
R1_S = 0.81                                     #rocket area
R1_V = 1000                                     #rocket base speed
R1F_MASS = 52000                                #rocket fuel mass
R1F_CONSUMPTION = 900                           #rocket fuel consumption per second
R1F_SPEED = 1000                                #fuel exhaustion speed relative to the rocket
R1_ALPHA = math.pi/4                            #angle alpha in polar coordinates (X/Y plane)
R1_BETA = math.pi/4                             #angle beta in polar coordinates (Z plane)
#SOUND_V = 330                                  #UNUSED
G = G_BIG * PLANET_MASS/ (PLANET_RADIUS ** 2)   #computes g 
BIGNUMBA = 200000                               #seconds to evaluate trajectory after fuel is no more, leave it very big, matplotlib is very smart
#print(T_LIMIT)
global fig, ax
fig = plt.figure()                              #set up matplotlib for 3d plotting
ax = fig.add_subplot(111,projection='3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
def dxyzdt(f, t, rmass, fmass, fcons , fspeed, aird, rs, g): #solves the system of non-linear differential equations for first part of the trajectory, when fuel is present
    vx = f[1]       #obtain derivatives for speeds
    vy = f[3]
    vz = f[5]
    k = aird * 0.6 * rs / 2                                                                                             # air resistance coefficient, 0.6 is an aerodynamical coefficient for a rocket similar object
    d2xdt = (fcons * (-vx + fspeed) - k * math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)*vx)/(rmass+fmass - fcons * t)          # differential equation for acceleration on proj X
    d2ydt = (fcons * (-vy + fspeed) - k * math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)*vy)/(rmass+fmass - fcons * t)          # differential equation for acceleration on proj Y
    d2zdt = -g + (fcons * (-vz + fspeed) - k * math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)*vz)/(rmass+fmass - fcons * t)     # differential equation for acceleration on proj Z
    return [vx,d2xdt,vy, d2ydt,vz, d2zdt]
def dxyz1dt(f, t, rmass, fmass, fcons , fspeed, aird, rs, g): #second part, without fuel => mass = constant
    vx = f[1]
    vy = f[3]
    vz = f[5]
    k = aird * 0.6 * rs / 2
    d2xdt = ( - k * math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)*vx)/rmass
    d2ydt = ( - k * math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)*vy)/rmass
    d2zdt = -g + ( - k * math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)*vz)/rmass
    return [vx,d2xdt,vy, d2ydt,vz, d2zdt]
def plot_me(clr, a = math.pi/4, b = math.pi/4, fcons = 600, fsp = 1000, v = 1000): #made for easier plotting
    T_LIMIT = R1F_MASS // fcons #seconds for the first part of the trajectory
    ns = np.linspace(0,T_LIMIT,T_LIMIT)
    solution = odeint(dxyzdt, [0,v * math.sin(a)*math.sin(b),0,v*math.sin(b)*math.cos(a),0,v*math.cos(b)], ns , args = ( R1_MASS, R1F_MASS, fcons, fsp, AIR_DENSITY, R1_S, G))                                      #solving 1st equation
    ns2 = np.linspace(T_LIMIT+1, T_LIMIT+BIGNUMBA, BIGNUMBA)
    solution1 = odeint(dxyz1dt, [solution[:,0][-1],solution[:,1][-1],solution[:,2][-1],solution[:,3][-1],solution[:,4][-1],solution[:,5][-1]], ns2 , args = ( R1_MASS, R1F_MASS, fcons, fsp, AIR_DENSITY, R1_S, G)) #solving 2nd equation
    x=[] #merge arrays from the first and second part
    y=[]
    z=[]
    flag = 1 
    for i in range (0,T_LIMIT):
        x.append(solution[:,0][i])
        y.append(solution[:,2][i])
        z.append(solution[:,4][i])
    for i in range(0,BIGNUMBA):
        x.append(solution1[:,0][i])
        y.append(solution1[:,2][i])
        if solution1[:,4][i] > 0 and flag == 1: #to prevent ugly results below z = 0
            z.append(solution1[:,4][i])
        else: 
            z.append(0)
            flag = 0
    ax.plot(x,y,z,clr)
#cool examples
plot_me("blue",a = math.pi/6,fcons =600)
plot_me("red", a= math.pi/2000,fcons=300)
plot_me("green", a = math.pi/3,fcons = 200)
plot_me("black", a = math.pi/2, b = math.pi/3,fcons = 150,fsp=2000)
plt.show()
