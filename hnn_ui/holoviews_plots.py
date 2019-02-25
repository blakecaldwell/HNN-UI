import numpy as np
from bokeh.resources import CDN
from bokeh.embed import file_html
import holoviews as hv
hv.extension('bokeh')


def get_dipole():
    x = np.linspace(0, 4*np.pi, 100)
    y = np.sin(x)

    scatter1 = hv.Scatter((x, y), label='sin(x)')
    scatter2 = hv.Scatter((x, y*2), label='2*sin(x)').opts(color='orange')
    scatter3 = hv.Scatter((x, y*3), label='3*sin(x)').opts(color='green')
    scatter4 = hv.Scatter(scatter3).opts(line_color='green', marker='square', fill_alpha=0, size=5)

    curve1 = hv.Curve(scatter1)
    curve2 = hv.Curve(scatter2).opts(line_dash=(4, 4), color='orange')
    curve3 = hv.Curve(scatter3).opts(color='orange')

    example = scatter1 *  curve1 * curve2 * scatter4 * curve3

    example.relabel("Dipole Dummy Example")
    
    renderer = hv.renderer('bokeh')
    hvplot = renderer.get_plot(example)
    html = renderer._figure_data(hvplot)
    return html