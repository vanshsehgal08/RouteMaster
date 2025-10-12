"""
Configuration file for Metro Route Planner
Contains app settings, themes, and customizable options
"""

# App Configuration
APP_CONFIG = {
    'name': 'Metro Route Planner',
    'version': '2.0.0',
    'author': 'Vansh Sehgal',
    'description': 'Advanced metro route planning with real-time insights',
    'github_url': 'https://github.com/vanshsehgal08/Metro-Project',
    'support_email': 'support@metroplanner.com'
}

# UI Themes
THEMES = {
    'default': {
        'primary_color': '#667eea',
        'secondary_color': '#764ba2',
        'success_color': '#00a651',
        'warning_color': '#ff6b6b',
        'info_color': '#00bfff',
        'background_gradient': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'card_background': 'rgba(255, 255, 255, 0.25)',
        'text_color': '#333333'
    },
    'dark': {
        'primary_color': '#4a5568',
        'secondary_color': '#2d3748',
        'success_color': '#38a169',
        'warning_color': '#ed8936',
        'info_color': '#4299e1',
        'background_gradient': 'linear-gradient(135deg, #2d3748 0%, #4a5568 100%)',
        'card_background': 'rgba(255, 255, 255, 0.1)',
        'text_color': '#ffffff'
    },
    'metro': {
        'primary_color': '#e53e3e',
        'secondary_color': '#dd6b20',
        'success_color': '#38a169',
        'warning_color': '#d69e2e',
        'info_color': '#3182ce',
        'background_gradient': 'linear-gradient(135deg, #e53e3e 0%, #dd6b20 100%)',
        'card_background': 'rgba(255, 255, 255, 0.2)',
        'text_color': '#1a202c'
    }
}

# Metro System Configuration
METRO_CONFIG = {
    'Bengaluru': {
        'name': 'Namma Metro',
        'operator': 'Bangalore Metro Rail Corporation Limited (BMRCL)',
        'opened': '2011',
        'total_stations': 51,
        'total_lines': 2,
        'network_length': '42.3 km',
        'daily_ridership': '5,00,000+',
        'website': 'https://english.bmrc.co.in/',
        'contact': '+91-80-2296-0300'
    },
    'Delhi': {
        'name': 'Delhi Metro',
        'operator': 'Delhi Metro Rail Corporation (DMRC)',
        'opened': '2002',
        'total_stations': '285+',
        'total_lines': 8,
        'network_length': '390+ km',
        'daily_ridership': '60,00,000+',
        'website': 'https://www.delhimetrorail.com/',
        'contact': '+91-11-2341-7910'
    }
}

# Fare Calculation Rules
FARE_RULES = {
    'Bengaluru': {
        'base_fare': 10,
        'per_station_rate': 2,
        'max_fare': 60,
        'concessions': {
            'senior_citizen': 0.5,
            'student': 0.25,
            'divyang': 0.0
        }
    },
    'Delhi': {
        'base_fare': 10,
        'per_station_rate': 2.5,
        'max_fare': 100,
        'concessions': {
            'senior_citizen': 0.5,
            'student': 0.25,
            'divyang': 0.0
        }
    }
}

# Travel Time Estimates
TRAVEL_TIME_CONFIG = {
    'minutes_per_station': 2.5,
    'interchange_time': 5,
    'waiting_time': 3,
    'peak_hour_multiplier': 1.3,
    'off_peak_multiplier': 0.8
}

# Operating Hours
OPERATING_HOURS = {
    'Bengaluru': {
        'weekday_first': '05:30',
        'weekday_last': '23:00',
        'weekend_first': '06:00',
        'weekend_last': '23:00',
        'frequency_peak': '3-5 minutes',
        'frequency_off_peak': '8-10 minutes'
    },
    'Delhi': {
        'weekday_first': '05:30',
        'weekday_last': '23:30',
        'weekend_first': '06:00',
        'weekend_last': '23:30',
        'frequency_peak': '2-3 minutes',
        'frequency_off_peak': '5-8 minutes'
    }
}

# Features Configuration
FEATURES = {
    'route_planning': True,
    'fare_calculation': True,
    'station_info': True,
    'interchange_info': True,
    'accessibility_info': True,
    'operating_hours': True,
    'real_time_updates': False,  # Future feature
    'multi_modal': False,  # Future feature
    'crowd_density': False,  # Future feature
    'weather_info': False  # Future feature
}

# Analytics Configuration
ANALYTICS_CONFIG = {
    'track_searches': True,
    'track_popular_routes': True,
    'track_user_preferences': False,  # Privacy-first approach
    'max_search_history': 10,
    'analytics_retention_days': 30
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    'cache_route_calculations': True,
    'cache_station_info': True,
    'cache_duration_minutes': 60,
    'max_concurrent_users': 1000,
    'response_time_threshold': 2.0  # seconds
}

# Accessibility Configuration
ACCESSIBILITY_CONFIG = {
    'screen_reader_support': True,
    'high_contrast_mode': True,
    'large_font_option': True,
    'keyboard_navigation': True,
    'voice_commands': False  # Future feature
}

# Social Features Configuration
SOCIAL_CONFIG = {
    'share_routes': True,
    'route_reviews': False,  # Future feature
    'community_tips': False,  # Future feature
    'social_login': False  # Future feature
}

# Export/Import Configuration
EXPORT_CONFIG = {
    'supported_formats': ['PDF', 'PNG', 'CSV'],
    'max_export_size': '10MB',
    'include_metadata': True,
    'custom_branding': False  # Future feature
}

# Notification Configuration
NOTIFICATION_CONFIG = {
    'route_alerts': False,  # Future feature
    'delay_notifications': False,  # Future feature
    'maintenance_updates': False,  # Future feature
    'promotional_messages': False
}

# Security Configuration
SECURITY_CONFIG = {
    'rate_limiting': True,
    'max_requests_per_minute': 60,
    'input_sanitization': True,
    'xss_protection': True,
    'csrf_protection': False  # Not needed for read-only app
}

def get_config(section, key=None):
    """Get configuration value"""
    config_sections = {
        'app': APP_CONFIG,
        'themes': THEMES,
        'metro': METRO_CONFIG,
        'fare': FARE_RULES,
        'travel_time': TRAVEL_TIME_CONFIG,
        'hours': OPERATING_HOURS,
        'features': FEATURES,
        'analytics': ANALYTICS_CONFIG,
        'performance': PERFORMANCE_CONFIG,
        'accessibility': ACCESSIBILITY_CONFIG,
        'social': SOCIAL_CONFIG,
        'export': EXPORT_CONFIG,
        'notifications': NOTIFICATION_CONFIG,
        'security': SECURITY_CONFIG
    }
    
    section_config = config_sections.get(section)
    if not section_config:
        return None
    
    if key:
        return section_config.get(key)
    
    return section_config

def get_metro_info(city):
    """Get metro system information"""
    return METRO_CONFIG.get(city, {})

def get_theme(theme_name='default'):
    """Get theme configuration"""
    return THEMES.get(theme_name, THEMES['default'])

def is_feature_enabled(feature_name):
    """Check if a feature is enabled"""
    return FEATURES.get(feature_name, False)
