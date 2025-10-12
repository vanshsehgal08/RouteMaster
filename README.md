# 🚇 Metro Route Planner Pro

**Metro Route Planner Pro** is an advanced web application built using **Python** and **Streamlit** that provides comprehensive metro route planning for **Delhi** and **Bangalore** metro systems. The application features a modern UI, intelligent route optimization, and detailed station information.

## 🌟 Features

### Core Features
- **🧠 Smart Route Planning**: Advanced algorithms find the shortest and most efficient routes
- **💰 Fare Calculator**: Accurate fare estimation based on distance and station count
- **⏱️ Travel Time Estimation**: Realistic travel time calculations including interchange time
- **🔄 Return Journey**: One-click return route planning
- **📊 Journey Analytics**: Detailed insights with metrics and visualizations

### Advanced Features
- **🏢 Station Intelligence**: Comprehensive station information including amenities and accessibility
- **🎨 Modern UI**: Beautiful, responsive design with animations and glassmorphism effects
- **📱 Mobile Optimized**: Fully responsive design for all devices
- **🔍 Interactive Visualizations**: Route maps and network diagrams using Plotly
- **📚 Search History**: Track recent searches for quick access
- **♿ Accessibility Info**: Wheelchair accessibility and facility information

### Metro Systems Supported
- **Bengaluru Namma Metro**: 51 stations across Purple and Green lines
- **Delhi Metro**: 285+ stations across 8 operational lines

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/vanshsehgal08/Metro-Project.git
    cd Metro-Project
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

   **Main Application (Recommended)**:
   ```bash
   streamlit run app.py
   ```

   **Advanced Features**:
   ```bash
   streamlit run advanced_app.py
   ```

   **Mobile Optimized**:
   ```bash
   streamlit run mobile_app.py
   ```

   **Original Versions**:
   ```bash
   streamlit run Bengaluru.py    # For Bengaluru only
   streamlit run pages/Delhi.py  # For Delhi only
   ```

## 📱 Usage

### Basic Route Planning
1. **Select City**: Choose either Bengaluru or Delhi from the sidebar
2. **Choose Stations**: Select your starting and destination stations
3. **Find Route**: Click "Find Route" to get the optimal path
4. **View Results**: See detailed route information, travel time, and fare estimates

### Advanced Features
- **Station Information**: Click on any station to see amenities, accessibility, and operating hours
- **Route Visualization**: Interactive maps showing your journey path
- **Return Journey**: Instantly plan your return trip
- **Search History**: Access your recent searches for quick planning

### Mobile Usage
- Optimized for touch interfaces
- Swipe-friendly navigation
- Quick access to popular features
- Responsive design for all screen sizes

## 🏗️ Project Structure

```
Metro-Project/
├── app.py                 # Main unified application
├── advanced_app.py        # Advanced features version
├── mobile_app.py          # Mobile-optimized version
├── Bengaluru.py           # Original Bengaluru app
├── pages/
│   └── Delhi.py          # Original Delhi app
├── graph.py              # Metro network data
├── station_info.py       # Station details and amenities
├── config.py             # Configuration and settings
├── requirements.txt      # Python dependencies
├── images/               # Metro maps and logos
│   ├── bengaluru_map.jpg
│   ├── delhi_map.jpg
│   ├── namma_metro.png
│   ├── delhi_metro.png
│   └── icon.png
└── README.md            # This file
```

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.7+**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations

### UI/UX Technologies
- **CSS3**: Advanced styling with gradients and animations
- **HTML5**: Semantic markup
- **Google Fonts**: Typography (Inter font family)
- **Responsive Design**: Mobile-first approach

### Algorithms
- **Breadth-First Search (BFS)**: Shortest path finding
- **Graph Theory**: Metro network representation
- **Dynamic Programming**: Route optimization

## 🎨 UI/UX Features

### Modern Design Elements
- **Glassmorphism**: Frosted glass effects with backdrop blur
- **Gradient Backgrounds**: Beautiful color transitions
- **Smooth Animations**: CSS transitions and keyframe animations
- **Interactive Elements**: Hover effects and micro-interactions

### Responsive Design
- **Mobile-First**: Optimized for mobile devices
- **Tablet Support**: Perfect layout for tablets
- **Desktop Enhancement**: Enhanced features for larger screens
- **Touch-Friendly**: Large touch targets and swipe gestures

### Accessibility
- **Screen Reader Support**: Semantic HTML and ARIA labels
- **High Contrast**: Readable color combinations
- **Keyboard Navigation**: Full keyboard accessibility
- **Large Font Options**: Adjustable text sizes

## 📊 Data Sources

### Metro Network Data
- **Bengaluru**: BMRCL official network data
- **Delhi**: DMRC official network data
- **Station Information**: Amenities, accessibility, and operating hours
- **Line Information**: Colors, lengths, and station counts

### Real-Time Features
- **Operating Hours**: Current schedule information
- **Fare Estimates**: Based on official fare structures
- **Travel Time**: Calculated using average speeds and interchange times

## 🔧 Configuration

The application supports extensive configuration through `config.py`:

- **Themes**: Multiple color schemes and styling options
- **Features**: Enable/disable specific functionality
- **Performance**: Caching and optimization settings
- **Analytics**: Usage tracking and search history
- **Security**: Rate limiting and input validation

## 🚀 Performance Optimizations

### Caching
- Route calculation caching
- Station information caching
- Network data caching

### Algorithm Efficiency
- Optimized BFS implementation
- Graph traversal optimization
- Memory-efficient data structures

### UI Performance
- Lazy loading of components
- Optimized CSS and animations
- Efficient state management

## 📈 Future Enhancements

### Planned Features
- **Real-Time Updates**: Live train positions and delays
- **Multi-Modal Integration**: Bus, auto, and taxi connections
- **Crowd Density**: Real-time passenger information
- **Weather Integration**: Weather-based route suggestions
- **Voice Commands**: Hands-free navigation
- **Offline Mode**: Work without internet connection

### Technical Improvements
- **Machine Learning**: Predictive route optimization
- **Progressive Web App**: Native app-like experience
- **API Integration**: Real-time metro APIs
- **Multi-Language Support**: Regional language support

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
