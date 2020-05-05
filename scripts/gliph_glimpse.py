# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# Create a coordinate set
x = [1, 2, 1]
y = [1, 1, 2]

# Output the fisualization
output_file('visuals.first_glyphs.html', title='First Glyphs')

# Create the figure 
fig = figure(title='My Coordinates',
			 plot_height=300, 
			 plot_width=300,
			 x_range=(0, 3), y_range=(0, 3),
			 toolbar_location=None)

# Create glyphs
fig.circle(x=x, y=y, color='green',
		   size=10, alpha=0.5)

show(fig)