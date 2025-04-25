"""
Initialize and register all callbacks for the dashboard application.
"""

from callbacks.url_callbacks import register_url_callbacks
from callbacks.dropdown_callbacks import register_dropdown_callbacks
from callbacks.table_callbacks import register_table_callbacks
from callbacks.chart_callbacks import register_chart_callbacks
from callbacks.error_callbacks import register_error_callbacks

def register_callbacks(app):
    """Register all callbacks for the application"""
    register_url_callbacks(app)
    register_dropdown_callbacks(app)
    register_table_callbacks(app)
    register_chart_callbacks(app)
    register_error_callbacks(app)