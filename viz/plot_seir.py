import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple

def plot_results(infected: np.ndarray[np.float64],
                 *,
                 figsize:Tuple[int, int]=(10, 6),
                 color:str='#AA0000',
                 linestyle:str='dashed',
                 marker:str='o',
                 xlabel:str='Day',
                 ylabel:str='Number of Infected Cases',
                 title:str='Simulated Outbreak') -> plt.Figure:
    """Plots the time series of infected cases."""
    
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.plot(infected, color=color, linestyle=linestyle, marker=marker)
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.set_title(title, fontsize=20)
    ax.grid(alpha=0.2)
    return fig
