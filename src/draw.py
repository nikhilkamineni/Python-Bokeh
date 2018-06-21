import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.palettes import Spectral8
from bokeh.models import (
    GraphRenderer,
    StaticLayoutProvider,
    Circle,
    ColumnDataSource,
    LabelSet,
    Label,
)

from graph import *

WIDTH = 640
HEIGHT = 480
CIRCLE_SIZE = 30

graph_data = Graph()
graph_data.debug_create_test_data()
# graph_data.bfs(graph_data.vertexes[0])

N = len(graph_data.vertexes)
node_indices = list(range(N))

# populate the list of colors from the property on each vertex
color_list = [v.color for v in graph_data.vertexes]

plot = figure(
    title="Python-Bokeh Graph project with CS8",
    x_range=(0, WIDTH),
    y_range=(0, HEIGHT),
    tools="",
    toolbar_location=None,
    plot_width=WIDTH,
    plot_height=HEIGHT
)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, "index")
graph.node_renderer.data_source.add(color_list, "color")
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color="color")


# this is drawing the edges from start to end
start_indexes = []
end_indexes = []

for v in graph_data.vertexes:
    for e in v.edges:
        self_index = graph_data.vertexes.index(v)
        start_indexes.append(self_index)

        dest_index = graph_data.vertexes.index(e.destination)
        end_indexes.append(dest_index)

graph.edge_renderer.data_source.data = dict(start=start_indexes, end=end_indexes)

# this is setting the positions of the vertexes
x = [v.pos["x"] for v in graph_data.vertexes]
y = [v.pos["y"] for v in graph_data.vertexes]
names = [v.value for v in graph_data.vertexes]

# draw labels
label_data = dict(x=x, y=y, names=names)
source = ColumnDataSource(data=label_data)
labels = LabelSet(
    x="x",
    y="y",
    x_offset=-7,
    # y_offset=-40,
    text_baseline="middle",
    text_color="white",
    text="names",
    level="overlay",
    source=source,
    render_mode="canvas",
)

# start of layout code

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.add_layout(labels)
plot.renderers.append(graph)

output_file("graph.html")
show(plot)
