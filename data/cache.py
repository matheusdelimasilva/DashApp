"""
Caching mechanism for data fetching functions.
"""

from functools import lru_cache
import numpy as np
from data.api import (
    get_continents, get_countries, get_states, get_cities,
    get_continent_data, get_country_data, get_state_data, get_city_data,
    get_data_fallback
)

# Cache system for data fetching functions
# Using lru_cache with maxsize to limit memory usage
@lru_cache(maxsize=128)
def fetch_data_with_cache(data_type, parent=None):
    """Generic caching wrapper for data fetching functions"""
    try:
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
    except Exception as e:
        # Simulate random errors for demonstration purposes
        if np.random.random() < 0.1:  # 10% chance of error
            raise Exception(f"Error fetching {data_type} data: {str(e)}")
        return get_data_fallback(data_type, parent)
