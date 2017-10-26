GlowScript 2.1 VPython


#scene.width =800
#scene.height = 800
#Create the graphics display for the relative position

#gd = gdisplay(x=0,y=600,width=600,height=300,
#    title='Relative position',
#    xtitle='Time (years)',
#    ytitle='Relative pos. (Earth radii)')
#create the figure for the relative position

#f1 = gcurve(gdisplay=gd,color=color.red)
#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60
year_in_s = 365*24*60*60

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6, color=color.yellow,make_trail=True) #trail= curve(color=craft.color)    ## for leaving a trail behind the craft
vcraft = vector(0,2e3,0)
pcraft = mcraft*vcraft
t = 0

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP
while t < 10*year_in_s:
    rate(1000)          ## slow down motion to make animation look nicer
    rce       = craft.pos-Earth.pos
#    f1.plot(pos=(t/year_in_s,mag(rce)/Earth.radius))
    Fg_mag    = G * mEarth * mcraft /mag(rce) ** 2
    Fg_hat    = -norm(rce)
    Fnet      = Fg_mag * Fg_hat
    pcraft    = pcraft + Fnet * deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    #trail.append(pos=craft.pos)
    t = t+deltat
    
    
    
    






