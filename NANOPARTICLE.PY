from ase.cluster import Icosahedron 
from ase.visualize import view


nanoparticle = Icosahedron("Na", noshells=2)

view(nanoparticle)