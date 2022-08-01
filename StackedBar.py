# Adding numerical labels to bar charts

import numpy as np

def add_stacked_label(chart, categories, labels, y , colors=None, sizes='10pt'):
    assert len(categories) == len(labels), 'categories must be the same length as labels'
    if colors:
        assert len(colors) == len(categories), 'colors must be the same length as categories'
    else:
        colors = np.full(len(categories),'black')
    if isinstance(sizes, str):
        sizes = np.full(len(categories), sizes)
    else:
        assert len(sizes) == len(categories), 'size array must be same length as categories'

    data = chart.data[0]
    for i in range(len(categories)):
        chart.callout.text(labels[i], categories[i], y[i],
                           text_color=colors[i], text_align='center', font_size=sizes[i])
