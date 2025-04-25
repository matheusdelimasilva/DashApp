"""
Data API functions for the dashboard application.
These functions simulate API calls to fetch geographic data.
"""

import time
import numpy as np

def get_continents():
    """Fetch list of continents from server"""
    # Simulate network delay
    time.sleep(0.5)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception("Network error while fetching continents data")

    return ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']

def get_countries(continent):
    """Fetch countries for a given continent from server"""
    if not continent:
        return []

    # Simulate network delay
    time.sleep(0.8)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"Database error while fetching countries for {continent}")

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
    time.sleep(0.7)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"API timeout while fetching states for {country}")

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
    time.sleep(0.6)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"Server error while fetching cities for {state}")

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
    time.sleep(1.0)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"Data service unavailable for {continent} information")

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
    time.sleep(0.9)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"Authentication error while fetching data for {country}")

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
    time.sleep(0.8)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"Connection error while fetching data for {state}")

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
    time.sleep(0.7)

    # Simulate random error (for demonstration)
    if np.random.random() < 0.05:  # 5% chance of error
        raise Exception(f"Rate limit exceeded while fetching data for {city}")

    city_data = {
        'Los Angeles': {'Population': '3.9 million', 'Area': '1,302 km²',
                       'Mayor': 'Karen Bass', 'Founded': '1781', 'Famous For': 'Hollywood'},
        'New York City': {'Population': '8.4 million', 'Area': '783.8 km²',
                         'Mayor': 'Eric Adams', 'Founded': '1624', 'Famous For': 'Wall Street'},
        'London': {'Population': '8.9 million', 'Area': '1,572 km²',
                  'Mayor': 'Sadiq Khan', 'Founded': '43 AD', 'Famous For': 'Big Ben'}
    }

    return city_data.get(city, {})

def get_data_fallback(data_type, parent=None):
    """Fallback data in case of errors"""
    if data_type == 'continents':
        return ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']
    elif data_type == 'countries':
        return []
    elif data_type == 'states':
        return []
    elif data_type == 'cities':
        return []
    elif data_type in ['continent_data', 'country_data', 'state_data', 'city_data']:
        return {}
    return None
