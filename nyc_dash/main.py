from bokeh.io import output_file, show, curdoc
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models.widgets import Dropdown, Select
from bokeh.models import ColumnDataSource
from bokeh.palettes import mpl # get nice colors
from src import data_analysis as da
import os

FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(FILE_DIR, 'data', '2020_closed_nyc_311.csv')
#build the dataframe ONCE so that we can query it many times for updates.
data, zips = da.construct_df(DATA_PATH)

#might need to get rid of this line
data.index.set_levels(['jan', 'feb', 'mar', 'apr','may', 'jun' ,'jul','aug','sep'],level=0,inplace=True)

x = list(range(9)) # ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug","sep"] # x axis months
# the y-values will depend on the zip code you choose
menu = list(zips)

# the y-values of all the year data
plot_year = list(da.query_zip(data).values.flatten())
#print(plot_year)

f = figure(title="NYC 311 Service Response Time", x_axis_label='month', y_axis_label='avg. response time (hours)')
#f.line(x, plot_year)

drop1 = Dropdown(label="Zipcode 1", button_type="danger", menu=menu)
drop2 = Dropdown(label="Zipcode 2", button_type="danger", menu=menu)



def handler1(event):
    update_plot1(event.item)

def handler2(event):
    update_plot2(event.item)

# set the source to specific columns initially
zip1 = list(da.query_zip(data, zip_code='10001' ).values.flatten())
zip2 = list(da.query_zip(data,zip_code="10002").values.flatten())


colsource = {'x_vals':x,
        "yearly": plot_year,
        "selected_zip1":zip1,
        "selected_zip2":zip2

        }


source = ColumnDataSource(colsource)

colorpal = mpl['Plasma'][3]
year_line = f.line('x_vals', 'yearly', line_color = colorpal[0], source=source, name='year_line', legend_label="2020 average",line_width=5)
z1_line = f.line('x_vals', 'selected_zip1', line_color=colorpal[1],source=source, name='z1_line', legend_label="Zipcode 1",line_width=5)
z2_line = f.line('x_vals', 'selected_zip2', line_color=colorpal[2],source=source, name='z2_line', legend_label="Zipcode 2",line_width=5)

#update the plot with newly clicked data from the dropdown
def update_plot1(new):
    new_zip_vals = list(da.query_zip(data, zip_code=new ).values.flatten())
    source.data.update({"selected_zip1":new_zip_vals}) # update the thing w the new value
    z1_line = f.select_one({'name':'z1_line'})
    z1_line.data_source.data = dict(source.data)
    print("HERE")

def update_plot2(new):
    new_zip_vals = list(da.query_zip(data, zip_code=new ).values.flatten())
    source.data.update({'selected_zip2':new_zip_vals}) # update the selected zip2 w the new value
    z2_line = f.select_one({'name':'z2_line'})
    z2_line.data_source.data = dict(source.data)
    print("zip2")

#when either drop1 or drop2 are clicked, update the plot
drop1.on_click(handler1)
drop2.on_click(handler2)

f.legend.location = 'top_right'


curdoc().add_root(column(drop1, drop2, f))

