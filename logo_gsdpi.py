from altair import FontWeight
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import hsv_to_rgb
from matplotlib.patches import Circle
from matplotlib.text import Text

def draw_phyllotaxis(ax,N,c):
    n  = np.arange(N); 
    th = n*2*np.pi/360*137.5; 
    r  = c*np.sqrt(n);          # distancia al centro
    x  = r*np.cos(th);          # posición x
    y  = r*np.sin(th);          # posición y
    t  = n/N                    # escala de 0 a 1 para color
    R  = (2 - t)*0.4            # radio de las semillas

    # colores con hue variable desde el amarillo (replica el original hecho en D3)
    colors = hsv_to_rgb(np.row_stack([(0.5*x + 0.2,0.3,0.95) for x in t]))

    from matplotlib.patches import Circle
    from matplotlib.text import Text

    
    for i in range(N):
        semilla = Circle((x[i],-y[i]),radius=R[i],alpha=1,color=colors[i,:])
        ax.add_artist(semilla)
        ax.axis(xmin=-10,xmax=80,ymin=-15,ymax=15)




plt.close('all')
plt.ion()



'''
EJEMPLO 1
Figura para fondo blanco con el texto del nombre del grupo
'''

fig, ax = plt.subplots(1)
fig.set_size_inches(9,3)

# logo con 100 semillas y c=1
draw_phyllotaxis(ax,100,1)

# Agregar texto con la fuente específica
from matplotlib.font_manager import FontProperties

font_path = "Yanone_Kaffeesatz/static/YanoneKaffeesatz-Bold.ttf"
font_prop = FontProperties(fname=font_path,weight=100)

texto = '''grupo de supervisión, diagnóstico
y descubrimiento del conocimiento
en procesos de ingeniería'''

ax.text(12,+4.5,'GSDPI',verticalalignment='center', fontsize=40,color='black', fontproperties=font_prop, alpha=1)
ax.text(12,-4.5,texto,  verticalalignment='center', fontsize=20,color='black', fontproperties=font_prop, alpha=1)
ax.axis('scaled')

plt.axis('off')

plt.savefig('logo_para_fondo_blanco.png', transparent=True, dpi=300)




'''
EJEMPLO 3
Figura para fondo negro con el acrónimo del grupo en el centro
'''


fig, ax = plt.subplots(1)
fig.set_size_inches(9,3)

# logo con 100 semillas y c=1
draw_phyllotaxis(ax,100,1)

# Agregar texto con la fuente específica
from matplotlib.font_manager import FontProperties

font_path = "Yanone_Kaffeesatz/static/YanoneKaffeesatz-Bold.ttf"
font_prop = FontProperties(fname=font_path,weight=100)

texto = '''grupo de supervisión, diagnóstico
y descubrimiento del conocimiento
en procesos de ingeniería'''

ax.text(0,0,'GSDPI',verticalalignment='center',horizontalalignment='center', fontsize=50,color='#888888', fontproperties=font_prop, alpha=1)
ax.axis('scaled')

plt.axis('off')

plt.savefig('logo_solo_acronimo.png', transparent=True, dpi=300)









'''
EJEMPLO 2
Figura para fondo negro con el texto del nombre del grupo
'''


fig, ax = plt.subplots(1)
fig.set_size_inches(9,3)

# logo con 100 semillas y c=1
draw_phyllotaxis(ax,100,1)

# Agregar texto con la fuente específica
from matplotlib.font_manager import FontProperties

font_path = "Yanone_Kaffeesatz/static/YanoneKaffeesatz-Bold.ttf"
font_prop = FontProperties(fname=font_path,weight=100)

texto = '''grupo de supervisión, diagnóstico
y descubrimiento del conocimiento
en procesos de ingeniería'''

ax.text(12,+4.5,'GSDPI',verticalalignment='center', fontsize=40,color='lightgray', fontproperties=font_prop, alpha=1)
ax.text(12,-4.5,texto,  verticalalignment='center', fontsize=20,color='lightgray', fontproperties=font_prop, alpha=1)
ax.axis('scaled')

plt.axis('off')

plt.savefig('logo_para_fondo_negro.png', transparent=True, dpi=300)
