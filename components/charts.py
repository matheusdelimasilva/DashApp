"""
Chart components for the dashboard application.
"""

from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
from utils.styles import colors, graph_config

def create_climate_chart(entity, entity_type):
    """Create a climate chart for the given entity"""
    # Generate random data for the selected entity
    np.random.seed(hash(entity) % 2**32)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    if entity_type == "City":
        temp_base = 15
        precip_base = 50
    elif entity_type == "State":
        temp_base = 12
        precip_base = 70
    elif entity_type == "Country":
        temp_base = 10
        precip_base = 90
    else:  # Continent
        temp_base = 8
        precip_base = 120
    
    df = pd.DataFrame({
        'Month': months,
        'Temperature (°C)': [temp_base + np.random.uniform(-5, 15) for _ in range(12)],
        'Precipitation (mm)': [precip_base + np.random.uniform(0, 100) for _ in range(12)]
    })
    
    title = f"Monthly Climate Data for {entity}"
    
    fig = px.scatter(
        df, 
        x='Temperature (°C)', 
        y='Precipitation (mm)',
        size='Precipitation (mm)',
        color='Month',
        hover_name='Month',
        title=title,
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    
    fig.update_layout(
        title={
            'font': {'size': 20, 'color': colors['primary']},
            'x': 0.5,
            'xanchor': 'center'
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.02)',
        margin=dict(l=40, r=40, t=60, b=40),
        hovermode='closest',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(0,0,0,0.1)',
        zeroline=False
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(0,0,0,0.1)',
        zeroline=False
    )
    
    return html.Div([
        html.H3(f"Climate Data for {entity}", style={'marginTop': '0', 'color': colors['primary']}),
        html.P("Monthly temperature and precipitation patterns", 
               style={'color': colors['light_text'], 'marginBottom': '20px'}),
        dcc.Graph(
            figure=fig,
            config=graph_config,
            style={'height': '450px'}
        )
    ], style={'padding': '20px'})

def create_empty_chart_message():
    """Create a message for when no entity is selected for the chart"""
    return html.Div("Select a geographic entity to view data visualization.", 
                   style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})

def create_error_chart_message():
    """Create a message for when there's an error generating the chart"""
    return html.Div("Error generating visualization.", 
                   style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
