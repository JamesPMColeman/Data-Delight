import numpy as np
from bokeh.io import output_file
from bokeh.plotting import show, figure


# Word count data
day_number = np.linspace(1, 10, 10)
daily_words = [450, 628, 488, 210, 791,508,639,397,943]
cumulative_words = np.cumsum(daily_words)

# Output
output_file('visuals.progress.html', title='My Progress')

# Create the data figure
fig = figure(title='My Progress',
			 plot_height=400,
			 plot_width=700,
			 x_minor_ticks=2,
			 y_range=(0, 6000),
			 toolbar_location=None)

# Vertical bar representing words
fig.vbar(x=day_number,
		 bottom=0,
		 top=daily_words,
		 color='blue',
		 width=0.75,
		 legend='Daily')

# Accumulation of words over time
fig.line(x=day_number,
		 y=cumulative_words,
		 color='red',
		 line_width=1,
		 legend='Cumulative')

# Add the legend
fig.legend.location = 'top_left'

show(fig)