"""
Chart update callbacks for the dashboard application.
"""

from dash import callback, Output, Input, no_update
from components.charts import create_climate_chart, create_empty_chart_message, create_error_chart_message
import uuid

def register_chart_callbacks(app):
    """Register chart update callbacks"""
    
    # Callback to update scatter plot
    @app.callback(
        [Output('scatter-plot-container', 'children'),
         Output('error-store', 'data', allow_duplicate=True)],
        [Input('selections-store', 'data'),
         Input('geo-tabs', 'value')],
        prevent_initial_call=True
    )
    def update_scatter_plot(selections, active_tab):
        if not selections:
            return create_empty_chart_message(), no_update
        
        continent = selections.get('continent')
        country = selections.get('country')
        state = selections.get('state')
        city = selections.get('city')
        
        # Generate sample data for scatter plot based on current selection
        if not any([continent, country, state, city]):
            return create_empty_chart_message(), no_update
        
        try:
            # Determine the currently selected entity
            if active_tab == 'city-tab' and city:
                entity = city
                entity_type = "City"
            elif active_tab == 'state-tab' and state:
                entity = state
                entity_type = "State"
            elif active_tab == 'country-tab' and country:
                entity = country
                entity_type = "Country"
            elif active_tab == 'continent-tab' and continent:
                entity = continent
                entity_type = "Continent"
            else:
                return create_empty_chart_message(), no_update
            
            return create_climate_chart(entity, entity_type), no_update
        
        except Exception as e:
            error_id = str(uuid.uuid4())
            return create_error_chart_message(), {
                'show': True,
                'message': f"Error generating chart: {str(e)}",
                'type': 'error',
                'id': error_id
            }
