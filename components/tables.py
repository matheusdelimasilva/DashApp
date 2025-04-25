"""
Table components for the dashboard application.
"""

from dash import html
import dash_ag_grid as dag
import pandas as pd
from utils.styles import colors, default_col_def

def create_data_table(data, entity_type, entity_name):
    """Create a data table for the given entity"""
    if not data:
        return html.Div(f"No data available for {entity_name}.",
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    df = pd.DataFrame([data])
    df.insert(0, entity_type, entity_name)
    
    column_defs = [{"field": col, "headerName": col.replace('_', ' ').title()} for col in df.columns]
    
    return html.Div([
        html.H3(f"{entity_name} Information", style={'marginTop': '0', 'color': colors['primary']}),
        dag.AgGrid(
            id=f'{entity_type.lower()}-ag-grid',
            rowData=df.to_dict('records'),
            columnDefs=column_defs,
            defaultColDef=default_col_def,
            dashGridOptions={"domLayout": "autoHeight"},
            className="ag-theme-alpine",
        )
    ])

def create_empty_table_message(entity_type):
    """Create a message for when no entity is selected"""
    return html.Div(f"Please select a {entity_type.lower()} to view information.",
                   style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})

def create_error_table_message(entity_name):
    """Create a message for when there's an error loading data"""
    return html.Div(f"Error loading data for {entity_name}.",
                   style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
