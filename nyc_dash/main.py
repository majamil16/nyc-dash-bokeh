from bokeh.io import output_file, show, curdoc
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models.widgets import Dropdown
from bokeh.models import ColumnDataSource
from src import data_analysis as da
import os

FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(FILE_DIR, 'data', '2020_closed_nyc_311.csv')
#build the dataframe ONCE so that we can query it many times for updates.
data, zips = da.construct_df(DATA_PATH)
x = list(range(9)) # ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug","sep"] # x axis months
# the y-values will depend on the zip code you choose
#print(x)
menu = list(zips)

# the y-values of all the year data
plot_year = list(da.query_zip(data).values.flatten())
#print(plot_year)

f = figure(title="NYC Info")
#f.line(x, plot_year)

drop1 = Dropdown(label="Zipcode 1", button_type="danger", menu=menu)
drop2 = Dropdown(label="Zipcode 2", button_type="danger", menu=menu)

def handler(event):
    print(event.item)

clicked_zip1 = drop1.on_click(handler)
clicked_zip2 = drop2.on_click(handler)

#zip1 = list(da.query_zip(data, clicked_zip1).values.flatten())
#zip2 = list(da.query_zip(data, clicked_zip2).values.flatten())
#print(zip1)
#print(zip2)
# set the source to specific columns initially

zip1 = list(da.query_zip(data, zip_code='10001' ).values.flatten())
zip2 = list(da.query_zip(data,zip_code="10002").values.flatten())


colsource = {'x_vals':x,
        "yearly": plot_year,
        "selected_zip1":zip1,
        "selected_zip2":zip2

        }


source = ColumnDataSource(colsource)



#def update_plot():
#    source.data.update('selected_zip1': clicked_zip1, "selected_zip2": clicked_zip2)

#clicked1.onclick(update plot)

#f.multi_line([x,x,x],[plot_year, zip1, zip2])
f.line('x_vals', 'yearly', source=source)
f.line('x_vals', 'selected_zip1', source=source)
f.line('x_vals', 'selected_zip2', source=source)
curdoc().add_root(column(drop1, drop2, f))

"""
x = list(range(11))
y0 = x

# create three plots
s1 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s1.circle(x, y0, size=12, color="#53777a", alpha=0.8)

menu=[("ZIP1", "zip1"), ("ZIP2", "zip2")]
dropdown1=Dropdown(label="Zipcode 1", button_type="danger", menu=menu)
dropdown2 = Dropdown(label="Zipcode 2", button_type="danger", menu=menu)


curdoc().add_root(column(dropdown1, dropdown2, s1))
"""
