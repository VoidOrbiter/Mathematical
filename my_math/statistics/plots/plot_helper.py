import numpy as np
import plotly.graph_objects as go
import scipy.stats as stats

def create_descriptive_plot(figure, data):
    figure.clear()
    ax = figure.add_subplot(111)
    ax.set_facecolor('#1e1e1e')

    ax.set_title("Interquartile Range (IQR) Distribution", 
                 color='white', 
                 fontsize=12, 
                 fontweight='bold', 
                 pad=15)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    bp = ax.boxplot(data, vert=False, patch_artist=True, widths=0.5)

    for box in bp['boxes']:
        box.set(color='#3498db', linewidth=2)
        box.set(facecolor='#2980b9')

    ax.axvline(q1, color='#e74c3c', linestyle='--', alpha=0.6, label=f'Q1: {q1:.2f}')
    ax.axvline(q3, color='#e74c3c', linestyle='--', alpha=0.6, label=f'Q3: {q3:.2f}')

    for median in bp['medians']:
        median.set(color='#f1c40f', linewidth=3)

    ax.tick_params(colors='white', labelsize=8)
    for spine in ax.spines.values():
        spine.set_color('#3d3d3d')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.xaxis.grid(True, linestyle=':', alpha=0.3, color='white')
    
    return figure

def skewness_plot(figure, data, color="#109618"):
    figure.clear()
    ax = figure.add_subplot(111)
    ax.clear()
    ax.set_title("Skewness", 
                 color='white', 
                 fontsize=12, 
                 fontweight='bold', 
                 pad=15)
    
    kde = stats.gaussian_kde(data)
    x_range = np.linspace(min(data), max(data), 200)
    ax.plot(x_range, kde(x_range), color="#ecf0f1", linewidth=2)

    # Styling for your Dark Theme
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='#7f8c8d')
    ax.spines['bottom'].set_color('#3d3d3d')
    ax.spines['left'].set_color('#3d3d3d')
    ax.xaxis.label.set_color('#7f8c8d')
    ax.yaxis.label.set_color('#7f8c8d')