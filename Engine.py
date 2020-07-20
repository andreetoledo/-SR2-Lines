#Andree Toledo 18439

from gl import Render, color

r = Render(800,800)

#Size of the vp
r.glViewport(200, 200, 1000, 1000)

#Color picker
r.glClearColor(0,0,0.25)
r.glColor(0.55,0,0)
r.glClear()

#Create Lines 
r.glLine( 1,-1, 1, 0)
r.glLine( 1,-1, 0, 1)
r.glLine( 1, 1,-1, 0)
r.glLine( 1, 1, 1, 1)

r.glLine( 0, 0,-1, 1)
r.glLine( 0, 1,-1, 0)
r.glLine( 0, 0, 1, 1)
r.glLine(-1,-1,-1, 0)


#Imagen de salida
r.glFinish('output.bmp')



