"""
Error handling callbacks for the dashboard application.
"""

from dash import callback, Output, Input, State, callback_context, no_update
from utils.styles import colors
from dash import html

def register_error_callbacks(app):
    """Register error handling callbacks"""
    
    # Callback to display error notifications
    @app.callback(
        Output('error-notification-container', 'children'),
        Output('error-notification-container', 'style'),
        Input('error-store', 'data')
    )
    def display_error_notification(error_data):
        if not error_data or not error_data.get('show', False):
            return None, {'display': 'none'}
        
        error_type = error_data.get('type', 'error')
        message = error_data.get('message', 'An unknown error occurred')
        
        # Set colors based on error type
        if error_type == 'error':
            bg_color = colors['error']
            icon = '❌'
        elif error_type == 'warning':
            bg_color = colors['warning']
            icon = '⚠️'
        else:  # info
            bg_color = colors['primary']
            icon = 'ℹ️'
        
        notification = html.Div([
            html.Div([
                html.Span(icon, style={'marginRight': '10px', 'fontSize': '18px'}),
                html.Span(error_type.upper(), style={'fontWeight': 'bold'})
            ], style={'marginBottom': '5px'}),
            html.P(message, style={'margin': '0', 'wordBreak': 'break-word'}),
            html.Button(
                "×",
                id='close-error-button',
                n_clicks=0,
                style={
                    'position': 'absolute',
                    'top': '8px',
                    'right': '8px',
                    'background': 'none',
                    'border': 'none',
                    'fontSize': '20px',
                    'cursor': 'pointer',
                    'color': 'white',
                    'fontWeight': 'bold',
                    'padding': '0 5px'
                }
            )
        ], style={
            'backgroundColor': bg_color,
            'color': 'white',
            'padding': '15px',
            'borderRadius': '5px',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.2)',
            'marginBottom': '10px',
            'position': 'relative',
            'animation': 'slideIn 0.5s forwards'
        })
        
        container_style = {
            'position': 'fixed',
            'top': '80px',
            'right': '20px',
            'width': '350px',
            'maxWidth': '100%',
            'zIndex': '1000',
            'display': 'block'
        }
        
        return notification, container_style
    
    # Callback to close error notification when close button is clicked
    @app.callback(
        Output('error-store', 'data', allow_duplicate=True),
        [Input('close-error-button', 'n_clicks'),
         Input('error-dismiss-interval', 'n_intervals')],
        [State('error-store', 'data')],
        prevent_initial_call=True
    )
    def close_error_notification(n_clicks, n_intervals, error_data):
        if not error_data or not error_data.get('show', False):
            return no_update
        
        # Check if callback was triggered by button click or interval
        ctx = callback_context
        if not ctx.triggered:
            return no_update
        
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        # If button was clicked or interval fired, hide the notification
        if trigger_id == 'close-error-button' or trigger_id == 'error-dismiss-interval':
            return {'show': False, 'message': '', 'type': 'error', 'id': None}
        
        return no_update
