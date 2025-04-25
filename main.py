import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px
import numpy as np
from urllib.parse import parse_qs, urlencode
import time
from functools import lru_cache
import uuid

# Initialize the Dash application
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

# Define custom styles
# Colors based on a modern blue palette
colors = {
    'background': '#f8f9fa',
    'card': '#ffffff',
    'primary': '#3f51b5',
    'secondary': '#7986cb',
    'accent': '#536dfe',
    'text': '#333333',
    'light_text': '#757575',
    'border': '#e0e0e0'
}

# Cache system for data fetching functions
# Using lru_cache with maxsize to limit memory usage
@lru_cache(maxsize=128)
def fetch_data_with_cache(data_type, parent=None):
    """Generic caching wrapper for data fetching functions"""
    if data_type == 'continents':
        return get_continents()
    elif data_type == 'countries':
        return get_countries(parent)
    elif data_type == 'states':
        return get_states(parent)
    elif data_type == 'cities':
        return get_cities(parent)
    elif data_type == 'continent_data':
        return get_continent_data(parent)
    elif data_type == 'country_data':
        return get_country_data(parent)
    elif data_type == 'state_data':
        return get_state_data(parent)
    elif data_type == 'city_data':
        return get_city_data(parent)
    return None

# Data fetching functions that simulate API calls
def get_continents():
    """Fetch list of continents from server"""
    # Simulate network delay
    #time.sleep(0.5)
    return ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']

def get_countries(continent):
    """Fetch countries for a given continent from server"""
    if not continent:
        return []
    
    # Simulate network delay
    #time.sleep(0.8)
    
    countries_data = {
        'North America': ['USA', 'Canada', 'Mexico'],
        'Europe': ['Germany', 'France', 'UK', 'Italy', 'Spain'],
        'Asia': ['China', 'Japan', 'India', 'South Korea'],
        'Africa': ['South Africa', 'Egypt', 'Nigeria', 'Kenya'],
        'South America': ['Brazil', 'Argentina', 'Colombia', 'Chile'],
        'Oceania': ['Australia', 'New Zealand']
    }
    
    return countries_data.get(continent, [])

def get_states(country):
    """Fetch states/provinces for a given country from server"""
    if not country:
        return []
    
    # Simulate network delay
    #time.sleep(0.7)
    
    states_data = {
        'USA': ['California', 'New York', 'Texas', 'Florida'],
        'Canada': ['Ontario', 'Quebec', 'British Columbia', 'Alberta'],
        'Germany': ['Bavaria', 'Hesse', 'Berlin'],
        'France': ['Île-de-France', 'Provence', 'Normandy'],
        'UK': ['England', 'Scotland', 'Wales', 'Northern Ireland']
    }
    
    return states_data.get(country, [])

def get_cities(state):
    """Fetch cities for a given state/province from server"""
    if not state:
        return []
    
    # Simulate network delay
    #time.sleep(0.6)
    
    cities_data = {
        'California': ['Los Angeles', 'San Francisco', 'San Diego'],
        'New York': ['New York City', 'Buffalo', 'Albany'],
        'Ontario': ['Toronto', 'Ottawa', 'Hamilton'],
        'Bavaria': ['Munich', 'Nuremberg', 'Augsburg'],
        'Île-de-France': ['Paris', 'Versailles', 'Saint-Denis'],
        'England': ['London', 'Manchester', 'Liverpool']
    }
    
    return cities_data.get(state, [])

def get_continent_data(continent):
    """Fetch detailed data for a specific continent"""
    if not continent:
        return {}
    
    # Simulate network delay
    #time.sleep(1.0)
    
    continent_data = {
        'North America': {'Population': '579 million', 'Area': '24.71 million km²', 
                         'Countries': '23', 'Major Languages': 'English, Spanish, French'},
        'Europe': {'Population': '746 million', 'Area': '10.18 million km²', 
                  'Countries': '44', 'Major Languages': 'English, German, French, Italian, Spanish'},
        'Asia': {'Population': '4.7 billion', 'Area': '44.58 million km²', 
                'Countries': '48', 'Major Languages': 'Mandarin, Hindi, Arabic, Russian'}
    }
    
    return continent_data.get(continent, {})

def get_country_data(country):
    """Fetch detailed data for a specific country"""
    if not country:
        return {}
    
    # Simulate network delay
    #time.sleep(0.9)
    
    country_data = {
        'USA': {'Capital': 'Washington D.C.', 'Population': '331 million', 
               'GDP': '$21.4 trillion', 'Currency': 'USD', 'Official Language': 'English'},
        'Canada': {'Capital': 'Ottawa', 'Population': '38 million', 
                  'GDP': '$1.6 trillion', 'Currency': 'CAD', 'Official Languages': 'English, French'},
        'Germany': {'Capital': 'Berlin', 'Population': '83 million', 
                   'GDP': '$3.8 trillion', 'Currency': 'Euro', 'Official Language': 'German'}
    }
    
    return country_data.get(country, {})

def get_state_data(state):
    """Fetch detailed data for a specific state/province"""
    if not state:
        return {}
    
    # Simulate network delay
    #time.sleep(0.8)
    
    state_data = {
        'California': {'Capital': 'Sacramento', 'Population': '39.5 million', 
                      'Largest City': 'Los Angeles', 'Area': '423,970 km²', 'Year Founded': '1850'},
        'New York': {'Capital': 'Albany', 'Population': '19.5 million', 
                    'Largest City': 'New York City', 'Area': '141,297 km²', 'Year Founded': '1788'},
        'Ontario': {'Capital': 'Toronto', 'Population': '14.5 million', 
                   'Largest City': 'Toronto', 'Area': '1,076,395 km²', 'Year Founded': '1867'}
    }
    
    return state_data.get(state, {})

def get_city_data(city):
    """Fetch detailed data for a specific city"""
    if not city:
        return {}
    
    # Simulate network delay
    #time.sleep(0.7)
    
    city_data = {
        'Los Angeles': {'Population': '3.9 million', 'Area': '1,302 km²', 
                       'Mayor': 'Karen Bass', 'Founded': '1781', 'Famous For': 'Hollywood'},
        'New York City': {'Population': '8.4 million', 'Area': '783.8 km²', 
                         'Mayor': 'Eric Adams', 'Founded': '1624', 'Famous For': 'Wall Street'},
        'London': {'Population': '8.9 million', 'Area': '1,572 km²', 
                  'Mayor': 'Sadiq Khan', 'Founded': '43 AD', 'Famous For': 'Big Ben'}
    }
    
    return city_data.get(city, {})

# Define the layout
app.layout = html.Div(style={'backgroundColor': colors['background'], 'minHeight': '100vh'}, children=[
    # Store the URL
    dcc.Location(id='url', refresh=False),
    
    # Store for keeping track of initialization and selections
    dcc.Store(id='selections-store', data={}),
    
    # Store for loading states
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
    
    # Header
    html.Div([
        html.H1("Example Dashboard", style={'textAlign': 'center', 'color': 'white', 'margin': '0', 'padding': '20px 0'}),
        # html.P("Explore data from around the world.", style={'textAlign': 'center', 'color': 'white', 'opacity': '0.8', 'marginTop': '5px'})
    ], style={'backgroundColor': colors['primary'], 'padding': '10px 0', 'marginBottom': '20px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
    
    # Main container
    html.Div([
        # Two-column layout
        html.Div([
            # Left column - Dropdowns
            html.Div([
                html.Div([
                    html.H3("Location Selection", style={'marginTop': '0', 'marginBottom': '20px', 'color': colors['primary']}),
                    
                    html.Div([
                        html.Label('Continent:', style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Loading(
                            id="loading-continent-dropdown",
                            type="circle",
                            delay_show=800,
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
                        html.Label('Country:', style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Loading(
                            id="loading-country-dropdown",
                            type="circle",
                            delay_show=800,
                            children=[
                                dcc.Dropdown(
                                    id='country-dropdown',
                                    placeholder="Select a country"
                                )
                            ]
                        ),
                    ], style={'marginBottom': '20px'}),
                    
                    html.Div([
                        html.Label('State/Province:', style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Loading(
                            id="loading-state-dropdown",
                            type="circle",
                            delay_show=800,
                            children=[
                                dcc.Dropdown(
                                    id='state-dropdown',
                                    placeholder="Select a state/province"
                                )
                            ]
                        ),
                    ], style={'marginBottom': '20px'}),
                    
                    html.Div([
                        html.Label('City:', style={'fontWeight': '500', 'marginBottom': '8px', 'display': 'block'}),
                        dcc.Loading(
                            id="loading-city-dropdown",
                            type="circle",
                            delay_show=800,
                            children=[
                                dcc.Dropdown(
                                    id='city-dropdown',
                                    placeholder="Select a city"
                                )
                            ]
                        ),
                    ]),
                ], style={
                    'backgroundColor': colors['card'], 
                    'padding': '20px', 
                    'borderRadius': '8px',
                    'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
                    'marginBottom': '20px'
                }),
                
                # Information card
                html.Div([
                    html.H3("How to Use", style={'marginTop': '0', 'marginBottom': '15px', 'color': colors['primary']}),
                    html.P("1. Select a continent from the dropdown above."),
                    html.P("2. Choose a country within that continent."),
                    html.P("3. Select a state/province if available."),
                    html.P("4. Choose a city within that state/province."),
                    html.P("The data table and visualization will update automatically based on your selection."),
                    html.P("You can bookmark or share the URL to save your current view.", style={'marginTop': '15px', 'fontStyle': 'italic'})
                ], style={
                    'backgroundColor': colors['card'], 
                    'padding': '20px', 
                    'borderRadius': '8px',
                    'boxShadow': '0 2px 10px rgba(0,0,0,0.1)'
                }),
            ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),
            
            # Right column - Tabs with tables and chart
            html.Div([
                html.Div([
                    dcc.Tabs(
                        id='geo-tabs', 
                        value='continent-tab',
                        children=[
                            dcc.Tab(
                                label='Continent', 
                                value='continent-tab',
                                style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500'
                                },
                                selected_style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500',
                                    'backgroundColor': colors['primary'],
                                    'color': 'white',
                                    'borderColor': colors['primary']
                                },
                                children=[
                                    dcc.Loading(
                                        id="loading-continent-table",
                                        type="default",
                                        delay_show=800,
                                        children=[html.Div(id='continent-table-container', style={'padding': '20px'})]
                                    )
                                ]
                            ),
                            dcc.Tab(
                                label='Country', 
                                value='country-tab',
                                style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500'
                                },
                                selected_style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500',
                                    'backgroundColor': colors['primary'],
                                    'color': 'white',
                                    'borderColor': colors['primary']
                                },
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
                                style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500'
                                },
                                selected_style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500',
                                    'backgroundColor': colors['primary'],
                                    'color': 'white',
                                    'borderColor': colors['primary']
                                },
                                children=[
                                    dcc.Loading(
                                        id="loading-state-table",
                                        delay_show=800,
                                        type="default",
                                        children=[html.Div(id='state-table-container', style={'padding': '20px'})]
                                    )
                                ]
                            ),
                            dcc.Tab(
                                label='City', 
                                value='city-tab',
                                style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500'
                                },
                                selected_style={
                                    'borderRadius': '4px 4px 0 0',
                                    'padding': '12px 20px',
                                    'fontWeight': '500',
                                    'backgroundColor': colors['primary'],
                                    'color': 'white',
                                    'borderColor': colors['primary']
                                },
                                children=[
                                    dcc.Loading(
                                        id="loading-city-table",
                                        delay_show=800,
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
                        delay_show=800,
                        type="default",
                        children=[html.Div(id='scatter-plot-container')]
                    )
                ], style={
                    'backgroundColor': colors['card'], 
                    'borderRadius': '8px',
                    'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
                    'overflow': 'hidden'
                })
                
            ], style={'width': '68%', 'float': 'right', 'display': 'inline-block'}),
        ], style={'maxWidth': '1400px', 'margin': '0 auto', 'padding': '0 20px'}),
    ]),
])

# Callback to initialize continents dropdown
@app.callback(
    Output('continent-dropdown', 'options'),
    Input('url', 'pathname')
)
def initialize_continents_dropdown(pathname):
    # Fetch continents data with caching
    continents = fetch_data_with_cache('continents')
    return [{'label': i, 'value': i} for i in continents]

# Callback to initialize from URL and update selections store
@app.callback(
    Output('selections-store', 'data'),
    [Input('url', 'search')],
    [State('selections-store', 'data')]
)
def initialize_from_url(search, current_selections):
    # If this is not the initial load (selections exist), don't update from URL
    if current_selections and 'initialized' in current_selections and current_selections['initialized']:
        return current_selections
    
    # Default empty selections
    selections = {
        'continent': None,
        'country': None,
        'state': None,
        'city': None,
        'initialized': True
    }
    
    # Parse URL parameters if they exist
    if search:
        parsed = parse_qs(search.lstrip('?'))
        if 'continent' in parsed:
            selections['continent'] = parsed['continent'][0]
        if 'country' in parsed:
            selections['country'] = parsed['country'][0]
        if 'state' in parsed:
            selections['state'] = parsed['state'][0]
        if 'city' in parsed:
            selections['city'] = parsed['city'][0]
    
    return selections

# Callback to update URL based on selections store
@app.callback(
    Output('url', 'search'),
    [Input('selections-store', 'data')]
)
def update_url(selections):
    if not selections or not selections.get('initialized', False):
        return dash.no_update
    
    params = {}
    if selections.get('continent'):
        params['continent'] = selections['continent']
    if selections.get('country'):
        params['country'] = selections['country']
    if selections.get('state'):
        params['state'] = selections['state']
    if selections.get('city'):
        params['city'] = selections['city']
    
    return f"?{urlencode(params)}" if params else ""

# Callback to update dropdown values from selections store
@app.callback(
    [Output('continent-dropdown', 'value'),
     Output('country-dropdown', 'options'),
     Output('country-dropdown', 'value'),
     Output('state-dropdown', 'options'),
     Output('state-dropdown', 'value'),
     Output('city-dropdown', 'options'),
     Output('city-dropdown', 'value')],
    [Input('selections-store', 'data')]
)
def update_dropdowns_from_store(selections):
    if not selections:
        return None, [], None, [], None, [], None
    
    continent = selections.get('continent')
    country = selections.get('country')
    state = selections.get('state')
    city = selections.get('city')
    
    # Set country options based on continent
    country_options = []
    if continent:
        # Fetch countries data with caching
        countries_list = fetch_data_with_cache('countries', continent)
        country_options = [{'label': i, 'value': i} for i in countries_list]
    
    # Set state options based on country
    state_options = []
    if country:
        # Fetch states data with caching
        states_list = fetch_data_with_cache('states', country)
        state_options = [{'label': i, 'value': i} for i in states_list]
    
    # Set city options based on state
    city_options = []
    if state:
        # Fetch cities data with caching
        cities_list = fetch_data_with_cache('cities', state)
        city_options = [{'label': i, 'value': i} for i in cities_list]
    
    return continent, country_options, country, state_options, state, city_options, city

# Callbacks to update selections store based on dropdown changes
@app.callback(
    Output('selections-store', 'data', allow_duplicate=True),
    [Input('continent-dropdown', 'value')],
    [State('selections-store', 'data')],
    prevent_initial_call=True
)
def update_continent_selection(continent, selections):
    if selections is None:
        selections = {}
    
    # If continent changed, reset dependent fields
    if continent != selections.get('continent'):
        selections['continent'] = continent
        selections['country'] = None
        selections['state'] = None
        selections['city'] = None
    else:
        selections['continent'] = continent
    
    selections['initialized'] = True
    return selections

@app.callback(
    Output('selections-store', 'data', allow_duplicate=True),
    [Input('country-dropdown', 'value')],
    [State('selections-store', 'data')],
    prevent_initial_call=True
)
def update_country_selection(country, selections):
    if selections is None:
        selections = {}
    
    # If country changed, reset dependent fields
    if country != selections.get('country'):
        selections['country'] = country
        selections['state'] = None
        selections['city'] = None
    else:
        selections['country'] = country
    
    selections['initialized'] = True
    return selections

@app.callback(
    Output('selections-store', 'data', allow_duplicate=True),
    [Input('state-dropdown', 'value')],
    [State('selections-store', 'data')],
    prevent_initial_call=True
)
def update_state_selection(state, selections):
    if selections is None:
        selections = {}
    
    # If state changed, reset dependent fields
    if state != selections.get('state'):
        selections['state'] = state
        selections['city'] = None
    else:
        selections['state'] = state
    
    selections['initialized'] = True
    return selections

@app.callback(
    Output('selections-store', 'data', allow_duplicate=True),
    [Input('city-dropdown', 'value')],
    [State('selections-store', 'data')],
    prevent_initial_call=True
)
def update_city_selection(city, selections):
    if selections is None:
        selections = {}
    
    selections['city'] = city
    selections['initialized'] = True
    return selections

# Callback to update active tab based on dropdown selections
@app.callback(
    Output('geo-tabs', 'value'),
    [Input('selections-store', 'data')]
)
def update_active_tab(selections):
    if not selections:
        return 'continent-tab'
    
    if selections.get('city'):
        return 'city-tab'
    elif selections.get('state'):
        return 'state-tab'
    elif selections.get('country'):
        return 'country-tab'
    elif selections.get('continent'):
        return 'continent-tab'
    return 'continent-tab'

# Callbacks to update table contents using AG Grid
@app.callback(
    Output('continent-table-container', 'children'),
    [Input('selections-store', 'data')]
)
def update_continent_table(selections):
    if not selections or not selections.get('continent'):
        return html.Div("Please select a continent to view information.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    selected_continent = selections.get('continent')
    
    # Fetch continent data with caching
    data = fetch_data_with_cache('continent_data', selected_continent)
    
    if not data:
        return html.Div(f"No data available for {selected_continent}.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    df = pd.DataFrame([data])
    df.insert(0, 'Continent', selected_continent)
    
    columnDefs = [{"field": col, "headerName": col.replace('_', ' ').title()} for col in df.columns]
    
    return html.Div([
        html.H3(f"{selected_continent} Information", style={'marginTop': '0', 'color': colors['primary']}),
        dag.AgGrid(
            id='continent-ag-grid',
            rowData=df.to_dict('records'),
            columnDefs=columnDefs,
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 120,
            },
            dashGridOptions={"domLayout": "autoHeight"},
            className="ag-theme-alpine",
        )
    ])

@app.callback(
    Output('country-table-container', 'children'),
    [Input('selections-store', 'data')]
)
def update_country_table(selections):
    if not selections or not selections.get('country'):
        return html.Div("Please select a country to view information.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    selected_country = selections.get('country')
    
    # Fetch country data with caching
    data = fetch_data_with_cache('country_data', selected_country)
    
    if not data:
        return html.Div(f"No data available for {selected_country}.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    df = pd.DataFrame([data])
    df.insert(0, 'Country', selected_country)
    
    columnDefs = [{"field": col, "headerName": col.replace('_', ' ').title()} for col in df.columns]
    
    return html.Div([
        html.H3(f"{selected_country} Information", style={'marginTop': '0', 'color': colors['primary']}),
        dag.AgGrid(
            id='country-ag-grid',
            rowData=df.to_dict('records'),
            columnDefs=columnDefs,
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 120,
            },
            dashGridOptions={"domLayout": "autoHeight"},
            className="ag-theme-alpine",
        )
    ])

@app.callback(
    Output('state-table-container', 'children'),
    [Input('selections-store', 'data')]
)
def update_state_table(selections):
    if not selections or not selections.get('state'):
        return html.Div("Please select a state/province to view information.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    selected_state = selections.get('state')
    
    # Fetch state data with caching
    data = fetch_data_with_cache('state_data', selected_state)
    
    if not data:
        return html.Div(f"No data available for {selected_state}.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    df = pd.DataFrame([data])
    df.insert(0, 'State/Province', selected_state)
    
    columnDefs = [{"field": col, "headerName": col.replace('_', ' ').title()} for col in df.columns]
    
    return html.Div([
        html.H3(f"{selected_state} Information", style={'marginTop': '0', 'color': colors['primary']}),
        dag.AgGrid(
            id='state-ag-grid',
            rowData=df.to_dict('records'),
            columnDefs=columnDefs,
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 120,
            },
            dashGridOptions={"domLayout": "autoHeight"},
            className="ag-theme-alpine",
        )
    ])

@app.callback(
    Output('city-table-container', 'children'),
    [Input('selections-store', 'data')]
)
def update_city_table(selections):
    if not selections or not selections.get('city'):
        return html.Div("Please select a city to view information.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    selected_city = selections.get('city')
    
    # Fetch city data with caching
    data = fetch_data_with_cache('city_data', selected_city)
    
    if not data:
        return html.Div(f"No data available for {selected_city}.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    df = pd.DataFrame([data])
    df.insert(0, 'City', selected_city)
    
    columnDefs = [{"field": col, "headerName": col.replace('_', ' ').title()} for col in df.columns]
    
    return html.Div([
        html.H3(f"{selected_city} Information", style={'marginTop': '0', 'color': colors['primary']}),
        dag.AgGrid(
            id='city-ag-grid',
            rowData=df.to_dict('records'),
            columnDefs=columnDefs,
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 120,
            },
            dashGridOptions={"domLayout": "autoHeight"},
            className="ag-theme-alpine",
        )
    ])

# Callback to update scatter plot
@app.callback(
    Output('scatter-plot-container', 'children'),
    [Input('selections-store', 'data'),
     Input('geo-tabs', 'value')]
)
def update_scatter_plot(selections, active_tab):
    if not selections:
        return html.Div("Select a geographic entity to view data visualization.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    continent = selections.get('continent')
    country = selections.get('country')
    state = selections.get('state')
    city = selections.get('city')
    
    # Generate sample data for scatter plot based on current selection
    if not any([continent, country, state, city]):
        return html.Div("Select a geographic entity to view data visualization.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    # Determine the currently selected entity
    if active_tab == 'city-tab' and city:
        entity = city
        title = f"Monthly Climate Data for {city}"
        entity_type = "City"
    elif active_tab == 'state-tab' and state:
        entity = state
        title = f"Monthly Climate Data for {state}"
        entity_type = "State"
    elif active_tab == 'country-tab' and country:
        entity = country
        title = f"Monthly Climate Data for {country}"
        entity_type = "Country"
    elif active_tab == 'continent-tab' and continent:
        entity = continent
        title = f"Monthly Climate Data for {continent}"
        entity_type = "Continent"
    else:
        return html.Div("No data available for visualization.", 
                       style={'padding': '20px', 'color': colors['light_text'], 'fontStyle': 'italic'})
    
    # Simulate data loading delay
    #time.sleep(0.8)
    
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
        html.P("Monthly temperature and precipitation patterns", style={'color': colors['light_text'], 'marginBottom': '20px'}),
        dcc.Graph(
            figure=fig,
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['select2d', 'lasso2d']
            },
            style={'height': '450px'}
        )
    ], style={'padding': '20px'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
