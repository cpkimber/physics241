

##################################
#
#  Physics 241
#  Lab 4
#  Problem 64
#  Group 4
#  Driver: Cameron Kimber
#  Navigator: Cameron Kimber
#  20 Septemeber 2017
#
##################################

from visual import *

#  Variable Declarations:

G = -6.7e-11  #  Gravitational consstant units of (N * m^2) / kg^2
mass_craft = 15e3  # mass of the spacecraft in units of kg
mass_planet = 6e24  # mass of the planet in units of kg
scalefactor = 25000

#  Object Declarations

planet     =  sphere(pos=vector(0,0,0), radius   =  6.4e6, color  =  color.cyan)
craft_1    =  sphere(pos=vector(-13e7,6.5e7,0), radius = 3e6, color  =  color.red)
craft_2    =  sphere(pos=vector(-6.5e7,6.5e7,0), radius = 3e6 , color  =  color.green)
craft_3    =  sphere(pos=vector(0,6.5e7,0), radius = 3e6 , color  =  color.yellow)
craft_4    =  sphere(pos=vector(6.5e7,6.5e7,0), radius = 3e6, color  =  color.white)
craft_5    =  sphere(pos=vector(13e7,6.5e7,0),  radius = 3e6, color  =  color.blue)

def F_gravy(craft):
    r_vector= planet.pos - craft.pos
    r_mag = mag(r_vector)
    r_hat  = norm(r_vector)
    return (-G * mass_craft * mass_planet / r_mag**2 * r_hat)
    
#  Arrow Declarations

pointer_1  = arrow(pos=craft_1.pos,      axis  =  scalefactor * F_gravy(craft_1),       color  =  color.orange)
pointer_2  = arrow(pos=craft_2.pos,      axis  =  scalefactor * F_gravy(craft_2),         color  =  color.orange)
pointer_3  = arrow(pos=craft_3.pos,      axis  =  scalefactor * F_gravy(craft_3),         color  =  color.orange)
pointer_4  = arrow(pos=craft_4.pos,      axis  =  scalefactor * F_gravy(craft_4),         color  =  color.orange)
pointer_5  = arrow(pos=craft_5.pos,      axis  =  scalefactor * F_gravy(craft_5),         color  =  color.orange)



