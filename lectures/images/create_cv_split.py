"""
Create graph illustrating split into training/validation/test samples
for CV.

"""

import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle

heading = dict(fontfamily='serif', fontsize='large', fontstyle='italic')

fig, ax = plt.subplots(1, 1, figsize=(7,5.5), constrained_layout=True)

Kfolds = 5

frac_train = 0.8
frac_test = 1.0 - frac_train
hspace = 0.01
vspace = 0.01
yoffset = 0.0
rectheight = 0.05
height = rectheight
textheight = 0.075

color_general = 'whitesmoke'
color_train = 'lightsteelblue'
color_validate = 'gold'
color_test = 'darkorange'

def add_rect_label(ax, xy, width, height, text, **kwargs):
    rct = Rectangle(xy, width=width, height=height, 
        edgecolor='black', lw=1.0, zorder=-10, **kwargs)
    
    ax.add_patch(rct)

    x = xy[0] + width/2.0
    y = xy[1] + height/2.0
    ax.text(x, y, text, va='center', ha='center', fontfamily='serif', 
        fontsize='medium')

add_rect_label(ax, (0.0, yoffset-height), width=1.0, height=height, 
    facecolor=color_general, text='All data')

yoffset -= height
height = textheight

ax.text(frac_train/2.0, yoffset - height/2.0, 'Find (hyper)parameters', 
    va='center', ha='center', **heading)

# Training data
yoffset -= height + vspace
height = rectheight

add_rect_label(ax, (0.0, yoffset-height), width=frac_train, height=height,
    text='Training sample', facecolor=color_train)

yoffset -= height + vspace
height = textheight

ax.text(frac_train/2.0, yoffset - height/2.0, 'Partition into folds', 
    va='center', ha='center', **heading)

yoffset -= height + vspace
height = rectheight

xoffset = 0.0

width = (frac_train - (Kfolds - 1) * hspace) / Kfolds

for k in range(Kfolds):
    add_rect_label(ax, (xoffset, yoffset - height), width=width, height=height,
        text=f'Fold {k+1}', facecolor='gainsboro')
    xoffset += width + hspace

yoffset -= height + vspace
height = textheight

ax.text(frac_train/2.0, yoffset - height/2.0, 'Cross-validation', 
    va='center', ha='center', **heading)

for j in range(Kfolds):

    yoffset -= height + vspace
    height = rectheight
    xoffset = 0.0

    ax.text(-0.02, yoffset - height/2.0, f'Split {j+1}', va='center', 
        ha='right', **heading)

    for k in range(Kfolds):
        color = color_validate if j == k else color_train
        add_rect_label(ax, (xoffset, yoffset - height), width=width, height=height,
            text=f'Fold {k+1}', facecolor=color)
        xoffset += width + hspace


yoffset -= height + vspace
height = textheight

ax.text(1.0 - frac_test + frac_test/2.0, yoffset - height/2.0, 'Evaluation', 
    va='center', ha='center', **heading)

yoffset -= height + vspace
height = rectheight

add_rect_label(ax, (frac_train, yoffset - height/2.0), width=frac_test, 
    height=height, text='Test data', facecolor=color_test)

bottom = yoffset - height / 2.0

ax.plot([frac_train, frac_train], [-rectheight, bottom], zorder=-100,
    lw=0.65, ls=':', color='black')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_ylabel('')
ax.set_xlabel('')
ax.tick_params(bottom=False, left=False)
ax.set_frame_on(False)
ax.grid(None)

ax.set_xlim((-0.01, 1.01))
ax.set_ylim((bottom - 0.01, 0.01))

fig.savefig('lectures/images/cv_split.pdf')
fig.savefig('lectures/images/cv_split.svg')