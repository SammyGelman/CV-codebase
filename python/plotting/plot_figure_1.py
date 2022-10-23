#!/usr/bin/env python
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
# from entropy_temperature.scripts.plot_delta_S import plot_delta_S
from entropy_temperature.scripts.plot_delta_S import plot_delta_S
from entropy_temperature.scripts.plot_temp_delta_S import plot_error
from entropy_temperature.scripts.plot_T_ent import plot_T_S
from samples.scripts.play_test import *
from matplotlib.backends.backend_pgf import FigureCanvasPgf
from matplotlib.ticker import AutoMinorLocator, MaxNLocator
from matplotlib.ticker import LinearLocator, AutoLocator, FixedLocator
from matplotlib.colors import LinearSegmentedColormap

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

fs = 9

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure()

#make nested objects
gs1 = gridspec.GridSpec(4, 2)
gs2 = gridspec.GridSpec(4, 2)
gs3 = gridspec.GridSpec(4, 2)

zorder = -5

#T0.5 - real
ax2 = fig.add_subplot(gs2[0, 0])
ax2.xaxis.set_ticks([])
ax2.set_xlabel('T=0.5',fontsize=(fs-1.5), labelpad=1.8)
ax2.yaxis.set_visible(False)
ax2.set_title('Real ',fontsize=7.5)
ax2.imshow(mc_samples(0.5), interpolation='nearest', rasterized=True)

#T0.5 - synthetic
ax3 = fig.add_subplot(gs2[0, 1])
ax3.set_title(' Synthetic',fontsize=7.3)
ax3.imshow(gen_samples(0.5), interpolation='nearest', rasterized=True)

ax3.xaxis.set_visible(False)
ax3.yaxis.set_visible(False)

#T1.5 - real
ax4 = fig.add_subplot(gs2[1, 0])
ax4.imshow(mc_samples(1.5), interpolation='nearest', rasterized=True)

ax4.xaxis.set_ticks([])
ax4.set_xlabel('T=1.5',fontsize=(fs-1.5), labelpad=1.8)
ax4.yaxis.set_visible(False)

#T1.5 - synthetic
ax5 = fig.add_subplot(gs2[1, 1])
ax5.imshow(gen_samples(1.5), interpolation='nearest', rasterized=True)

ax5.xaxis.set_visible(False)
ax5.yaxis.set_visible(False)

#T2.5 - real
ax7 = fig.add_subplot(gs2[2, 0])
ax7.imshow(mc_samples(2.5), interpolation='nearest', rasterized=True)

ax7.xaxis.set_ticks([])
ax7.set_xlabel('T=2.5',fontsize=(fs-1.5), labelpad=1.8)
ax7.yaxis.set_visible(False)

#T2.5 - synthetic
ax8 = fig.add_subplot(gs2[2, 1])
ax8.imshow(gen_samples(2.5), interpolation='nearest', rasterized=True)

ax8.xaxis.set_visible(False)
ax8.yaxis.set_visible(False)

#T4.5 - real
ax9 = fig.add_subplot(gs2[3, 0])
ax9.imshow(mc_samples(4.5), interpolation='nearest', rasterized=True)

ax9.xaxis.set_ticks([])
ax9.set_xlabel('T=4.5',fontsize=(fs-1.5), labelpad=1.8)
ax9.yaxis.set_visible(False)

#T4.5 - synthetic
ax10 = fig.add_subplot(gs2[3, 1])
ax10.imshow(gen_samples(4.5), interpolation='nearest', rasterized=True)

ax10.xaxis.set_visible(False)
ax10.yaxis.set_visible(False)




#delta S, T for different sample sizes
ax1 = fig.add_subplot(gs1[0:2, 0:2])
ax1.set_ylabel(r'$\Delta S$',labelpad=0.5,fontsize=fs)
ax1.set_xlabel("T",fontsize=fs)
ax1.xaxis.set_label_coords(0.52,-0.056)
subplot_1 = plot_error()

#mean delta S for different system sizes
ax6 = fig.add_subplot(gs3[2:4, 0:2])
ax6.set_ylabel(r'$\left<\Delta S\right>$',labelpad=0.5,fontsize=fs)
ax6.set_xlabel("L",labelpad=.001,fontsize=fs)
ax6.xaxis.set_label_coords(0.5,-0.1)
subplot_6 = plot_delta_S()

gs1.update(right=0.69)
gs3.update(right=0.69,top=0.75)
gs2.update(left=0.7,bottom=0.08,top=0.91)

gs2.update(hspace=.0,wspace=.2)
gs1.update(hspace=.0)
gs1.update(hspace=.0,wspace=.0)

#set figure size
width_inches = 8.6 * cm_in_inches
fig.default_height = width_inches / golden_ratio
height_inches = fig.default_height
fig.set_size_inches(width_inches, height_inches)


plt.savefig('../saved_figures/figure_1.pdf', dpi=400)
plt.show()
