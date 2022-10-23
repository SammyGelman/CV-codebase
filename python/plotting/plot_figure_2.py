#!/usr/bin/env python
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
from phase_diagrams.scripts.phase_plotting import plot_phase_diagram
from order_parameters.scripts.mag_time import get_mag
from brokenaxes import brokenaxes
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pgf import FigureCanvasPgf
from matplotlib.ticker import AutoMinorLocator, MaxNLocator
from matplotlib.ticker import LinearLocator, AutoLocator, FixedLocator
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D

# plt.rcParams['legend.handlelength'] = 0
plt.rcParams['legend.numpoints'] = 1


#code from guys plotting scripts
matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)

cm_in_inches = 0.393701
golden_ratio = 1.61803398875

plt.rcParams.update({
    "font.family": "serif",  # use serif/main font for text elements
    "text.usetex": True,     # use inline math for ticks
    "pgf.rcfonts": False,    # don't setup fonts from rc parameters
    "pgf.preamble": "\n".join([
         r"\usepackage{url}",                        # load additional packages
         r"\usepackage{unicode-math}",               # unicode math setup
         r"\setmainfont{DejaVu Serif}",              # serif font via preamble
         r"\usepackage[Symbolsmallscale]{upgreek}",  # Uppercase greek
    ])
})

plt.rc('font', **{'family':'serif', 'serif':['Times'], 'size': 9.0})
plt.rc('lines', linewidth=0.5)
plt.rc('axes', linewidth=0.5)
plt.rc('xtick', labelsize='medium', direction='in')
plt.rc('ytick', labelsize='medium', direction='in')
plt.rc('xtick.major', size=4.0, width=0.5)
plt.rc('xtick.minor', size=2.0, width=0.5)
plt.rc('ytick.major', size=4.0, width=0.5)
plt.rc('ytick.minor', size=2.0, width=0.5)
plt.rc('legend', fontsize='small', loc='best')
plt.rc('text', usetex=True)

#Set fontsize
fs = 9

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure()
# fig = plt.figure(constrained_layout=True)

gs1 = GridSpec(1, 3, figure=fig, wspace=0.0, bottom=0.53)
gs2 = GridSpec(2, 1, figure=fig, wspace=0.0, hspace=0.0, top = 0.45, bottom=0.28)
gs3 = GridSpec(1, 1, figure=fig, wspace=0.0, top = 0.22)

#Phase diagram l16
ax1 = fig.add_subplot(gs1[0,0])
ax1.set_ylabel('H',fontsize=fs)
ax1.tick_params(axis = 'both', labelsize=8)
label='(a)'
# ax1.text(-0.1, 
#          1.35, 
#          label, 
#          transform=ax1.transAxes,
#          fontsize=12, 
#          va='top', 
#          ha='right')
ax1.set_aspect('equal')
t16 = ax1.text(
    3.0, 4.0, "$L=16$", ha="center", va="center", size=8, 
    bbox=dict(boxstyle="round,pad=0.3", fc="white")
)
bb = t16.get_bbox_patch()
bb.set_boxstyle("round",pad=0.3,rounding_size=None)
subplot_1 = plot_phase_diagram(16)

#Phase diagram l32
ax3 = fig.add_subplot(gs1[0,1])
ax3.set_xlabel('T',fontsize=fs,labelpad=2.2)
ax3.get_yaxis().set_visible(False)
ax3.tick_params(axis = 'both', labelsize=8)
ax3.set_aspect('equal')
ax3.set_xticks([2])
t32 = ax3.text(
    3.0, 4.0, "$L=32$", ha="center", va="center", size=8, 
    bbox=dict(boxstyle="round,pad=0.3",fc="white")
)
bb = t16.get_bbox_patch()
bb.set_boxstyle("round",pad=0.3,rounding_size=None)
subplot_2 = plot_phase_diagram(32)

#Phase diagram l64
ax4 = fig.add_subplot(gs1[0,2])
ax4.get_yaxis().set_visible(False)
t64 = ax4.text(
    3.0, 4.0, "$L=64$", ha="center", va="center", size=8, 
    bbox=dict(boxstyle="round,pad=0.3",fc="white")
)
bb = t16.get_bbox_patch()
bb.set_boxstyle("round",pad=0.3,rounding_size=None)
subplot_3 = plot_phase_diagram(64)
ax4.tick_params(axis = 'both', labelsize=8)
ax4.set_aspect('equal')

# Custom legend elements
ms = 3.8
legend_elements = [[Line2D([0], [0], marker='o', color='orange',
                           markersize=3.5, markeredgecolor='black')],
                   [Line2D([0], [0], marker='s', color='orange', 
                           markersize=3.5, markeredgecolor= 'black')],
                   [Line2D([0], [0], marker='d', color='orange', 
                           markersize=ms, markeredgecolor = 'black')
                    ]]

legend_2        = [Line2D([0], [0], color='orange', lw=4), 
                    Line2D([0], [0], color='b', lw=4)]

#stuck
ax5 = fig.add_subplot(gs2[0,0])
ax5.legend(handles=legend_elements[0],handlelength=0,loc='upper right', edgecolor = (1,1,1,0),
                  facecolor = (1,1,1,.50001),
                  framealpha=0
)
mag_dir = 'order_parameters/data/'
time, field, mag = get_mag(mag_dir+'T0.2_H2.0.dat',300)
field = field/2.0
ax5.plot(time, mag)
# ax5.tick_params(axis = 'x', labelsize=6)
ax5.tick_params(axis = 'y', labelsize=8)
ax5.get_xaxis().set_visible(False)
# label='(b)'
# ax5.text(0.0, 
#          1.8,
#          label, 
#          transform=ax5.transAxes,
#          fontsize=12, 
#          va='top', 
#          ha='right')
ax5.plot(time,field,linewidth=0.4)
ax5.set_yticks([-1,0,1])
ax5.set_ylim(-1,1.32)
#linear response
# ax6 = fig.add_subplot(gs2[1,0])
# time, field, mag = get_mag(mag_dir+'/T4.0_H2.0.dat',300)
# ax6.plot(time, mag)
# ax6.plot(time,field,linewidth=0.4)
# ax6.get_xaxis().set_visible(False)
# ax6.get_yaxis().set_visible(False)

#saturated
ax7 = fig.add_subplot(gs2[1,0])
ax7.legend(handles=legend_elements[1],handlelength=0,edgecolor = (1,1,1,0),
                  facecolor = (1,1,1,.50001),
                  framealpha=0
)
ax7.set_ylabel('$h/h_{0}$')
time, field, mag = get_mag(mag_dir+'/T2.0_H2.0.dat',300)
field = field/2.0
ax7.plot(time, mag)
ax7.plot(time,field,linewidth=0.4)
ax7.tick_params(axis = 'x', labelsize=8.0)
ax7.tick_params(axis = 'y', labelsize=8)
# ax7.set_ylim([-3,3])
ax7.set_yticks([-1,0])
ax7.set_ylim(-1.32,1.32)

# chaotic regime

#set limits
a = 0
b = 300
e = 8000
f = 15000

#Plan to get frame to go over brokenaxes object
ax9 = fig.add_subplot(gs3[0,0])
ax9.xaxis.set_visible(False)
ax9.yaxis.set_visible(False)
ax9.spines['top'].set_linewidth(1.5)
ax9.spines['right'].set_linewidth(1.5)

ax8 = brokenaxes(
    xlims = [(a,b),(e,f)],
    ylims = [(-1.2,1.2)],
    subplot_spec = gs3[0, 0],
    wspace = 0.02,
    width_ratios=[3, 5]
)

time, field, mag = get_mag(mag_dir+'T1.2_H1.1.dat',f)

#Normalize magnetic field strength
field = field/1.1

ax8.plot(time, mag, label='$M$')

ax8.axs[0].plot(time, field, color='orange', label= '$\mathrm{h/h_0}$', linewidth=0.8)
ax8.tick_params(axis = 'y', labelsize=7.5)
ax8.tick_params(axis = 'x', labelsize=8)
# ax8.axs[0].spines["top"].set_color("black")
# ax8.axs[1].spines["top"].set_color("black")

ax8.axs[0].set_xticks([0,100,200])
ax8.axs[1].set_xticks([8000,11000,14000])
ax8.set_xlabel('t',labelpad=5,fontsize=fs)

ax8.axs[1].legend(handles = legend_elements[2], 
                  handlelength = 0, 
                  loc='upper right',
                  edgecolor = (1,1,1,0),
                  facecolor = (1,1,1,.50001),
                  framealpha=0
                  )

legend = ax8.legend(loc='lower right',bbox_to_anchor=(0.9,-0.13))
legend.get_frame().set_alpha(None)
legend.get_frame().set_facecolor((1, 1, 1, 0.3))

#set figure size
width_inches = 8.6 * cm_in_inches
fig.default_height = width_inches / golden_ratio
height_inches = fig.default_height * 1.5
fig.set_size_inches(width_inches, height_inches)

# plt.savefig('../saved_figures/figure_2.pdf',bbox_inches='tight',pad_inches=0)
plt.savefig('../saved_figures/figure_2.pdf', dpi=400)
plt.show()
