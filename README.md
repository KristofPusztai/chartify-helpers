# chartify-helpers
Some lightweight helper functions which add readability/functionality to Spotify's [chartify](https://github.com/spotify/chartify) library

## Installation:
via pip:

```
pip install chartify-helpers
```

via github:

```
git clone
```

navigate to cloned directory and run setup.py

```
sudo python setup.py install
```
## Usage:

### Custom Callouts:

Method:

```python
custom_callouts(chart, custom_callout, xs, ys, 
	        labels, colors, legend=True, label_text=False,
		sizes=None, alphas=None, text_offset=0.0005)
```

```python
import chartify
from ExtraCallouts import custom_callouts

# Generate example data
data = chartify.examples.example_data()

# Sum price grouped by date
price_by_date = (
    data.groupby('date')['total_price'].sum()
    .reset_index()  # Move 'date' from index to column
    )
# Plot the data
ch = chartify.Chart(blank_labels=True, x_axis_type='datetime')
ch.set_title("Line charts")
ch.set_subtitle("Custom Callouts")
ch.plot.line(
    # Data must be sorted by x column
    data_frame=price_by_date.sort_values('date'),
    x_column='date',
    y_column='total_price')

# Diamond Callout
custom_callouts(ch, ch.figure.diamond, 
                [[price_by_date['date'][54]]], [[price_by_date['total_price'][54]]], 
                ['diamond callout'], ['orange'], 
                legend=True, label_text=True, sizes=[10],alphas=[1], text_offset=0.3)
# Circular Callout
custom_callouts(ch, ch.figure.circle, 
                [[price_by_date['date'][103]]], [[price_by_date['total_price'][103]]], 
                ['circular callout'], ['green'], 
                legend=True, label_text=True, sizes=[10],alphas=[1], text_offset=0.3)
# Square Callout
custom_callouts(ch, ch.figure.square, 
                [[price_by_date['date'][146]]], [[price_by_date['total_price'][146]]], 
                ['square callout'], ['red'], 
                legend=True, label_text=True, sizes=[10],alphas=[1], text_offset=0.3)
```
 ![alt text](https://github.com/KristofPusztai/chartify-helpers/blob/main/custom_callouts.png)
 
 More callout styles found [here](https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html)
 
### Stacked Bar Chart Top Labels:

Method:

```python
add_stacked_label(chart, categories, labels, y , colors=None, sizes='10pt')
```

```python
# Generate example data
data = chartify.examples.example_data()

quantity_by_fruit_and_country = (data.groupby(
    ['fruit', 'country'])['quantity'].sum().reset_index())

# Plot the data
ch = chartify.Chart(blank_labels=True,
                x_axis_type='categorical')
ch.set_title("Stacked bar chart")
ch.set_subtitle("Stack columns by a categorical factor, with top labels")
ch.plot.bar_stacked(
     data_frame=quantity_by_fruit_and_country,
     categorical_columns=['fruit'],
     numeric_column='quantity',
     stack_column='country',
     normalize=False)
ch.set_legend_location('top_right')

# Adding numerical labels above each bar
add_stacked_label(ch,data.groupby('fruit').sum()['quantity'].index,
data.groupby('fruit').sum()['quantity'].values, 
data.groupby('fruit').sum()['quantity'].values)

ch.show('png')
```
 ![alt text](https://github.com/KristofPusztai/chartify-helpers/blob/main/stackedbar_label.png)
