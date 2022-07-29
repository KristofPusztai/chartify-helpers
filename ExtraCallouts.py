#Extra callouts for chartify plots

import chartify
import numpy as np

def circular_callouts(chart, x, y, labels, colors, legend=True, label_text=False, sizes=None, alphas=None):
    assert len(x) == len(y), 'x and y lengths must be the same'
    assert len(x) == len(labels), 'length of data categories and labels must be the same'
    assert len(x) == len(colors), 'length of data categories and colors must be the same'
    if alphas:
        assert len(alphas) == len(x), 'length of alphas must be the same as data'
    else:
        alphas = np.full(len(x), 1)
    if sizes:
         assert len(sizes) == len(x), 'length of sizes must be the same as data'
    else:
        sizes = np.full(len(x), 10)
    # Adding callouts to plot
    for points in range(len(x)):
        if legend:
            chart.figure.circle(x[i] , y[i], size=sizes[i], color=colors[i],
                             alpha=alphas[i], legend_label=labels[i])
        elif label_text:
            ch.callout.text(labels[i], x[i], y[i] + 0.0005*sizes[i]*y[i])
        else:
            chart.figure.circle(x[i] , y[i], size=sizes[i], color=colors[i],
                             alpha=alphas[i])


def square_callouts(chart, x, y, labels, colors, legend=None, label_text=None):
    #TODO
