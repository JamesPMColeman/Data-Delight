# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# The figure wil be rendered into a static HTML file
output_file('visuals.test_output_file.html',
            title='Empty Bokeh Figure')

# Set up a generic figure() object
fig = figure(
    background_fill_color='gray',
    background_fill_alpha=0.5,
    border_fill_color='blue',
    border_fill_alpha=0.25,
    plot_height=300,
    plot_width=500,
    x_axis_type='datetime',
    x_axis_location='above',
    x_range=('2018-01-01', '2018-06-30'),
    y_axis_type='linear',
    y_axis_location='left',
    y_range=(0, 100),
    title='Example Figure',
    title_location='right',
    toolbar_location='below',
    tools='save'
    )

# Remove gridlines
fig.grid.grid_line_color = 'red'
# view the figure
show(fig)
