GlowScript 2.1 VPython

##################################
#
#  Physics 241
#  Lab 4
#  Problem 65
#  Group 4
#  Driver: James Gallegos
#  Navigator: Cameron Kimber
#  20 Septemeber 2017
#
##################################


#Definition of constants
G             =  6.7e-11
mEarth        =  6e24
mcraft        =  15e3
deltat        =  60
year_in_s     =  365*24*60*60
Fg_scale      =  5000
pcraft_scale  =  1


#OBJECTS AND INITIAL VALUES
Earth    =  sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft    =  sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6, color=color.yellow,make_trail=True) #trail= curve(color=craft.color)    ## for leaving a trail behind the craft

rce      =  craft.pos-Earth.pos
Fg_mag   =  G * mEarth * mcraft /mag(rce) ** 2
Fg_hat   =  norm(rce)
Fnet     =  Fg_mag * Fg_hat
Fg_arrow =  arrow(pos= craft.pos, axis=Fg_scale*Fnet, color=color.white)


vcraft   =  vector(0,3e3,0)
pcraft   =  mcraft*vcraft t = 0
t        =  0

pcraft_arrow  =  arrow(pos=craft.pos,axis=pcraft_scale*pcraft,color=color.red)


#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP
while t < 10*year_in_s:
    rate(1000)          ## slow down motion to make animation look nicer
    rce               = craft.pos-Earth.pos
    Fg_mag            = G * mEarth * mcraft /mag(rce) ** 2
    Fg_hat            = -norm(rce)
    Fnet              = Fg_mag * Fg_hat
    Fg_arrow.pos      = craft.pos
    Fg_arrow.axis     = Fg_scale*Fnet
    pcraft            = pcraft + Fnet * deltat
    craft.pos         = craft.pos + (pcraft/mcraft)*deltat
    t                 = t+deltat
    pcraft_arrow.pos  = craft.pos
    pcraft_arrow.axis = pcraft_scale*pcraft
    

