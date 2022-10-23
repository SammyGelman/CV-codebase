#!/usr/bin/env python
import matplotlib
import numpy as np
from  matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.lines as mlines
from contours.scripts.contour_plot import contour
from contours.scripts.time_mag import time_mag
from contours.scripts.plot_ent_mag_for_T import ent_mag_for_T
from matplotlib.backends.backend_pgf import FigureCanvasPgf
from matplotlib.ticker import AutoMinorLocator, MaxNLocator
from matplotlib.ticker import LinearLocator, AutoLocator, FixedLocator
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

plt.rcParams['legend.handlelength'] = 0
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

fs = 9

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(constrained_layout=True)

gs = GridSpec(13, 15, figure=fig)

#Entropy_time l32
ax1 = fig.add_subplot(gs[0:5, 0:7])
ax1.set_ylabel('T',labelpad=2.8,fontsize=fs)
ax1.set_xlabel('t',labelpad=0.5,fontsize=fs)
ax1.set_title('S', fontsize=fs)
ax1.set_yticks([0.2,0.6,1.0])
subplot_1 = contour('ent',True)
ax1.set_rasterization_zorder(-1)

axins = inset_axes(ax1,
                   width="5%",  # width = 5% of parent_bbox width
                   height="100%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1),
                   bbox_transform=ax1.transAxes,
                   borderpad=0,
                   )


color_bar = plt.colorbar(subplot_1, cax=axins)
cbytick_obj = plt.getp(color_bar.ax.axes, 'yticklabels')
plt.setp(cbytick_obj, color='black')
tick_locator = MaxNLocator(nbins=5)
color_bar.locator = tick_locator
color_bar.ax.tick_params(labelsize=8)
color_bar.update_ticks()

#mag_time l32
ax2 = fig.add_subplot(gs[0:5, 9:15],sharey=ax1)
ax2.get_yaxis().set_visible(False)
ax2.set_title('M', fontsize=fs)
ax2.set_xlabel('t',labelpad=0.5,fontsize=fs)
subplot_2 = contour('mag', False, cmap='seismic')
ax2.set_rasterization_zorder(-1)

axins = inset_axes(ax2,
                   width="5%",  # width = 5% of parent_bbox width
                   height="100%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1),
                   bbox_transform=ax2.transAxes,
                   borderpad=0,
                   )

color_bar = plt.colorbar(subplot_2, cax=axins, ticks=[-0.8,-0.4,0.0,0.4,0.8])
cbytick_obj = plt.getp(color_bar.ax.axes, 'yticklabels')
plt.setp(cbytick_obj, color='black')
# tick_locator = MaxNLocator(nbins=5)
# color_bar.locator = tick_locator
color_bar.ax.tick_params(labelsize=6)
color_bar.ax.set_yticklabels(['textsuperscript{-0.8}','/N{MINUS SIGN}'+'0.4','0.0', '0.4', '0.8'])
color_bar.update_ticks()

#predictable region
ax3 = fig.add_subplot(gs[7:10, 0:])
ax3.set_ylim([0.0,0.65])
temp_1 = 0.8
ent, mag , err, time = ent_mag_for_T(temp_1)

ax3.errorbar(time,ent,yerr=err)
# ax3.text(39.0, 0.45, f"$T={temp_1}$", bbox=dict(boxstyle="round", fc='white'))
ax3.get_xaxis().set_visible(False)
ax3.tick_params(axis='y', colors='tab:blue')
ax3.yaxis.label.set_color('tab:blue')
ax3.set_ylabel('S', labelpad=0.7, fontsize=fs, loc="bottom")
ax3.text(0.0, 0.48, f"$T={temp_1}$")
# label='(c)'
# ax3.text(-0.1,
#          1.15,
#          label,
#          transform=ax3.transAxes,
#          fontsize=12,
#          va='top',
#          ha='right')
ax4 = ax3.twinx()
ax4.plot(time,mag,'r',linewidth='0.6')
ax4.plot(time,np.zeros((len(time)),),'r',linestyle='dashed',alpha=0.5,linewidth='0.6')
ax4.set_ylim([-1.1,1.5])
ax4.get_xaxis().set_visible(False)
ax4.tick_params(axis='y', colors='r')
ax4.yaxis.label.set_color('red')
ax4.set_ylabel('M',labelpad=0.2,fontsize=fs,loc="bottom")

#chaotic region
ax5 = fig.add_subplot(gs[10:13, 0:],sharex=ax3)
ax5.set_ylim([0.0,0.15])
temp_2 = 0.38
ent, mag , err, time = ent_mag_for_T(temp_2)
ax5.errorbar(time,ent,yerr=err,label='$T='+str(temp_2)+'$')

#Two lines with different colors and axis labels on different sides
# ax5.text(39.0, 0.1, f"$T={temp_2}$", bbox=dict(boxstyle="round", fc='white'))
ax5.text(0.0, 0.11, f"$T={temp_2}$")
ax5.tick_params(axis='y', colors='tab:blue')
plt.setp(ax3.get_xticklabels(), visible=False)
ax5.yaxis.label.set_color('tab:blue')
# ax5.set_ylabel('S')

#make label
label='(d)'
# ax5.text(-0.1,
#          1.15,
#          label,
#          transform=ax5.transAxes,
#          fontsize=12,
#          va='top',
#          ha='right')
ax6 = ax5.twinx()
ax6.set_ylim([-0.2,0.29])
ax6.set_yticks([-0.25,0.0,0.2])
ax6.plot(time,mag,'r',linewidth='0.6')
ax6.tick_params(axis='y', colors='r')
ax6.yaxis.label.set_color('red')
ax5.set_xlabel('t',labelpad=0.1,fontsize=fs)
ax6.plot(time,np.zeros((len(time)),),'r',linestyle='dashed',alpha=0.5,linewidth='0.6')
# ax6.set_ylabel('M')

# fig.tight_layout()
# format_axes(fig)

#remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)

#set figure size
width_inches = 8.6 * cm_in_inches
fig.default_height = width_inches / golden_ratio * 1.5
height_inches = fig.default_height
fig.set_size_inches(width_inches, height_inches)


plt.savefig('../saved_figures/figure_3.pdf', dpi=400)
# plt.show()
