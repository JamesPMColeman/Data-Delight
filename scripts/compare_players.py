from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import row
from bokeh.plotting import figure, show

from read_nba_data import player_stats

output_file('jokic_vs_embiid.html', title='Nikola Jokic vs. Joel Embiid')

# Column
players = ColumnDataSource(player_stats)

# Player views
jokic_filters = [
    GroupFilter(column_name='playFNm', group='Nikola'),
    GroupFilter(column_name='playLNm', group='Jokić')
    ]
jokic_view = CDSView(source=players, filters=jokic_filters)

embiid_filters = [
    GroupFilter(column_name='playFNm', group='Joel'),
    GroupFilter(column_name='playLNm', group='Embiid')
    ]
embiid_view = CDSView(source=players, filters=embiid_filters)

# Common Keyword arguments
rebound_figure_keywords = {
    'plot_width': 400,
    'x_axis_label': 'Points',
    'toolbar_location': None,
}
assist_figure_keywords = {
    'plot_width': 600,
    'x_axis_label': 'Points',
    'toolbar_location': None,
}
circle_keywords = {
    'x': 'playPTS',
    'y': 'playTRB',
    'source': players,
    'size': 12,
    'alpha': 0.7,
}
square_keywords = {
    'x': 'playPTS',
    'y': 'playAST',
    'source': players,
    'size': 12,
    'alpha': 0.7,
}
jokic_keywords = {
    'view': jokic_view,
    'color': '#002859',
    'legend_label': 'Nikola Jokić'
}
embiid_keywords = {
    'view': embiid_view,
    'color': '#FFC324',
    'legend_label': 'Joel Embiid',
}

# Figures
hide_fig = figure(
    **rebound_figure_keywords,
    title='Click Legend to HIDE Data',
    y_axis_label='Rebounds'
    )
hide_fig.circle(**circle_keywords, **jokic_keywords)
hide_fig.circle(**circle_keywords, **embiid_keywords)

mute_fig = figure(**assist_figure_keywords,
                  title='Click Legend to Mute Data')
mute_fig.square(**square_keywords, **jokic_keywords, muted_alpha=0.1)
mute_fig.square(**square_keywords, **embiid_keywords, muted_alpha=0.1)

# Interactivity
hide_fig.legend.click_policy = 'hide'
mute_fig.legend.click_policy = 'mute'

show(row(hide_fig, mute_fig))
