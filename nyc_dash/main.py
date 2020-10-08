from bokeh.io import output_file, show, curdoc
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models.widgets import Dropdown

x = list(range(11))
y0 = x

# create three plots
s1 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s1.circle(x, y0, size=12, color="#53777a", alpha=0.8)

menu=[("ZIP1", "zip1"), ("ZIP2", "zip2")]
dropdown1=Dropdown(label="Zipcode 1", button_type="danger", menu=menu)
dropdown2 = Dropdown(label="Zipcode 2", button_type="danger", menu=menu)


curdoc().add_root(column(dropdown1, dropdown2, s1))
