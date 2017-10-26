

##################################
#
#  Physics 241
#  Lab 8
#  Problem 78
#  Group 4
#  Driver: Cameron Kimber
#  Navigator: Cameron Kimber
#  25 October 2017
#
##################################

from visual import *
from visual.graph import *
graph1 = gdisplay(title ="Orbital Energies", x = 0, y = 400, width = 400, height = 400)

#Definition of constants
G             =  6.7e-11
mEarth        =  6e24
mcraft        =  15e3
deltat        =  10
year_in_s     =  365*24*60*60
Fg_scale      =  5000
pcraft_scale  =  1


#OBJECTS AND INITIAL VALUES
Earth    =  sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft    =  sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6, color=color.yellow,make_trail=True) #trail= curve(color=craft.color)    ## for leaving a trail behind the craft

rce      =  craft.pos-Earth.pos
Fg_mag   =  G * mEarth * mcraft /mag(rce) ** 2
Fg_hat   =  -norm(rce)
Fnet     =  Fg_mag * Fg_hat
Fg_arrow =  arrow(pos= craft.pos, axis=Fg_scale*Fnet, color=color.white)

##vcraft   =  vector(0,3E3,0) Elliptical
vcraft   =  vector(0,3.54E3,0)
pcraft   =  mcraft*vcraft 
t        =  0

pcraft_arrow  =  arrow(pos=craft.pos,axis=pcraft_scale*pcraft,color=color.red)

Kgraph = gcurve(gdisplay = graph1, color = color.green, dot = True)
Ugraph = gcurve(gdisplay = graph1, color = color.red, dot = True)
KplusUgraph = gcurve(gdisplay = graph1, color = color.blue, dot = True)

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP
while t < 10 * year_in_s:
    rate(1000)          
    rce               = craft.pos-Earth.pos
    Fg_mag            = G * mEarth * mcraft /(mag(rce) ** 2)
    Fg_hat            = -norm(rce)
    Fnet              = Fg_mag * Fg_hat
    Fg_arrow.pos      = craft.pos
    Fg_arrow.axis     = Fg_scale*Fnet
    pcraft            = pcraft + Fnet * deltat
    craft.pos         = craft.pos + (pcraft/mcraft)*deltat
    t                 = t+deltat
    pcraft_arrow.pos  = craft.pos
    pcraft_arrow.axis = pcraft_scale*pcraft
    # Energy calculation/updates and graph
    K = (mag(pcraft)**2)/(2*mcraft)
    U = -(G * mEarth * mcraft)/(mag(rce))
    Kgraph.plot(pos=(t,K))
    Ugraph.plot(pos=(t,U))
    KplusUgraph.plot(pos=(t,K+U))
    
## Answer for d is vcraft = 2.51E3
## Answer for e is vcraft = 3.54E3 
## Answer for f -> K starts out positive and asymptotes to 0 a t
## infinity, while U starts at -K and asymptotes to 0 at infinity
