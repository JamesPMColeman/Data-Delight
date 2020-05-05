# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# The figure wil be rendered into a static HTML file
output_file('visuals/test_output_file.html',
			title='Empty Bokeh Figure')

# Set up a generic figure() object
fig = figure()

# view the figure
show(fig)