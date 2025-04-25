"""
URL and navigation callbacks for the dashboard application.
"""

from dash import callback, Output, Input, State, no_update
from urllib.parse import parse_qs, urlencode
from data.cache import fetch_data_with_cache
import uuid

def register_url_callbacks(app):
    """Register URL and navigation callbacks"""
    
    # Callback to initialize continents dropdown
    @app.callback(
        [Output('continent-dropdown', 'options'),
         Output('error-store', 'data', allow_duplicate=True)],
        Input('url', 'pathname'),
        prevent_initial_call=True
    )
    def initialize_continents_dropdown(pathname):
        try:
            # Fetch continents data with caching
            continents = fetch_data_with_cache('continents')
            return [{'label': i, 'value': i} for i in continents], no_update
        except Exception as e:
            error_id = str(uuid.uuid4())
            return [], {
                'show': True,
                'message': f"Error loading continents: {str(e)}",
                'type': 'error',
                'id': error_id
            }
    
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
            return no_update
        
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
