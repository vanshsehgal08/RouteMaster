"""
Station Information Database
Contains detailed information about metro stations including amenities, timings, and accessibility features.
"""

# Station amenities and information
STATION_AMENITIES = {
    # Bengaluru Metro Stations
    'NADAPRABHU KEMPEGOWDA STATION, MAJESTIC': {
        'amenities': ['Parking', 'Food Court', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator'],
        'lines': ['Purple Line', 'Green Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:00',
        'interchange': True,
        'description': 'Major interchange station connecting Purple and Green lines'
    },
    'INDIRANAGAR': {
        'amenities': ['Parking', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator', 'Shopping'],
        'lines': ['Purple Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:00',
        'interchange': False,
        'description': 'Popular commercial area with shopping and dining options'
    },
    'BAIYYAPANAHALLI': {
        'amenities': ['Parking', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator'],
        'lines': ['Purple Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:00',
        'interchange': False,
        'description': 'Terminal station of Purple Line'
    },
    'YELACHENAHALLI': {
        'amenities': ['Parking', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator'],
        'lines': ['Green Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:00',
        'interchange': False,
        'description': 'Terminal station of Green Line'
    },
    'SILK INSTITUTE': {
        'amenities': ['Parking', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator'],
        'lines': ['Green Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:00',
        'interchange': False,
        'description': 'Terminal station of Green Line extension'
    },
    
    # Delhi Metro Stations
    'RAJIV CHOWK': {
        'amenities': ['Parking', 'Food Court', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator', 'Shopping', 'Medical'],
        'lines': ['Yellow Line', 'Blue Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:30',
        'interchange': True,
        'description': 'Major interchange station in central Delhi, connects to Connaught Place'
    },
    'KASHMERE GATE': {
        'amenities': ['Parking', 'Food Court', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator', 'Shopping'],
        'lines': ['Red Line', 'Yellow Line', 'Violet Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:30',
        'interchange': True,
        'description': 'Major interchange station connecting multiple lines'
    },
    'NEW DELHI': {
        'amenities': ['Parking', 'Food Court', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator', 'Shopping', 'Medical'],
        'lines': ['Orange Line', 'Airport Express'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:30',
        'interchange': True,
        'description': 'Connects to New Delhi Railway Station and Airport Express'
    },
    'AIRPORT (T-3)': {
        'amenities': ['Parking', 'Food Court', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator', 'Luggage Trolley'],
        'lines': ['Orange Line'],
        'accessibility': True,
        'first_train': '04:45',
        'last_train': '23:30',
        'interchange': False,
        'description': 'Terminal 3 of Indira Gandhi International Airport'
    },
    'HUDA CITY CENTRE': {
        'amenities': ['Parking', 'Food Court', 'ATM', 'WiFi', 'Toilet', 'Lift', 'Escalator', 'Shopping'],
        'lines': ['Yellow Line'],
        'accessibility': True,
        'first_train': '05:30',
        'last_train': '23:30',
        'interchange': False,
        'description': 'Terminal station connecting to Gurgaon'
    }
}

# Metro line colors
LINE_COLORS = {
    'Purple Line': '#7B2CBF',
    'Green Line': '#00A651',
    'Red Line': '#FF0000',
    'Yellow Line': '#FFFF00',
    'Blue Line': '#0066CC',
    'Violet Line': '#8B00FF',
    'Orange Line': '#FF6600',
    'Airport Express': '#00BFFF',
    'Green Line (Branch)': '#32CD32',
    'Pink Line': '#FF69B4',
    'Magenta Line': '#8B008B'
}

# Metro line information
METRO_LINES = {
    'Bengaluru': {
        'Purple Line': {
            'stations': ['NAGASANDRA', 'DASARAHALLI', 'JALAHALLI', 'PEENYA INDUSTRY', 'PEENYA', 
                        'GORAGUNTEPALYA', 'YESHWANTHPUR', 'SANDAL SOAP FACTORY', 'MAHALAKSHMI', 
                        'RAJAJINAGAR', 'MAHAKAVI KUVEMPU ROAD', 'SRIRAMPURA', 'MANTRI SQUARE SAMPIGE ROAD', 
                        'NADAPRABHU KEMPEGOWDA STATION, MAJESTIC', 'SRI M VISVESWARAYA STATION, CENTRAL COLLEGE', 
                        'DR.B.R.AMBEDKAR STATION, VIDHANA SOUDHA', 'CUBBON PARK', 'MAHATMA GANDHI ROAD', 
                        'TRINITY', 'HALASURU', 'INDIRANAGAR', 'SWAMI VIVEKANANDA ROAD', 'BAIYYAPANAHALLI'],
            'color': '#7B2CBF',
            'length': '18.2 km',
            'stations_count': 23
        },
        'Green Line': {
            'stations': ['NADAPRABHU KEMPEGOWDA STATION, MAJESTIC', 'CHICKPETE', 'KRISHNA RAJENDRA MARKET', 
                        'NATION COLLEGE', 'LALBAGH', 'SOUTH END CIRCLE', 'JAYANAGAR', 'RASHTREEYA VIDYALAYA ROAD', 
                        'BANASHANKARI', 'JAYA PRAKASH NAGAR', 'YELACHENAHALLI', 'KONANAKUNTE CROSS', 
                        'DODDAKALLASANDRA', 'VAJRAHALLI', 'THALAGHATTAPURA', 'SILK INSTITUTE'],
            'color': '#00A651',
            'length': '13.8 km',
            'stations_count': 16
        },
        'Green Line Extension': {
            'stations': ['KENGERI', 'KENGERI BUS TERMINAL', 'PATTANAGERE', 'JNANABHARATHI', 
                        'RAJARAJESHWARI NAGAR', 'NAYANDAHALLI', 'MYSORE ROAD', 'DEEPANJALI NAGAR', 
                        'ATTIGUPPE', 'VIJAYANAGAR', 'SRI BALAGANGADHARANATHA SWAMIJI STATION, HOSAHALLI', 
                        'MAGADI ROAD', 'KRANTIVIRA SANGOLLI RAYANNA RAILWAY STATION'],
            'color': '#32CD32',
            'length': '12.8 km',
            'stations_count': 13
        }
    },
    'Delhi': {
        'Red Line': {
            'stations': ['SHAHEED STHAL', 'HINDON RIVER', 'ARTHALA', 'MOHAN NAGAR', 'SHYAM PARK', 
                        'MAJOR MOHIT SHARMA RAJENDRA NAGAR', 'RAJBAGH', 'SHAHEED NAGAR', 'DILSHAD GARDEN', 
                        'JHILMIL', 'MANSAROVAR PARK', 'SHAHDARA', 'WELCOME', 'SEELAMPUR', 'SHASTRI PARK', 
                        'KASHMERE GATE', 'TIS HAZARI', 'PULBANGASH', 'PRATAP NAGAR', 'SHASTRI NAGAR', 
                        'INDERLOK', 'KANHAIYA NAGAR', 'KESHAV PURAM', 'NETAJI SUBHASH PLACE', 'SHAKUR PUR', 
                        'PUNJABI BAGH (W)', 'ESI HOSPITAL', 'RAJOURI GARDEN', 'MAYAPURI', 'NARAINA VIHAR', 
                        'DELHI CANTT.', 'DURGABAI DESHMUKH SOUTH CAMPUS', 'SIR M. VISHWESHARAIYAH MOTI BAGH', 
                        'BHIKAJI CAMA PLACE', 'SAROJINI NAGAR', 'DILLI HAAT - INA', 'JOR BAGH', 'LOK KALYAN MARG', 
                        'UDYOG BHAWAN', 'CENTRAL SECRETARIAT', 'PATEL CHOWK', 'RAJIV CHOWK', 'NEW DELHI', 
                        'CHAWRI BAZAR', 'CHANDNI CHOWK', 'KASHMERE GATE'],
            'color': '#FF0000',
            'length': '34.5 km',
            'stations_count': 29
        },
        'Yellow Line': {
            'stations': ['HUDA CITY CENTRE', 'IFFCO CHOWK', 'MG ROAD', 'SIKANDERPUR', 'GURU DRONACHARYA', 
                        'ARJANGARH', 'GHITORNI', 'SULTANPUR', 'CHHATTARPUR', 'QUTAB MINAR', 'SAKET', 
                        'MALVIYA NAGAR', 'HAUZ KHAS', 'GREEN PARK', 'AIIMS', 'DILLI HAAT - INA', 'JOR BAGH', 
                        'LOK KALYAN MARG', 'UDYOG BHAWAN', 'CENTRAL SECRETARIAT', 'PATEL CHOWK', 'RAJIV CHOWK', 
                        'NEW DELHI', 'CHAWRI BAZAR', 'CHANDNI CHOWK', 'KASHMERE GATE', 'SHASTRI PARK', 'SEELAMPUR', 
                        'WELCOME', 'JAFRABAD', 'MAUJPUR-BABARPUR', 'GOKULPURI', 'JOHRI ENCLAVE', 'SHIV VIHAR'],
            'color': '#FFFF00',
            'length': '49.0 km',
            'stations_count': 37
        },
        'Blue Line': {
            'stations': ['DWARKA SECTOR-21', 'DWARKA SECTOR-8', 'DWARKA SECTOR-9', 'DWARKA SECTOR-10', 
                        'DWARKA SECTOR-11', 'DWARKA SECTOR-12', 'DWARKA SECTOR-13', 'DWARKA SECTOR-14', 
                        'DWARKA', 'DWARKA MOR', 'NAWADA', 'UTTAM NAGAR (WEST)', 'UTTAM NAGAR (EAST)', 
                        'JANAKPURI (WEST)', 'JANAKPURI (EAST)', 'TILAK NAGAR', 'SUBHASH NAGAR', 'TAGORE GARDEN', 
                        'RAJOURI GARDEN', 'RAMESH NAGAR', 'MOTI NAGAR', 'KIRTI NAGAR', 'SATGURU RAM SINGH MARG', 
                        'ASHOK PARK MAIN', 'INDERLOK', 'SHIVAJI PARK', 'PUNJABI BAGH', 'MADIPUR', 'PASCHIM VIHAR (EAST)', 
                        'PASCHIM VIHAR (WEST)', 'PEERAGARHI', 'UDYOG NAGAR', 'MAHARAJA SURAJMAL STADIUM', 'NANGLOI', 
                        'NANGLOI RAILWAY STATION', 'RAJDHANI PARK', 'MUNDKA', 'MUNDKA INDUSTRIAL AREA', 'GHEVRA', 
                        'TIKRI KALAN', 'TIKRI BORDER', 'PANDIT SHREE RAM SHARMA', 'BAHADURGARH CITY', 'BRIG. HOSHIAR SINGH'],
            'color': '#0066CC',
            'length': '56.6 km',
            'stations_count': 50
        }
    }
}

def get_station_info(station_name):
    """Get detailed information about a station"""
    return STATION_AMENITIES.get(station_name, {
        'amenities': ['ATM', 'WiFi', 'Toilet'],
        'lines': ['Unknown Line'],
        'accessibility': False,
        'first_train': '05:30',
        'last_train': '23:00',
        'interchange': False,
        'description': 'Standard metro station'
    })

def get_line_info(city, line_name):
    """Get information about a metro line"""
    return METRO_LINES.get(city, {}).get(line_name, {
        'stations': [],
        'color': '#666666',
        'length': 'Unknown',
        'stations_count': 0
    })

def get_all_lines_for_city(city):
    """Get all lines for a specific city"""
    return METRO_LINES.get(city, {})

def is_interchange_station(station_name):
    """Check if a station is an interchange station"""
    station_info = get_station_info(station_name)
    return station_info.get('interchange', False)

def get_station_amenities(station_name):
    """Get amenities available at a station"""
    station_info = get_station_info(station_name)
    return station_info.get('amenities', [])

def get_operating_hours(station_name):
    """Get operating hours for a station"""
    station_info = get_station_info(station_name)
    return {
        'first_train': station_info.get('first_train', '05:30'),
        'last_train': station_info.get('last_train', '23:00')
    }
