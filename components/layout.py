"""
Layout components for the dashboard application.
"""

from dash import html, dcc
import dash_ag_grid as dag
from utils.styles import colors, tab_style, tab_selected_style, card_style, header_style

def create_header():
    """Create the header component"""
    return html.Div([
        html.H1("Geographic Information Dashboard", 
                style={'textAlign': 'center', 'color': 'white', 'margin': '0', 'padding': '20px 0'}),
        html.P("Explore data from continents to cities", 
               style={'textAlign': 'center', 'color': 'white', 'opacity': '0.8', 'marginTop': '5px'})
    ], style=header_style)

def create_dropdown_section():
    """Create the dropdown selection section"""
    return html.Div([
        html.Div([
            html.H3("Location Selection", 
                    style={'marginTop': '0', 'marginBottom': '20px', 'color': colors['primary']}),
            
            html.Div([
                html.Label('Continent:', 
                           style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                dcc.Loading(
                    id="loading-continent-dropdown",
                    type="circle",
                    children=[
                        dcc.Dropdown(
                            id='continent-dropdown',
                            options=[],
                            placeholder="Select a continent"
                        )
                    ]
                ),
            ], style={'marginBottom': '20px'}),
            
            html.Div([
                html.Label('Country:', 
                           style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                dcc.Loading(
                    id="loading-country-dropdown",
                    type="circle",
                    children=[
                        dcc.Dropdown(
                            id='country-dropdown',
                            placeholder="Select a country"
                        )
                    ]
                ),
            ], style={'marginBottom': '20px'}),
            
            html.Div([
                html.Label('State/Province:', 
                           style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                dcc.Loading(
                    id="loading-state-dropdown",
                    type="circle",
                    children=[
                        dcc.Dropdown(
                            id='state-dropdown',
                            placeholder="Select a state/province"
                        )
                    ]
                ),
            ], style={'marginBottom': '20px'}),
            
            html.Div([
                html.Label('City:', 
                           style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                dcc.Loading(
                    id="loading-city-dropdown",
                    type="circle",
                    children=[
                        dcc.Dropdown(
                            id='city-dropdown',
                            placeholder="Select a city"
                        )
                    ]
                ),
            ]),
        ], style=card_style),
        
        # Information card
        html.Div([
            html.H3("How to Use", 
                    style={'marginTop': '0', 'marginBottom': '15px', 'color': colors['primary']}),
            html.P("1. Select a continent from the dropdown above."),
            html.P("2. Choose a country within that continent."),
            html.P("3. Select a state/province if available."),
            html.P("4. Choose a city within that state/province."),
            html.P("The data table and visualization will update automatically based on your selection."),
            html.P("You can bookmark or share the URL to save your current view.", 
                   style={'marginTop': '15px', 'fontStyle': 'italic'})
        ], style=card_style),
    ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'})

def create_tabs_section():
    """Create the tabs section with tables"""
    return html.Div([
        html.Div([
            dcc.Tabs(
                id='geo-tabs',
                value='continent-tab',
                children=[
                    dcc.Tab(
                        label='Continent',
                        value='continent-tab',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            dcc.Loading(
                                id="loading-continent-table",
                                type="default",
                                children=[html.Div(id='continent-table-container', style={'padding': '20px'})]
                            )
                        ]
                    ),
                    dcc.Tab(
                        label='Country',
                        value='country-tab',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            dcc.Loading(
                                id="loading-country-table",
                                type="default",
                                children=[html.Div(id='country-table-container', style={'padding': '20px'})]
                            )
                        ]
                    ),
                    dcc.Tab(
                        label='State/Province',
                        value='state-tab',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            dcc.Loading(
                                id="loading-state-table",
                                type="default",
                                children=[html.Div(id='state-table-container', style={'padding': '20px'})]
                            )
                        ]
                    ),
                    dcc.Tab(
                        label='City',
                        value='city-tab',
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            dcc.Loading(
                                id="loading-city-table",
                                type="default",
                                children=[html.Div(id='city-table-container', style={'padding': '20px'})]
                            )
                        ]
                    ),
                ]
            )
        ], style={
            'backgroundColor': colors['card'],
            'borderRadius': '8px',
            'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
            'marginBottom': '20px'
        }),
        
        # Scatter plot area below the table
        html.Div([
            dcc.Loading(
                id="loading-scatter-plot",
                type="default",
                children=[html.Div(id='scatter-plot-container')]
            )
        ], style={
            'backgroundColor': colors['card'],
            'borderRadius': '8px',
            'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
            'overflow': 'hidden'
        })
        
    ], style={'width': '68%', 'float': 'right', 'display': 'inline-block'})

def create_error_notification():
    """Create the error notification container"""
    return html.Div(
        id='error-notification-container',
        style={
            'position': 'fixed',
            'top': '80px',
            'right': '20px',
            'width': '350px',
            'maxWidth': '100%',
            'zIndex': '1000',
            'display': 'none'
        }
    )

def create_layout(app):
    """Create the main layout for the application"""
    return html.Div(style={'backgroundColor': colors['background'], 'minHeight': '100vh'}, children=[
        # Store the URL
        dcc.Location(id='url', refresh=False),
        
        # Store for keeping track of initialization and selections
        dcc.Store(id='selections-store', data={}),
        
        # Store for loading states (optional but good practice)
        dcc.Store(id='loading-states', data={
            'continents': False,
            'countries': False,
            'states': False,
            'cities': False,
            'continent_data': False,
            'country_data': False,
            'state_data': False,
            'city_data': False,
            'chart': False
        }),
        
        # Store for error messages
        dcc.Store(id='error-store', data={'show': False, 'message': '', 'type': 'error', 'id': None}),
        
        # Header
        create_header(),
        
        # Error notification container
        create_error_notification(),
        
        # Main container
        html.Div([
            # Two-column layout
            html.Div([
                # Left column - Dropdowns
                create_dropdown_section(),
                
                # Right column - Tabs with tables and chart
                create_tabs_section(),
            ], style={'maxWidth': '1400px', 'margin': '0 auto', 'padding': '0 20px'}),
        ]),
        
        # Interval component for auto-dismissing error notifications
        dcc.Interval(
            id='error-dismiss-interval',
            interval=8000,  # 8 seconds
            n_intervals=0
        ),
    ])
