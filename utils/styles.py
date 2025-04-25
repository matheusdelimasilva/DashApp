"""
Styles for the dashboard application.
Contains color definitions and common style elements.
"""

# Colors based on a modern blue palette
colors = {
    'background': '#f8f9fa',
    'card': '#ffffff',
    'primary': '#3f51b5',
    'secondary': '#7986cb',
    'accent': '#536dfe',
    'text': '#333333',
    'light_text': '#757575',
    'border': '#e0e0e0',
    'error': '#f44336',
    'warning': '#ff9800',
    'success': '#4caf50'
}

# Common style elements
tab_style = {
    'borderRadius': '4px 4px 0 0',
    'padding': '12px 20px',
    'fontWeight': '500'
}

tab_selected_style = {
    'borderRadius': '4px 4px 0 0',
    'padding': '12px 20px',
    'fontWeight': '500',
    'backgroundColor': colors['primary'],
    'color': 'white',
    'borderColor': colors['primary']
}

card_style = {
    'backgroundColor': colors['card'],
    'padding': '20px',
    'borderRadius': '8px',
    'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
    'marginBottom': '20px'
}

header_style = {
    'backgroundColor': colors['primary'],
    'padding': '10px 0',
    'marginBottom': '20px',
    'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'
}

# AG Grid default column definition
default_col_def = {
    "resizable": True,
    "sortable": True,
    "filter": True,
    "minWidth": 120,
}

# Graph configuration
graph_config = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['select2d', 'lasso2d']
}
