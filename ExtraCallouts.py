# Extra callouts for chartify plots

import chartify
import numpy as np

def custom_callouts(chart, custom_callout, xs, ys, labels, colors, legend=True, label_text=False, sizes=None,
                      alphas=None, text_offset=0.0005):
    assert len(xs) == len(ys), 'x and y lengths must be the same'
    assert len(xs) == len(labels), 'length of data categories and labels must be the same'
    assert len(xs) == len(colors), 'length of data categories and colors must be the same'
    if alphas:
        assert len(alphas) == len(xs), 'length of alphas must be the same as data'
    else:
        alphas = np.full(len(xs), 1)
    if sizes:
         assert len(sizes) == len(xs), 'length of sizes must be the same as data'
    else:
        sizes = np.full(len(xs), 10)
    # Adding callouts to plot
    for i in range(len(xs)):
        label = None
        if legend:
            label = labels[i]
        if len(np.shape(xs)) == 2:
            for j, x in enumerate(xs[i]):
                if label_text:
                    chart.callout.text(labels[i], x, ys[i][j] + text_offset)
                custom_callout(x , ys[i][j], size=sizes[i], color=colors[i],
                                    alpha=alphas[i], legend_label=label)
        else:
            if label_text:
                chart.callout.text(labels[i], x, ys[i] + text_offset, text_font='helvetica')
            custom_callout(x , ys[i], size=sizes[i], color=colors[i],
                                    alpha=alphas[i], legend_label=label)