import plotly.graph_objects as go
import numpy as np
import kaleido

iteration = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Original data
custom_kg_time = [93, 97, 96, 97, 96, 95, 95, 93, 95, 94]
neo4j_time = [4792, 4423, 4469, 4637, 5405, 4868, 4655, 4134, 5627, 4491]

# Transform data to log base 2
log2_custom_kg = np.log2(custom_kg_time)
log2_neo4j = np.log2(neo4j_time)

fig = go.Figure()
fig.add_trace(go.Bar(x=iteration,
                     y=log2_custom_kg,
                     name='Custom KG',
                     marker_color='rgb(55, 83, 109)',
                     text=custom_kg_time,
                     textposition='auto'
                     ))
fig.add_trace(go.Bar(x=iteration,
                     y=log2_neo4j,
                     name='Neo4j',
                     marker_color='rgb(26, 118, 255)',
                     text=neo4j_time,
                     textposition='auto'
                     ))

fig.update_layout(
    title='Custom KG vs Neo4j Build Time Comparison',
    xaxis=dict(
        tickfont_size=14,
        tickvals=iteration,  # Custom x-axis ticks from 1 to 10
        ticktext=[str(i) for i in iteration]  # Tick labels
    ),
    yaxis=dict(
        title='log2(Time in Microseconds)',
        titlefont_size=14,
        tickfont_size=10,
        tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],  # Log2 scale values
        ticktext=["2^0", "2^1", "2^2", "2^3", "2^4", "2^5", "2^6", "2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13"],  # Custom tick text
        range=[0, 13]  # Set the range to include up to log2(8192)
    ),
    legend=dict(
        orientation='h',  # Horizontal legend
        yanchor='bottom',
        y=1.02,  # Position the legend at the top
        xanchor='center',
        x=0.5,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,  # gap between bars of adjacent location coordinates
    bargroupgap=0.1  # gap between bars of the same location coordinate
)

# Export the plot as a PNG file using kaleido
fig.write_image('plot.png', engine='kaleido')
