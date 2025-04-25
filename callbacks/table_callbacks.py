"""
Table update callbacks for the dashboard application.
"""

from dash import callback, Output, Input, no_update
from data.cache import fetch_data_with_cache
from components.tables import create_data_table, create_empty_table_message, create_error_table_message
import uuid

def register_table_callbacks(app):
    """Register table update callbacks"""
    
    # Callback to update continent table
    @app.callback(
        [Output('continent-table-container', 'children'),
         Output('error-store', 'data', allow_duplicate=True)],
        [Input('selections-store', 'data')],
        prevent_initial_call=True
    )
    def update_continent_table(selections):
        if not selections or not selections.get('continent'):
            return create_empty_table_message("continent"), no_update
        
        selected_continent = selections.get('continent')
        
        try:
            # Fetch continent data with caching
            data = fetch_data_with_cache('continent_data', selected_continent)
            
            if not data:
                return create_empty_table_message(f"No data available for {selected_continent}"), no_update
            
            return create_data_table(data, "Continent", selected_continent), no_update
        
        except Exception as e:
            error_id = str(uuid.uuid4())
            return create_error_table_message(selected_continent), {
                'show': True,
                'message': f"Error loading continent data: {str(e)}",
                'type': 'error',
                'id': error_id
            }
    
    # Callback to update country table
    @app.callback(
        [Output('country-table-container', 'children'),
         Output('error-store', 'data', allow_duplicate=True)],
        [Input('selections-store', 'data')],
        prevent_initial_call=True
    )
    def update_country_table(selections):
        if not selections or not selections.get('country'):
            return create_empty_table_message("country"), no_update
        
        selected_country = selections.get('country')
        
        try:
            # Fetch country data with caching
            data = fetch_data_with_cache('country_data', selected_country)
            
            if not data:
                return create_empty_table_message(f"No data available for {selected_country}"), no_update
            
            return create_data_table(data, "Country", selected_country), no_update
        
        except Exception as e:
            error_id = str(uuid.uuid4())
            return create_error_table_message(selected_country), {
                'show': True,
                'message': f"Error loading country data: {str(e)}",
                'type': 'error',
                'id': error_id
            }
    
    # Callback to update state table
    @app.callback(
        [Output('state-table-container', 'children'),
         Output('error-store', 'data', allow_duplicate=True)],
        [Input('selections-store', 'data')],
        prevent_initial_call=True
    )
    def update_state_table(selections):
        if not selections or not selections.get('state'):
            return create_empty_table_message("state/province"), no_update
        
        selected_state = selections.get('state')
        
        try:
            # Fetch state data with caching
            data = fetch_data_with_cache('state_data', selected_state)
            
            if not data:
                return create_empty_table_message(f"No data available for {selected_state}"), no_update
            
            return create_data_table(data, "State/Province", selected_state), no_update
        
        except Exception as e:
            error_id = str(uuid.uuid4())
            return create_error_table_message(selected_state), {
                'show': True,
                'message': f"Error loading state data: {str(e)}",
                'type': 'error',
                'id': error_id
            }
    
    # Callback to update city table
    @app.callback(
        [Output('city-table-container', 'children'),
         Output('error-store', 'data', allow_duplicate=True)],
        [Input('selections-store', 'data')],
        prevent_initial_call=True
    )
    def update_city_table(selections):
        if not selections or not selections.get('city'):
            return create_empty_table_message("city"), no_update
        
        selected_city = selections.get('city')
        
        try:
            # Fetch city data with caching
            data = fetch_data_with_cache('city_data', selected_city)
            
            if not data:
                return create_empty_table_message(f"No data available for {selected_city}"), no_update
            
            return create_data_table(data, "City", selected_city), no_update
        
        except Exception as e:
            error_id = str(uuid.uuid4())
            return create_error_table_message(selected_city), {
                'show': True,
                'message': f"Error loading city data: {str(e)}",
                'type': 'error',
                'id': error_id
            }
