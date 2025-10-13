import streamlit as st
import pandas as pd
from PIL import Image
import time
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
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

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main theme */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        text-align: center;
        margin: 0;
        font-size: 2.5rem;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        text-align: center;
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
    }
    
    /* Card styling */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    /* Station selection styling */
    .station-selector {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    /* Route result styling */
    .route-result {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Metrics styling */
    .metric-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_city' not in st.session_state:
    st.session_state.selected_city = None
if 'route_path' not in st.session_state:
    st.session_state.route_path = None
if 'travel_time' not in st.session_state:
    st.session_state.travel_time = None

def get_metro_data(city):
    """Get metro data based on selected city"""
    if city == "Bengaluru":
        return bengaluru, "images/namma_metro.png", "images/bengaluru_map.jpg"
    elif city == "Delhi":
        return delhi, "images/delhi_metro.png", "images/delhi_map.jpg"
    return None, None, None

def calculate_fare(stations_count):
    """Calculate approximate fare based on number of stations"""
    if stations_count <= 3:
        return "₹10-15"
    elif stations_count <= 6:
        return "₹15-25"
    elif stations_count <= 10:
        return "₹25-40"
    else:
        return "₹40-60"

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

def create_route_visualization(path, city_name):
    """Create an interactive route visualization"""
    if not path or len(path) < 2:
        return None
    
    # Create a simple line plot showing the route
    fig = go.Figure()
    
    # Add route line
    fig.add_trace(go.Scatter(
        x=list(range(len(path))),
        y=[1] * len(path),
        mode='lines+markers+text',
        line=dict(color='#667eea', width=4),
        marker=dict(size=10, color='#764ba2'),
        text=[f"{i+1}. {station}" for i, station in enumerate(path)],
        textposition="top center",
        textfont=dict(size=10),
        name="Route"
    ))
    
    fig.update_layout(
        title=f"Route Visualization: {city_name} Metro",
        xaxis_title="Station Sequence",
        yaxis_title="",
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False)
    )
    
    return fig

# Main header
st.markdown("""
<div class="main-header fade-in">
    <h1>🚇 Metro Route Planner</h1>
    <p>Your smart companion for seamless metro travel across India's major cities</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for city selection
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
        
        # Quick facts
        if city == "Bengaluru":
            st.markdown("""
            **Quick Facts:**
            - 2 Operational Lines
            - Purple & Green Lines
            - 51 Stations
            - Connects IT Corridors
            """)
        elif city == "Delhi":
            st.markdown("""
            **Quick Facts:**
            - 8 Operational Lines
            - 285+ Stations
            - India's Largest Metro
            - Connects NCR
            """)

# Main content area
if st.session_state.selected_city:
    metro_data, logo_path, map_path = get_metro_data(st.session_state.selected_city)
    
    # Metro map display
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<h3 style='text-align: center; color: #667eea;'>{st.session_state.selected_city} Metro Network</h3>", unsafe_allow_html=True)
        if map_path:
            st.image(map_path, use_column_width=True, caption=f"{st.session_state.selected_city} Metro Map")
    
    # Station selection
    st.markdown('<div class="station-selector fade-in">', unsafe_allow_html=True)
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
    
    with col2:
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
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 Find Best Route", key="find_route", help="Click to find the shortest route"):
                with st.spinner("Finding the best route for you..."):
                    time.sleep(1)  # Simulate processing time
                    
                    route = find_shortest_path(metro_data, source_station, dest_station)
                    
                    if route:
                        st.session_state.route_path = route
                        stations_count = len(route) - 1
                        st.session_state.travel_time = estimate_travel_time(stations_count)
                        
                        # Display results
                        st.markdown('<div class="route-result fade-in">', unsafe_allow_html=True)
                        st.markdown(f"### 🎉 Route Found!")
                        
                        # Route metrics
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.markdown(f"""
                            <div class="metric-card">
                                <h4>📊 Stations</h4>
                                <h2>{stations_count}</h2>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            st.markdown(f"""
                            <div class="metric-card">
                                <h4>⏱️ Travel Time</h4>
                                <h2>{st.session_state.travel_time}</h2>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col3:
                            fare = calculate_fare(stations_count)
                            st.markdown(f"""
                            <div class="metric-card">
                                <h4>💰 Approx. Fare</h4>
                                <h2>{fare}</h2>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col4:
                            current_time = datetime.now()
                            arrival_time = current_time + timedelta(minutes=int(stations_count * 2.5) + 5)
                            st.markdown(f"""
                            <div class="metric-card">
                                <h4>🕐 Arrival</h4>
                                <h2>{arrival_time.strftime('%H:%M')}</h2>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Route details
                        st.markdown("### 📋 Your Journey Route")
                        
                        # Create route visualization
                        fig = create_route_visualization(route, st.session_state.selected_city)
                        if fig:
                            st.plotly_chart(fig, use_container_width=True)
                        
                        # Route steps
                        st.markdown("#### 🚉 Step-by-Step Directions")
                        route_df = pd.DataFrame({
                            'Step': range(1, len(route) + 1),
                            'Station': route,
                            'Action': ['Start here'] + ['Continue'] * (len(route) - 2) + ['You have arrived!']
                        })
                        st.dataframe(route_df, use_container_width=True, hide_index=True)
                        
                        # Return journey option
                        st.markdown("### 🔄 Return Journey")
                        if st.button("🔄 Get Return Route", help="Get the route back to your starting point"):
                            return_route = route[::-1]
                            return_df = pd.DataFrame({
                                'Step': range(1, len(return_route) + 1),
                                'Station': return_route,
                                'Action': ['Start return journey'] + ['Continue'] * (len(return_route) - 2) + ['Back at starting point!']
                            })
                            st.markdown("#### 🚉 Return Journey Route")
                            st.dataframe(return_df, use_container_width=True, hide_index=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    else:
                        st.error("❌ No route found between the selected stations. Please check your selections.")
    
    # Additional features section
    st.markdown("---")
    st.markdown("### 🌟 Additional Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🚇 Smart Route Planning</h4>
            <p>Advanced algorithms find the shortest and most efficient routes for your metro journey.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>💰 Fare Estimation</h4>
            <p>Get approximate fare estimates based on distance and station count for budget planning.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>⏱️ Time Estimation</h4>
            <p>Realistic travel time calculations including interchange and waiting times.</p>
        </div>
        """, unsafe_allow_html=True)

else:
    # Landing page when no city is selected
    st.markdown("""
    <div style="text-align: center; padding: 3rem;">
        <h2>🚇 Welcome to Metro Route Planner</h2>
        <p style="font-size: 1.2rem; color: #666;">Please select a city from the sidebar to start planning your metro journey!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature showcase
    st.markdown("### 🌟 What You Can Do")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Find Shortest Routes</h4>
            <p>Get the most efficient path between any two metro stations using advanced pathfinding algorithms.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Journey Analytics</h4>
            <p>View detailed journey information including travel time, fare estimates, and arrival times.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🔄 Return Journey</h4>
            <p>Instantly get your return route with a single click for complete journey planning.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📱 Mobile Friendly</h4>
            <p>Responsive design that works perfectly on all devices - desktop, tablet, and mobile.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>Built with ❤️ using Streamlit | © 2024 Metro Route Planner</p>
    <p>Supporting Bengaluru Namma Metro & Delhi Metro</p>
</div>
""", unsafe_allow_html=True)
