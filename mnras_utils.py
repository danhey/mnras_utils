import matplotlib
import numpy as np

matplotlib.rcParams["font.size"] = 6
matplotlib.rcParams["savefig.pad_inches"] = 0
matplotlib.rcParams["savefig.bbox"] = 'tight'

def mnras_size(cols=1, square=False):
    if cols==1:
        fig_width_pt = 240.
    else:
        fig_width_pt = 504.
    #Paper width = 504  for 2 columns
    #Col width = 240.0    #for single column
    inches_per_pt = 1.0/72.00              # Convert pt to inches
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Most aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # Figure width in inches
    if square:
        fig_height = fig_width
    else:
        fig_height = fig_width*golden_mean
    fig_size = [fig_width,fig_height]
    return fig_size