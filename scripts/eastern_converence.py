from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter


from read_nba_data import standings


output_file(
    'east_top_2_standings_race.html',
    title='Eastern Conference Top 2 Teams Wins'
    )

# Isolate the Rockets and the Warriors
standings_data = ColumnDataSource(standings)

# Create ColumnDataSources
celtics_view = CDSView(source=standings_data,
                       filters=[GroupFilter(column_name='teamAbbr',
                                            group='BOS')])
raptors_view = CDSView(source=standings_data,
                       filters=[GroupFilter(column_name='teamAbbr',
                                            group='TOR')])

# Create figure
east_fig = figure(
    x_axis_type='datetime',
    plot_height=300,
    plot_width=600,
    title='Eastern Conference Top 2 Teams Wins',
    toolbar_location=None
    )

# Render specs
east_fig.step(
    'stDate',
    'gameWon',
    color='#007A33',
    legend_label='Celtics',
    source=standings_data,
    view=celtics_view
    )

east_fig.step(
    'stDate',
    'gameWon',
    color='#CE1141',
    legend_label='Toronto',
    source=standings_data,
    view=raptors_view)

east_fig.legend.location = 'top_left'

show(east_fig)
