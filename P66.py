GlowScript 2.6 VPython

##################################
#
#  Physics 241
#  Lab 4
#  Problem 66
#  Group 4
#  Driver: James Gallegos
#  Navigator: Cameron Kimber
#  20 Septemeber 2017
#
##################################

#CONSTANTS
G = 6.7e-11    #  N * m^2 / kg^2
mEarth = 6e24  #  kg
mcraft = 15e3  #  kg
mmoon = 7e22   #  kg
deltat = 60
year_in_s = 365*24*60*60
Fg_scale = 5000
pcraft_scale = 0.5


#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6, color=color.green,make_trail=True)
moon = sphere(pos=vector(4e8,0,0), radius = 1.75e6, color=color.yellow)

rce   = craft.pos-Earth.pos
rcm   = craft.pos-moon.pos
Fg_mag = G * mEarth * mcraft /mag(rce) ** 2
Fg_moon = G * mmoon * mcraft /mag(rcm) **2
Fg_hat = norm(rce)
Fg_hatm = norm(rcm)
Fnet = Fg_mag * Fg_hat + Fg_moon * Fg_hatm

Fg_arrow = arrow(pos= craft.pos, axis=Fg_scale*Fnet, color=color.blue)

vcraft = vector(0,3.3e3,0)
pcraft = mcraft*vcraft

t = 0

pcraft_arrow = arrow(pos=craft.pos,axis=pcraft_scale*pcraft,color=color.red)

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP
while t < 10*year_in_s:
    rate(1000)          ## slow down motion to make animation look nicer
    rce       = craft.pos-Earth.pos
    Fg_mag    = G * mEarth * mcraft /mag(rce) ** 2
    Fg_hat    = -norm(rce)
    Fnet = Fg_mag * Fg_hat + Fg_moon * Fg_hatm
    Fg_arrow.pos = craft.pos
    Fg_arrow.axis = Fg_scale*Fnet
    pcraft    = pcraft + Fnet * deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    t = t+deltat
    pcraft_arrow.pos = craft.pos
    pcraft_arrow.axis = pcraft_scale*pcraft


