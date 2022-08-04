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
### stacked bar chart labels:

```python
# Generate example data
data = chartify.examples.example_data()

# Sum price grouped by date
price_by_date = (
    data.groupby('date')['total_price'].sum()
    .reset_index()  # Move 'date' from index to column
    )
print(price_by_date.head())
# Circular Callout
ch = chartify.Chart(blank_labels=True, x_axis_type='datetime')
ch.set_title("Line charts")
ch.set_subtitle("Custom Callouts")
ch.plot.line(
    # Data must be sorted by x column
    data_frame=price_by_date.sort_values('date'),
    x_column='date',
    y_column='total_price')
custom_callouts(ch, ch.figure.diamond, 
                [[price_by_date['date'][54]]], [[price_by_date['total_price'][54]]], 
                ['diamond callout'], ['orange'], 
                legend=True, label_text=True, sizes=[10],alphas=[1], text_offset=0.3)
custom_callouts(ch, ch.figure.circle, 
                [[price_by_date['date'][103]]], [[price_by_date['total_price'][103]]], 
                ['circular callout'], ['green'], 
                legend=True, label_text=True, sizes=[10],alphas=[1], text_offset=0.3)
custom_callouts(ch, ch.figure.square, 
                [[price_by_date['date'][146]]], [[price_by_date['total_price'][146]]], 
                ['square callout'], ['red'], 
                legend=True, label_text=True, sizes=[10],alphas=[1], text_offset=0.3)
ch.show('png')
```
 ![alt text](https://github.com/KristofPusztai/chartify-helpers/blob/main/custom_callouts.png)

