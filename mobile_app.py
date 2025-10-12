import streamlit as st
import pandas as pd
from PIL import Image
import time
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from graph import bengaluru, delhi
from station_info import get_station_info, get_all_lines_for_city, calculate_fare

# Mobile-optimized page configuration
st.set_page_config(
    page_title="Metro Planner Mobile",
    page_icon="images/icon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/vanshsehgal08/Metro-Project',
        'Report a bug': "https://github.com/vanshsehgal08/Metro-Project/issues",
        'About': "# Metro Planner Mobile \nOptimized for mobile devices"
    }
)

# Mobile-first CSS
st.markdown("""
<style>
    /* Mobile-first responsive design */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Base styles */
    .main {
        padding: 0.5rem;
    }
    
    /* Mobile header */
    .mobile-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .mobile-header h1 {
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        margin: 0;
        font-size: 1.8rem;
    }
    
    .mobile-header p {
        color: rgba(255,255,255,0.9);
        margin: 0.5rem 0 0 0;
        font-size: 0.9rem;
    }
    
    /* Mobile cards */
    .mobile-card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    
    /* Mobile buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.9rem;
        width: 100%;
        margin: 0.5rem 0;
    }
    
    /* Mobile metrics */
    .mobile-metric {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    
    /* Mobile route display */
    .mobile-route {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main {
            padding: 0.25rem;
        }
        
        .mobile-header h1 {
            font-size: 1.5rem;
        }
        
        .mobile-card {
            padding: 0.75rem;
        }
    }
    
    /* Touch-friendly elements */
    .touch-friendly {
        min-height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

def get_metro_data(city):
    """Get metro data based on selected city"""
    if city == "Bengaluru":
        return bengaluru, "images/namma_metro.png", "images/bengaluru_map.jpg"
    elif city == "Delhi":
        return delhi, "images/delhi_metro.png", "images/delhi_map.jpg"
    return None, None, None

def estimate_travel_time(stations_count):
    """Estimate travel time based on number of stations"""
    minutes = stations_count * 2.5
    if stations_count > 1:
        minutes += 5
    return f"{int(minutes)}-{int(minutes + 5)} min"

def find_shortest_path(graph, start, end):
    """Find shortest path using BFS"""
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

# Initialize session state
if 'mobile_city' not in st.session_state:
    st.session_state.mobile_city = None

# Mobile header
st.markdown("""
<div class="mobile-header">
    <h1>🚇 Metro Planner</h1>
    <p>Quick & Easy Metro Route Planning</p>
</div>
""", unsafe_allow_html=True)

# City selection
st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
st.markdown("### 🏙️ Select City")
city = st.selectbox(
    "Choose Metro System",
    ["Bengaluru", "Delhi"],
    index=0,
    key="mobile_city_select"
)
st.markdown('</div>', unsafe_allow_html=True)

if city:
    st.session_state.mobile_city = city
    metro_data, logo_path, map_path = get_metro_data(city)
    
    # Quick stats
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="mobile-metric">
            <h3>{len(metro_data)}</h3>
            <p>Stations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        lines = get_all_lines_for_city(city)
        st.markdown(f"""
        <div class="mobile-metric">
            <h3>{len(lines)}</h3>
            <p>Lines</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Metro map
    if map_path:
        st.image(map_path, use_column_width=True, caption=f"{city} Metro Map")
    
    # Station selection
    st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Plan Journey")
    
    source_station = st.selectbox(
        "📍 From",
        sorted(metro_data.keys()),
        key="mobile_source"
    )
    
    dest_station = st.selectbox(
        "🎯 To",
        sorted(metro_data.keys()),
        key="mobile_dest"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Find route
    if source_station and dest_station:
        if st.button("🔍 Find Route", key="mobile_find", help="Find the best route"):
            with st.spinner("Finding route..."):
                time.sleep(1)
                
                route = find_shortest_path(metro_data, source_station, dest_station)
                
                if route:
                    stations_count = len(route) - 1
                    travel_time = estimate_travel_time(stations_count)
                    fare = calculate_fare(stations_count, city)
                    
                    # Results
                    st.markdown('<div class="mobile-route">', unsafe_allow_html=True)
                    st.markdown("### 🎉 Route Found!")
                    
                    # Quick metrics
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Stations", stations_count)
                    with col2:
                        st.metric("Time", travel_time)
                    with col3:
                        st.metric("Fare", fare)
                    
                    # Route steps
                    st.markdown("#### 🚉 Your Route")
                    for i, station in enumerate(route):
                        if i == 0:
                            st.markdown(f"**{i+1}.** 🚀 **{station}** (Start)")
                        elif i == len(route) - 1:
                            st.markdown(f"**{i+1}.** 🏁 **{station}** (Destination)")
                        else:
                            st.markdown(f"**{i+1}.** ➡️ **{station}**")
                    
                    # Return route
                    if st.button("🔄 Return Route", key="mobile_return"):
                        st.markdown("#### 🔄 Return Journey")
                        for i, station in enumerate(route[::-1]):
                            if i == 0:
                                st.markdown(f"**{i+1}.** 🚀 **{station}** (Start Return)")
                            elif i == len(route) - 1:
                                st.markdown(f"**{i+1}.** 🏁 **{station}** (Back Home)")
                            else:
                                st.markdown(f"**{i+1}.** ➡️ **{station}**")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                else:
                    st.error("❌ No route found. Please check your selections.")
    
    # Quick features
    st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
    st.markdown("### ⚡ Quick Features")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Line Info", key="line_info"):
            lines = get_all_lines_for_city(city)
            for line_name, line_data in lines.items():
                st.info(f"**{line_name}**: {line_data['stations_count']} stations")
    
    with col2:
        if st.button("🚉 Station Info", key="station_info"):
            station = st.selectbox("Select station", sorted(metro_data.keys()))
            if station:
                info = get_station_info(station)
                st.write(f"**{station}**")
                st.write(f"Amenities: {', '.join(info['amenities'][:3])}")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Mobile landing
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2 style="color: #667eea;">🚇 Metro Planner Mobile</h2>
        <p style="color: #666;">Select a city to start planning your metro journey!</p>
        <div style="font-size: 3rem; margin: 1rem 0;">📱 🚇 🎯</div>
    </div>
    """, unsafe_allow_html=True)

# Mobile footer
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #666; font-size: 0.8rem;">
    <p>🚇 Metro Planner Mobile | Built with ❤️</p>
</div>
""", unsafe_allow_html=True)
