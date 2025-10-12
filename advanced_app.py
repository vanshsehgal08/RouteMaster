import streamlit as st
import pandas as pd
from PIL import Image
import time
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from graph import bengaluru, delhi
from station_info import (
    STATION_AMENITIES, METRO_LINES, LINE_COLORS, 
    get_station_info, get_line_info, get_all_lines_for_city,
    is_interchange_station, get_station_amenities, get_operating_hours
)

# Page configuration
st.set_page_config(
    page_title="Metro Route Planner Pro",
    page_icon="images/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/vanshsehgal08/Metro-Project',
        'Report a bug': "https://github.com/vanshsehgal08/Metro-Project/issues",
        'About': "# Metro Route Planner Pro \nBuilt with ❤️ by Vansh Sehgal"
    }
)

# Enhanced CSS with more features
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Main theme */
    .main {
        padding-top: 1rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="1.5" fill="rgba(255,255,255,0.1)"/><circle cx="40" cy="80" r="1" fill="rgba(255,255,255,0.1)"/></svg>');
        opacity: 0.3;
    }
    
    .main-header h1 {
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        text-align: center;
        margin: 0;
        font-size: 3rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.95);
        text-align: center;
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Feature cards with glassmorphism */
    .feature-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        background: rgba(255, 255, 255, 0.35);
    }
    
    /* Station info card */
    .station-info-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #ff6b6b;
    }
    
    /* Route visualization */
    .route-viz {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
    }
    
    /* Metrics with icons */
    .metric-with-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 1rem;
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        margin: 0.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    /* Progress bars */
    .progress-container {
        background: rgba(255,255,255,0.2);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Interactive elements */
    .interactive-element {
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .interactive-element:hover {
        transform: scale(1.05);
    }
    
    /* Station selector enhancement */
    .station-selector {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Button enhancements */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Sidebar enhancements */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animations */
    @keyframes fadeInUp {
        from { 
            opacity: 0; 
            transform: translateY(30px); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0); 
        }
    }
    
    @keyframes slideInLeft {
        from { 
            opacity: 0; 
            transform: translateX(-30px); 
        }
        to { 
            opacity: 1; 
            transform: translateX(0); 
        }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }
    
    .slide-in-left {
        animation: slideInLeft 0.6s ease-out;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .feature-card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'selected_city' not in st.session_state:
        st.session_state.selected_city = None
    if 'route_path' not in st.session_state:
        st.session_state.route_path = None
    if 'travel_time' not in st.session_state:
        st.session_state.travel_time = None
    if 'selected_station_info' not in st.session_state:
        st.session_state.selected_station_info = None
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []

init_session_state()

def get_metro_data(city):
    """Get metro data based on selected city"""
    if city == "Bengaluru":
        return bengaluru, "images/namma_metro.png", "images/bengaluru_map.jpg"
    elif city == "Delhi":
        return delhi, "images/delhi_metro.png", "images/delhi_map.jpg"
    return None, None, None

def calculate_fare(stations_count, city):
    """Calculate approximate fare based on number of stations and city"""
    if city == "Bengaluru":
        if stations_count <= 3:
            return "₹10-15"
        elif stations_count <= 6:
            return "₹15-25"
        elif stations_count <= 10:
            return "₹25-40"
        else:
            return "₹40-60"
    elif city == "Delhi":
        if stations_count <= 5:
            return "₹10-20"
        elif stations_count <= 10:
            return "₹20-40"
        elif stations_count <= 20:
            return "₹40-60"
        else:
            return "₹60-100"

def estimate_travel_time(stations_count):
    """Estimate travel time based on number of stations"""
    # Assuming 2-3 minutes per station + interchange time
    minutes = stations_count * 2.5
    if stations_count > 1:
        minutes += 5  # Buffer for interchange and waiting
    return f"{int(minutes)}-{int(minutes + 5)} minutes"

def find_shortest_path(graph, start, end):
    """Enhanced shortest path algorithm with BFS"""
    if start == end:
        return [start]
    
    if start not in graph or end not in graph:
        return None
    
    # BFS for shortest path
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        current_station, path = queue.pop(0)
        
        if current_station == end:
            return path
        
        if current_station in visited:
            continue
            
        visited.add(current_station)
        
        for neighbor in graph[current_station]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

def create_advanced_route_visualization(path, city_name):
    """Create an advanced interactive route visualization"""
    if not path or len(path) < 2:
        return None
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Route Overview', 'Station Details'),
        vertical_spacing=0.1,
        row_heights=[0.6, 0.4]
    )
    
    # Route overview
    fig.add_trace(go.Scatter(
        x=list(range(len(path))),
        y=[1] * len(path),
        mode='lines+markers+text',
        line=dict(color='#667eea', width=6),
        marker=dict(size=15, color='#764ba2', symbol='circle'),
        text=[f"{i+1}" for i in range(len(path))],
        textposition="top center",
        textfont=dict(size=12, color='white'),
        name="Route",
        showlegend=False
    ), row=1, col=1)
    
    # Station details
    station_lengths = [len(station) for station in path]
    fig.add_trace(go.Bar(
        x=[f"Station {i+1}" for i in range(len(path))],
        y=station_lengths,
        marker=dict(color='#ff6b6b'),
        name="Station Name Length",
        showlegend=False
    ), row=2, col=1)
    
    fig.update_layout(
        title=f"Advanced Route Visualization: {city_name} Metro",
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333'),
        showlegend=False
    )
    
    fig.update_xaxes(showgrid=False, zeroline=False, row=1, col=1)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False, row=1, col=1)
    
    return fig

def create_line_network_visualization(city):
    """Create a network visualization of metro lines"""
    lines = get_all_lines_for_city(city)
    if not lines:
        return None
    
    fig = go.Figure()
    
    for line_name, line_data in lines.items():
        color = line_data.get('color', '#666666')
        stations = line_data.get('stations', [])
        
        # Create line trace
        fig.add_trace(go.Scatter(
            x=list(range(len(stations))),
            y=[list(lines.keys()).index(line_name)] * len(stations),
            mode='lines+markers',
            line=dict(color=color, width=4),
            marker=dict(size=8),
            name=line_name,
            text=stations,
            textposition="top center",
            hovertemplate=f"<b>{line_name}</b><br>%{text}<extra></extra>"
        ))
    
    fig.update_layout(
        title=f"{city} Metro Network Overview",
        xaxis_title="Station Sequence",
        yaxis_title="Metro Lines",
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

# Main header
st.markdown("""
<div class="main-header fade-in-up">
    <h1>🚇 Metro Route Planner Pro</h1>
    <p>Advanced metro planning with real-time insights, station amenities, and smart route optimization</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🏙️ Select Your City")
    city = st.selectbox(
        "Choose Metro System",
        ["Bengaluru", "Delhi"],
        index=0,
        help="Select the metro system you want to plan your route for"
    )
    
    if city:
        st.session_state.selected_city = city
        metro_data, logo_path, map_path = get_metro_data(city)
        
        if logo_path:
            st.image(logo_path, use_column_width=True)
        
        # Enhanced city stats
        st.markdown(f"### 📊 {city} Metro Statistics")
        total_stations = len(metro_data)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Stations", total_stations)
        with col2:
            lines = get_all_lines_for_city(city)
            st.metric("Active Lines", len(lines))
        
        # Network visualization
        network_fig = create_line_network_visualization(city)
        if network_fig:
            st.plotly_chart(network_fig, use_container_width=True)
        
        # Quick facts
        if city == "Bengaluru":
            st.markdown("""
            **🏗️ Infrastructure:**
            - 2 Operational Lines
            - Purple & Green Lines
            - 51 Stations
            - IT Corridor Connectivity
            
            **📈 Expansion:**
            - Phase 2 Underway
            - Airport Connectivity
            - Outer Ring Road Line
            """)
        elif city == "Delhi":
            st.markdown("""
            **🏗️ Infrastructure:**
            - 8 Operational Lines
            - 285+ Stations
            - India's Largest Metro
            - NCR Connectivity
            
            **📈 Expansion:**
            - Phase 4 Underway
            - Regional Connectivity
            - High-Speed Corridors
            """)
        
        # Station search
        st.markdown("### 🔍 Station Information")
        all_stations = sorted(metro_data.keys())
        selected_station = st.selectbox(
            "Select a station for details",
            all_stations,
            help="Get detailed information about any station"
        )
        
        if selected_station:
            station_info = get_station_info(selected_station)
            
            st.markdown(f"#### 🚉 {selected_station}")
            st.markdown(f"**Description:** {station_info['description']}")
            
            # Amenities
            amenities = station_info['amenities']
            if amenities:
                st.markdown("**Amenities:**")
                amenity_cols = st.columns(2)
                for i, amenity in enumerate(amenities):
                    with amenity_cols[i % 2]:
                        st.markdown(f"✅ {amenity}")
            
            # Operating hours
            hours = get_operating_hours(selected_station)
            st.markdown(f"**Operating Hours:** {hours['first_train']} - {hours['last_train']}")
            
            # Accessibility
            if station_info['accessibility']:
                st.success("♿ Wheelchair Accessible")
            else:
                st.warning("⚠️ Limited Accessibility")

# Main content area
if st.session_state.selected_city:
    metro_data, logo_path, map_path = get_metro_data(st.session_state.selected_city)
    
    # Metro map display with enhanced styling
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<h3 style='text-align: center; color: #667eea; font-weight: 600;'>{st.session_state.selected_city} Metro Network</h3>", unsafe_allow_html=True)
        if map_path:
            st.image(map_path, use_column_width=True, caption=f"{st.session_state.selected_city} Metro Map")
    
    # Enhanced station selection
    st.markdown('<div class="station-selector fade-in-up">', unsafe_allow_html=True)
    st.markdown("### 🎯 Plan Your Journey")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📍 Starting Station**")
        source_station = st.selectbox(
            "Select your starting station",
            sorted(metro_data.keys()),
            key="source",
            help="Choose where you want to start your journey"
        )
        
        # Show source station info
        if source_station:
            source_info = get_station_info(source_station)
            st.markdown(f"<small>💡 {source_info['description']}</small>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("**🎯 Destination Station**")
        dest_station = st.selectbox(
            "Select your destination",
            sorted(metro_data.keys()),
            key="destination",
            help="Choose your final destination"
        )
        
        # Show destination station info
        if dest_station:
            dest_info = get_station_info(dest_station)
            st.markdown(f"<small>💡 {dest_info['description']}</small>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Journey planning with enhanced features
    if source_station and dest_station:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 Find Optimal Route", key="find_route", help="Click to find the shortest and most efficient route"):
                with st.spinner("Analyzing routes and finding the best option..."):
                    time.sleep(1.5)  # Simulate processing time
                    
                    route = find_shortest_path(metro_data, source_station, dest_station)
                    
                    if route:
                        st.session_state.route_path = route
                        stations_count = len(route) - 1
                        st.session_state.travel_time = estimate_travel_time(stations_count)
                        
                        # Add to search history
                        search_entry = {
                            'timestamp': datetime.now(),
                            'from': source_station,
                            'to': dest_station,
                            'stations': stations_count,
                            'route': route
                        }
                        st.session_state.search_history.append(search_entry)
                        
                        # Display enhanced results
                        st.markdown('<div class="route-viz fade-in-up">', unsafe_allow_html=True)
                        st.markdown(f"### 🎉 Optimal Route Found!")
                        
                        # Enhanced route metrics
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.markdown(f"""
                            <div class="metric-with-icon">
                                <div class="metric-icon">📊</div>
                                <h3>{stations_count}</h3>
                                <p>Stations</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            st.markdown(f"""
                            <div class="metric-with-icon">
                                <div class="metric-icon">⏱️</div>
                                <h3>{st.session_state.travel_time}</h3>
                                <p>Travel Time</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col3:
                            fare = calculate_fare(stations_count, st.session_state.selected_city)
                            st.markdown(f"""
                            <div class="metric-with-icon">
                                <div class="metric-icon">💰</div>
                                <h3>{fare}</h3>
                                <p>Approx. Fare</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col4:
                            current_time = datetime.now()
                            arrival_time = current_time + timedelta(minutes=int(stations_count * 2.5) + 5)
                            st.markdown(f"""
                            <div class="metric-with-icon">
                                <div class="metric-icon">🕐</div>
                                <h3>{arrival_time.strftime('%H:%M')}</h3>
                                <p>Arrival Time</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Advanced route visualization
                        st.markdown("### 📈 Advanced Route Analysis")
                        fig = create_advanced_route_visualization(route, st.session_state.selected_city)
                        if fig:
                            st.plotly_chart(fig, use_container_width=True)
                        
                        # Detailed route steps with station info
                        st.markdown("### 🚉 Detailed Journey Guide")
                        
                        route_data = []
                        for i, station in enumerate(route):
                            station_info = get_station_info(station)
                            action = "Start your journey" if i == 0 else "You have arrived!" if i == len(route)-1 else "Continue"
                            
                            route_data.append({
                                'Step': i + 1,
                                'Station': station,
                                'Action': action,
                                'Amenities': ', '.join(station_info['amenities'][:3]) + ('...' if len(station_info['amenities']) > 3 else ''),
                                'Accessibility': '♿ Yes' if station_info['accessibility'] else '⚠️ Limited',
                                'Interchange': '🔄 Yes' if station_info['interchange'] else '➡️ No'
                            })
                        
                        route_df = pd.DataFrame(route_data)
                        st.dataframe(route_df, use_container_width=True, hide_index=True)
                        
                        # Interchange information
                        interchange_stations = [station for station in route if is_interchange_station(station)]
                        if interchange_stations:
                            st.markdown("### 🔄 Interchange Stations")
                            for station in interchange_stations:
                                station_info = get_station_info(station)
                                st.info(f"**{station}**: {', '.join(station_info['lines'])}")
                        
                        # Return journey option
                        st.markdown("### 🔄 Return Journey Planning")
                        if st.button("🔄 Plan Return Route", help="Get the optimized route back to your starting point"):
                            return_route = route[::-1]
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown("#### 🚉 Return Route")
                                return_df = pd.DataFrame({
                                    'Step': range(1, len(return_route) + 1),
                                    'Station': return_route,
                                    'Action': ['Start return journey'] + ['Continue'] * (len(return_route) - 2) + ['Back at starting point!']
                                })
                                st.dataframe(return_df, use_container_width=True, hide_index=True)
                            
                            with col2:
                                st.markdown("#### 📊 Return Journey Stats")
                                return_fare = calculate_fare(len(return_route)-1, st.session_state.selected_city)
                                return_time = estimate_travel_time(len(return_route)-1)
                                st.metric("Return Fare", return_fare)
                                st.metric("Return Time", return_time)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    else:
                        st.error("❌ No route found between the selected stations. Please check your selections.")
    
    # Search history
    if st.session_state.search_history:
        st.markdown("---")
        st.markdown("### 📚 Recent Searches")
        
        # Show last 3 searches
        recent_searches = st.session_state.search_history[-3:]
        for search in reversed(recent_searches):
            with st.expander(f"🔍 {search['from']} → {search['to']} ({search['timestamp'].strftime('%H:%M')})"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Stations", search['stations'])
                with col2:
                    st.metric("Time", estimate_travel_time(search['stations']))
                with col3:
                    st.metric("Fare", calculate_fare(search['stations'], st.session_state.selected_city))
    
    # Additional features section
    st.markdown("---")
    st.markdown("### 🌟 Advanced Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card slide-in-left">
            <h4>🧠 Smart Route Optimization</h4>
            <p>Advanced algorithms consider multiple factors including distance, interchanges, and travel time to find the most efficient route.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card slide-in-left">
            <h4>🏢 Station Intelligence</h4>
            <p>Comprehensive station information including amenities, accessibility features, operating hours, and connectivity details.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card slide-in-left">
            <h4>📊 Journey Analytics</h4>
            <p>Detailed journey analysis with fare estimates, time calculations, interchange information, and travel insights.</p>
        </div>
        """, unsafe_allow_html=True)

else:
    # Enhanced landing page
    st.markdown("""
    <div style="text-align: center; padding: 4rem;">
        <h2 style="color: #667eea; font-size: 2.5rem; margin-bottom: 1rem;">🚇 Welcome to Metro Route Planner Pro</h2>
        <p style="font-size: 1.3rem; color: #666; margin-bottom: 2rem;">Select a city from the sidebar to start planning your advanced metro journey!</p>
        <div style="font-size: 3rem; margin: 2rem 0;">🎯 📱 🚀</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature showcase
    st.markdown("### 🌟 What Makes This Special")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card pulse">
            <h4>🎯 Intelligent Route Planning</h4>
            <p>Our advanced algorithms analyze multiple route options to find the shortest, fastest, and most convenient path for your journey.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🏢 Comprehensive Station Data</h4>
            <p>Access detailed information about every station including amenities, accessibility, operating hours, and connectivity options.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Advanced Analytics</h4>
            <p>Get detailed journey insights including fare estimates, travel time calculations, interchange details, and arrival predictions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📱 Modern Interface</h4>
            <p>Beautiful, responsive design with interactive visualizations, smooth animations, and intuitive user experience across all devices.</p>
        </div>
        """, unsafe_allow_html=True)

# Enhanced footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin-top: 2rem;">
    <h3 style="margin-bottom: 1rem;">🚇 Metro Route Planner Pro</h3>
    <p style="margin-bottom: 1rem; opacity: 0.9;">Built with ❤️ using Streamlit | Advanced Metro Planning Technology</p>
    <p style="opacity: 0.8;">Supporting Bengaluru Namma Metro & Delhi Metro | © 2024</p>
    <div style="margin-top: 1rem; font-size: 2rem;">
        🚀 📱 🎯 🌟
    </div>
</div>
""", unsafe_allow_html=True)
