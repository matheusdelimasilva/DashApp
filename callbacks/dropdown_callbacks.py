"""
Dropdown interaction callbacks for the dashboard application.
"""

from dash import callback, Output, Input, State, no_update
from data.cache import fetch_data_with_cache
import uuid

def register_dropdown_callbacks(app):
    """Register dropdown interaction callbacks"""
    
    # Callback to update dropdown values from selections store
    @app.callback(
        [Output('continent-dropdown', 'value'),
         Output('country-dropdown', 'options'),
         Output('country-dropdown', 'value'),
         Output('state-dropdown', 'options'),
         Output('state-dropdown', 'value'),
         Output('city-dropdown', 'options'),
         Output('city-dropdown', 'value'),
         Output('error-store', 'data', allow_duplicate=True)],
        [Input('selections-store', 'data')],
        prevent_initial_call=True
    )
    def update_dropdowns_from_store(selections):
        if not selections:
            return None, [], None, [], None, [], None, no_update
        
        continent = selections.get('continent')
        country = selections.get('country')
        state = selections.get('state')
        city = selections.get('city')
        
        try:
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
            
            return continent, country_options, country, state_options, state, city_options, city, no_update
        
        except Exception as e:
            error_id = str(uuid.uuid4())
            # Return what we can and show error
            return continent, [], country, [], state, [], city, {
                'show': True,
                'message': f"Error loading dropdown options: {str(e)}",
                'type': 'error',
                'id': error_id
            }
    
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
