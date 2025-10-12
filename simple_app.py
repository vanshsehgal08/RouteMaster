import streamlit as st
import pandas as pd
from PIL import Image
import time
from datetime import datetime, timedelta
from graph import bengaluru, delhi

# Page configuration
st.set_page_config(
    page_title="Metro Route Planner",
    page_icon="images/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/vanshsehgal08/Metro-Project',
        'Report a bug': "https://github.com/vanshsehgal08/Metro-Project/issues",
        'About': "# Metro Route Planner \nBuilt with ❤️ by Vansh Sehgal"
    }
)

# Dark Theme CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Dark theme background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #2a2a2a 100%);
        color: #ffffff;
    }
    
    /* Force dark theme */
    .main .block-container {
        background: transparent;
        color: #ffffff;
    }
    
    /* Override any gray backgrounds */
    .stApp > div {
        background: transparent !important;
    }
    
    /* Main content area */
    .main {
        padding-top: 1rem;
        background: transparent;
    }
    
    /* Main header with dark theme */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        text-align: center;
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .main-header h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        margin: 0;
        font-size: 3rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.95;
    }
    
    /* Dark theme feature cards */
    .feature-card {
        background: rgba(20, 20, 20, 0.9);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        color: #ffffff;
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
        background: rgba(26, 26, 46, 0.9);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    /* Dark station selector */
    .station-selector {
        background: linear-gradient(135deg, rgba(20, 20, 20, 0.9) 0%, rgba(30, 30, 30, 0.9) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: #ffffff;
    }
    
    /* Dark route result */
    .route-result {
        background: linear-gradient(135deg, rgba(20, 20, 20, 0.9) 0%, rgba(30, 30, 30, 0.9) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: #ffffff;
    }
    
    /* Dark metric cards */
    .metric-card {
        background: rgba(20, 20, 20, 0.9);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        border-left: 4px solid #667eea;
        color: #ffffff;
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
    
    /* Dark buttons */
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
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
    }
    
    /* Dark sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a1a1a 50%, #2a2a2a 100%);
        border-right: 2px solid rgba(102, 126, 234, 0.3);
    }
    
    /* Sidebar content styling */
    .css-1d391kg .stMarkdown {
        color: #ffffff !important;
    }
    
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6 {
        color: #ffffff !important;
    }
    
    .css-1d391kg p {
        color: #ffffff !important;
    }
    
    /* Sidebar metric styling */
    .css-1d391kg .metric-container {
        background: rgba(26, 26, 46, 0.8) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }
    
    /* Sidebar selectbox styling */
    .css-1d391kg .stSelectbox > div > div {
        background-color: rgba(26, 26, 46, 0.9) !important;
        border: 1px solid rgba(102, 126, 234, 0.4) !important;
        color: #ffffff !important;
    }
    
    .css-1d391kg .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Dark selectboxes and inputs */
    .stSelectbox > div > div {
        background-color: rgba(26, 26, 46, 0.8);
        border: 1px solid rgba(102, 126, 234, 0.3);
        color: #ffffff;
    }
    
    .stSelectbox label {
        color: #ffffff !important;
    }
    
    /* Dark dataframe styling */
    .dataframe {
        background-color: rgba(26, 26, 46, 0.8) !important;
        color: #ffffff !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
    }
    
    .dataframe th {
        background-color: rgba(102, 126, 234, 0.3) !important;
        color: #ffffff !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
    }
    
    .dataframe td {
        background-color: rgba(26, 26, 46, 0.6) !important;
        color: #ffffff !important;
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Text color fixes */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    p, div {
        color: #ffffff;
    }
    
    /* Metric styling */
    .metric {
        color: #ffffff !important;
    }
    
    .metric > div {
        background-color: rgba(26, 26, 46, 0.8) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_city' not in st.session_state:
    st.session_state.selected_city = None
if 'route_path' not in st.session_state:
    st.session_state.route_path = None
if 'show_map' not in st.session_state:
    st.session_state.show_map = False

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
    minutes = stations_count * 2.5
    if stations_count > 1:
        minutes += 5
    return f"{int(minutes)}-{int(minutes + 5)} minutes"

def find_shortest_path(graph, start, end):
    """Enhanced shortest path algorithm with BFS"""
    if start == end:
        return [start]
    
    if start not in graph or end not in graph:
        return None
    
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

# Main header
st.markdown("""
<div class="main-header fade-in-up">
    <h1>🚇 Metro Route Planner</h1>
    <p>Your smart companion for seamless metro travel across India's major cities</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for city selection with dark theme
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
        
        st.markdown(f"### 📊 {city} Metro Stats")
        total_stations = len(metro_data)
        st.metric("Total Stations", total_stations)
        
        # Quick facts based on city
        if city == "Bengaluru":
            st.markdown("""
            **🚇 Quick Facts:**
            - **2 Operational Lines**
            - **Purple & Green Lines**
            - **51 Stations**
            - **Connects IT Corridors**
            - **42.3 km Network**
            - **5 Lakh+ Daily Riders**
            """)
            
            # Line information for Bengaluru
            st.markdown("### 🚇 Metro Lines")
            st.markdown("""
            **🟣 Purple Line**
            - NAGASANDRA → BAIYYAPANAHALLI
            - 23 Stations
            
            **🟢 Green Line**
            - YELACHENAHALLI → SILK INSTITUTE
            - 16 Stations
            """)
            
        elif city == "Delhi":
            st.markdown("""
            **🚇 Quick Facts:**
            - **8 Operational Lines**
            - **285+ Stations**
            - **India's Largest Metro**
            - **Connects NCR**
            - **390+ km Network**
            - **60 Lakh+ Daily Riders**
            """)
            
            # Line information for Delhi
            st.markdown("### 🚇 Major Lines")
            st.markdown("""
            **🔴 Red Line** - SHAHEED STHAL → RITHALA
            **🟡 Yellow Line** - HUDA CITY CENTRE → SHIV VIHAR
            **🔵 Blue Line** - DWARKA SECTOR-21 → NOIDA ELECTRONIC CITY
            **🟣 Violet Line** - KASHMERE GATE → RAJA NAHAR SINGH
            """)

# Main content area
if st.session_state.selected_city:
    metro_data, logo_path, map_path = get_metro_data(st.session_state.selected_city)
    
    # Metro map display with toggle button
    city_name = "Bengaluru Namma Metro" if st.session_state.selected_city == "Bengaluru" else "Delhi Metro"
    st.markdown(f"<h3 style='text-align: center; color: #667eea; font-weight: 600;'>{city_name} Network</h3>", unsafe_allow_html=True)
    
    # Map toggle button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if not st.session_state.show_map:
            if st.button("🗺️ Show Metro Map", key="show_map_btn", help="Click to view the metro network map"):
                st.session_state.show_map = True
                st.rerun()
        else:
            if st.button("❌ Hide Metro Map", key="hide_map_btn", help="Click to hide the metro network map"):
                st.session_state.show_map = False
                st.rerun()
    
    # Show map if toggled on
    if st.session_state.show_map and map_path:
        st.image(map_path, use_column_width=True, caption=f"{city_name} Map")
    
# Station selection
st.markdown("### 🎯 Plan Your Journey")

st.markdown("**📍 Starting Station**")
source_station = st.selectbox(
    "Select your starting station",
    sorted(metro_data.keys()),
    key="source",
    help="Choose where you want to start your journey"
)

st.markdown("**🎯 Destination Station**")
dest_station = st.selectbox(
    "Select your destination",
    sorted(metro_data.keys()),
    key="destination",
    help="Choose your final destination"
)

st.markdown('</div>', unsafe_allow_html=True)
    
# Journey planning
if source_station and dest_station:
    if st.button("🔍 Find Best Route", key="find_route", help="Click to find the shortest route"):
        with st.spinner("Finding the best route for you..."):
            time.sleep(1)
            
            route = find_shortest_path(metro_data, source_station, dest_station)
            
            if route:
                st.session_state.route_path = route
                stations_count = len(route) - 1
                travel_time = estimate_travel_time(stations_count)
                
                # Display results
                st.markdown('<div class="route-result fade-in-up">', unsafe_allow_html=True)
                st.markdown(f"### 🎉 Route Found!")
                
                # Route metrics
                st.markdown("""
                <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin: 1rem 0;">
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="metric-card" style="flex: 1; min-width: 200px; margin: 0.5rem;">
                    <h4>📊 Stations</h4>
                    <h2>{stations_count}</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="metric-card" style="flex: 1; min-width: 200px; margin: 0.5rem;">
                    <h4>⏱️ Travel Time</h4>
                    <h2>{travel_time}</h2>
                </div>
                """, unsafe_allow_html=True)
                
                fare = calculate_fare(stations_count, st.session_state.selected_city)
                st.markdown(f"""
                <div class="metric-card" style="flex: 1; min-width: 200px; margin: 0.5rem;">
                    <h4>💰 Approx. Fare</h4>
                    <h2>{fare}</h2>
                </div>
                """, unsafe_allow_html=True)
                
                current_time = datetime.now()
                arrival_time = current_time + timedelta(minutes=int(stations_count * 2.5) + 5)
                st.markdown(f"""
                <div class="metric-card" style="flex: 1; min-width: 200px; margin: 0.5rem;">
                    <h4>🕐 Arrival</h4>
                    <h2>{arrival_time.strftime('%H:%M')}</h2>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Route details
                st.markdown("### 📋 Your Journey Route")
                
                # Route steps
                st.markdown("#### 🚉 Step-by-Step Directions")
                route_data = []
                for i, station in enumerate(route):
                    action = "Start here" if i == 0 else "You have arrived!" if i == len(route)-1 else "Continue"
                    route_data.append({
                        'Step': i + 1,
                        'Station': station,
                        'Action': action
                    })
                
                route_df = pd.DataFrame(route_data)
                st.dataframe(route_df, use_container_width=True, hide_index=True)
                
                # Return journey option
                st.markdown("### 🔄 Return Journey")
                if st.button("🔄 Get Return Route", help="Get the route back to your starting point"):
                    return_route = route[::-1]
                    return_data = []
                    for i, station in enumerate(return_route):
                        action = "Start return journey" if i == 0 else "Back at starting point!" if i == len(return_route)-1 else "Continue"
                        return_data.append({
                            'Step': i + 1,
                            'Station': station,
                            'Action': action
                        })
                    
                    return_df = pd.DataFrame(return_data)
                    st.markdown("#### 🚉 Return Journey Route")
                    st.dataframe(return_df, use_container_width=True, hide_index=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
            else:
                st.error("❌ No route found between the selected stations. Please check your selections.")
    
# Additional features section
st.markdown("---")
st.markdown("### 🌟 Features")

st.markdown("""
<div class="feature-card">
    <h4>🚇 Smart Route Planning</h4>
    <p>Advanced algorithms find the shortest and most efficient routes for your metro journey.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <h4>💰 Fare Estimation</h4>
    <p>Get approximate fare estimates based on distance and station count for budget planning.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <h4>⏱️ Time Estimation</h4>
    <p>Realistic travel time calculations including interchange and waiting times.</p>
</div>
""", unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #ffffff;">
    <p>Built with ❤️ using Streamlit | © 2024 Metro Route Planner</p>
    <p>Supporting Bengaluru Namma Metro & Delhi Metro | Your Smart Metro Companion</p>
</div>
""", unsafe_allow_html=True)
