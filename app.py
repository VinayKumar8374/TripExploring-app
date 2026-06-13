from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change-this-in-production')
app.config['JSON_SORT_KEYS'] = False

# Helper function to generate SVG images for each destination
def generate_svg_image(name, category):
    colors = {
        "Historical": ("#8B4513", "#D2691E", "🏛️"),
        "Nature": ("#228B22", "#32CD32", "🌿"),
        "Beach": ("#1E90FF", "#00BFFF", "🏖️"),
        "Spiritual": ("#8E44AD", "#9B59B6", "🕉️"),
        "Adventure": ("#E67E22", "#F39C12", "🧗")
    }
    color1, color2, icon = colors.get(category, ("#3498DB", "#2980B9", "📍"))
    
    # Create SVG image
    svg = f'''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
            </linearGradient>
            <filter id="shadow">
                <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.3"/>
            </filter>
        </defs>
        <rect width="800" height="600" fill="url(#grad)"/>
        <circle cx="400" cy="280" r="120" fill="rgba(255,255,255,0.15)" filter="url(#shadow)"/>
        <text x="400" y="280" font-family="Arial" font-size="120" text-anchor="middle" fill="white" filter="url(#shadow)">{icon}</text>
        <text x="400" y="400" font-family="Arial" font-size="32" font-weight="bold" text-anchor="middle" fill="white" filter="url(#shadow)">{name}</text>
        <text x="400" y="450" font-family="Arial" font-size="24" text-anchor="middle" fill="rgba(255,255,255,0.9)">{category}</text>
        <rect x="300" y="500" width="200" height="40" rx="20" fill="rgba(255,255,255,0.2)"/>
        <text x="400" y="527" font-family="Arial" font-size="18" text-anchor="middle" fill="white">✨ Must Visit ✨</text>
    </svg>'''
    return f"data:image/svg+xml;base64,{svg.encode('utf-8').decode('utf-8')}"

trips = [
    {
        "id": 1,
        "name": "Taj Mahal, Agra",
        "state": "Uttar Pradesh",
        "category": "Historical",
        "description": "The Taj Mahal, a UNESCO World Heritage Site, is an ivory-white marble mausoleum on the right bank of the Yamuna River. Built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal, it's the jewel of Muslim art in India and one of the universally admired masterpieces of the world's heritage.",
        "best_time": "October to March",
        "must_see": "Main mausoleum, reflecting pools, mosque, Mehtab Bagh",
        "entry_fee": "₹50 (Indians), ₹1100 (Foreigners)",
        "time_needed": "3-4 hours",
        "icon": "🏛️"
    },
    {
        "id": 2,
        "name": "Amer Fort, Jaipur",
        "state": "Rajasthan",
        "category": "Historical",
        "description": "Amer Fort, perched on a hilltop, is a magnificent blend of Hindu and Mughal architecture. Known for its artistic style, the fort features large ramparts, series of gates, cobbled paths, and the famous Sheesh Mahal (Mirror Palace) that sparkles with thousands of mirror fragments.",
        "best_time": "November to February",
        "must_see": "Sheesh Mahal, Sukh Niwas, Ganesh Pol, Light & Sound Show",
        "entry_fee": "₹100 (Indians), ₹500 (Foreigners)",
        "time_needed": "2-3 hours",
        "icon": "🏯"
    },
    {
        "id": 3,
        "name": "Alleppey Backwaters",
        "state": "Kerala",
        "category": "Nature",
        "description": "Alleppey, also known as Alappuzha, is famous for its serene backwaters, houseboats, and lush green paddy fields. A houseboat cruise through the network of lagoons, lakes, and canals offers a tranquil escape into God's Own Country, passing through villages and witnessing local life.",
        "best_time": "September to March",
        "must_see": "Houseboat cruise, Kumarakom Bird Sanctuary, Marari Beach, Nehru Trophy Boat Race",
        "entry_fee": "Houseboat: ₹5000-15000/night",
        "time_needed": "1-2 days",
        "icon": "🚣"
    },
    {
        "id": 4,
        "name": "Palolem Beach, Goa",
        "state": "Goa",
        "category": "Beach",
        "description": "Palolem Beach is one of Goa's most beautiful and serene beaches, known for its crescent-shaped shoreline, calm waters, and stunning sunset views. Unlike the crowded northern beaches, Palolem offers a perfect blend of natural beauty and relaxed vibes with shoulder-season dolphins.",
        "best_time": "November to February",
        "must_see": "Dolphin spotting, Butterfly Island, Silent Noise Party, Canacona markets",
        "entry_fee": "Free",
        "time_needed": "1-2 days",
        "icon": "🏖️"
    },
    {
        "id": 5,
        "name": "Varanasi Ghats",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "description": "Varanasi, the spiritual capital of India, sits on the banks of the Ganges. The city's ghats are a mesmerizing spectacle of life, death, and devotion. Witness the Ganga Aarti at sunset for an unforgettable spiritual experience that has been performed for thousands of years.",
        "best_time": "October to March",
        "must_see": "Dashashwamedh Ghat, Kashi Vishwanath Temple, Sarnath, Manikarnika Ghat, Boat ride at sunrise",
        "entry_fee": "Free (Boat ride: ₹300-500)",
        "time_needed": "2-3 days",
        "icon": "🕉️"
    },
    {
        "id": 6,
        "name": "Pangong Lake, Ladakh",
        "state": "Ladakh",
        "category": "Nature",
        "description": "Pangong Lake is a stunning high-altitude lake at 4,350m, stretching from India to China. Famous for its ever-changing shades of blue and dramatic mountain backdrop, this brackish water lake freezes completely in winter and offers breathtaking views during summer months.",
        "best_time": "June to September",
        "must_see": "Pangong Lake, Nubra Valley, Khardung La Pass, Magnetic Hill, Thiksey Monastery",
        "entry_fee": "₹500 (Inner Line Permit)",
        "time_needed": "1-2 days",
        "icon": "🏔️"
    },
    {
        "id": 7,
        "name": "Mysore Palace",
        "state": "Karnataka",
        "category": "Historical",
        "description": "Mysore Palace, also known as Amba Vilas Palace, is a stunning example of Indo-Saracenic architecture. It's the former seat of the Wodeyar dynasty and is magnificently illuminated with nearly 100,000 bulbs during Sundays and festivals, drawing millions of visitors annually.",
        "best_time": "October to March",
        "must_see": "Palace interior, Dasara procession, Chamundi Hills, Brindavan Gardens, Mysore Zoo",
        "entry_fee": "₹70 (Indians), ₹200 (Foreigners)",
        "time_needed": "2-3 hours",
        "icon": "👑"
    },
    {
        "id": 8,
        "name": "Darjeeling Himalayan Railway",
        "state": "West Bengal",
        "category": "Adventure",
        "description": "The Darjeeling Himalayan Railway, a UNESCO World Heritage Site, is a narrow-gauge toy train that winds through stunning mountain scenery, tea gardens, and loops. The journey from New Jalpaiguri to Darjeeling is an unforgettable ride through 88km of Himalayan foothills.",
        "best_time": "April to June, September to November",
        "must_see": "Toy train ride, Tiger Hill sunrise, Batasia Loop, Tea estates, Ghum Monastery",
        "entry_fee": "₹1500-3000 for joy ride",
        "time_needed": "1 day",
        "icon": "🚂"
    },
    {
        "id": 9,
        "name": "Hampi Ruins",
        "state": "Karnataka",
        "category": "Historical",
        "description": "Hampi is a UNESCO World Heritage Site that once served as the capital of the Vijayanagara Empire. The surreal landscape dotted with boulders, temples, and royal ruins makes it a history lover's paradise, spanning over 25 square kilometers of ancient wonders.",
        "best_time": "October to March",
        "must_see": "Virupaksha Temple, Vittala Temple with stone chariot, Lotus Mahal, Elephant Stables, Matanga Hill sunset",
        "entry_fee": "₹40 (Indians), ₹600 (Foreigners)",
        "time_needed": "2-3 days",
        "icon": "🗿"
    },
    {
        "id": 10,
        "name": "Golden Temple, Amritsar",
        "state": "Punjab",
        "category": "Spiritual",
        "description": "The Golden Temple (Harmandir Sahib) is the holiest shrine in Sikhism. Its shimmering gold sanctum surrounded by the holy Amrit Sarovar lake exudes peace and spirituality. The community kitchen (langar) serves free meals to over 100,000 devotees daily, regardless of faith.",
        "best_time": "October to March",
        "must_see": "Golden Temple sanctum, Jallianwala Bagh, Wagah Border ceremony, Partition Museum, Langar meal",
        "entry_fee": "Free",
        "time_needed": "3-4 hours",
        "icon": "✨"
    },
    {
        "id": 11,
        "name": "Khajuraho Temples",
        "state": "Madhya Pradesh",
        "category": "Historical",
        "description": "The Khajuraho Group of Monuments is a UNESCO World Heritage Site famous for its stunning Nagara-style architecture and intricate erotic sculptures. Built by the Chandela dynasty between 950-1050 CE, these 25 surviving temples showcase medieval Indian art and spirituality.",
        "best_time": "July to March",
        "must_see": "Kandariya Mahadev Temple, Lakshmana Temple, Light & Sound Show, Archeological Museum",
        "entry_fee": "₹40 (Indians), ₹600 (Foreigners)",
        "time_needed": "4-5 hours",
        "icon": "🛕"
    },
    {
        "id": 12,
        "name": "Valley of Flowers",
        "state": "Uttarakhand",
        "category": "Nature",
        "description": "The Valley of Flowers is a UNESCO World Heritage Site known for its meadows of endemic alpine flowers and diverse flora. This high-altitude Himalayan valley comes alive during monsoon months with over 500 species of wildflowers, including the rare blue poppy and cobra lily.",
        "best_time": "July to September",
        "must_see": "Valley trek, Hemkund Sahib, Pushpawati River, Bhyundar Village, diverse alpine flowers",
        "entry_fee": "₹150 (Indians), ₹300 (Foreigners)",
        "time_needed": "1-2 days",
        "icon": "🌸"
    },
    {
        "id": 13,
        "name": "Munnar Tea Gardens",
        "state": "Kerala",
        "category": "Nature",
        "description": "Munnar is a picturesque hill station famous for its vast tea plantations, rolling hills, and cool climate. The endless stretches of emerald tea gardens, misty mountains, and spice plantations make it one of South India's most beautiful destinations, sitting at 1,600m altitude.",
        "best_time": "September to May",
        "must_see": "Tea Museum, Mattupetty Dam, Eravikulam National Park, Echo Point, Kundala Lake",
        "entry_fee": "Tea Museum: ₹100",
        "time_needed": "2-3 days",
        "icon": "🍃"
    },
    {
        "id": 14,
        "name": "Mahabalipuram Shore Temple",
        "state": "Tamil Nadu",
        "category": "Historical",
        "description": "The Shore Temple at Mahabalipuram is a UNESCO World Heritage Site that stands majestically overlooking the Bay of Bengal. Built in the 8th century during the Pallava dynasty, this structural temple is one of the oldest stone temples in South India and survived the 2004 tsunami.",
        "best_time": "November to February",
        "must_see": "Shore Temple, Pancha Rathas, Arjuna's Penance, Krishna's Butter Ball, Lighthouse",
        "entry_fee": "₹40 (Indians), ₹600 (Foreigners)",
        "time_needed": "3-4 hours",
        "icon": "🌊"
    },
    {
        "id": 15,
        "name": "Andaman Islands",
        "state": "Andaman & Nicobar",
        "category": "Beach",
        "description": "The Andaman Islands are a tropical paradise known for pristine white-sand beaches, crystal-clear turquoise waters, and vibrant coral reefs. This archipelago of 572 islands offers world-class snorkeling, scuba diving, and the famous Cellular Jail historical site.",
        "best_time": "October to May",
        "must_see": "Radhanagar Beach, Cellular Jail, Havelock Island, Neil Island, Ross Island, Scuba diving",
        "entry_fee": "₹50 entry (some islands)",
        "time_needed": "5-7 days",
        "icon": "🐠"
    }
]

@app.route('/')
def index():
    return render_template('index.html', trips=trips)

@app.route('/health')
def health():
    return {"status": "healthy", "destinations": len(trips), "server": socket.gethostname()}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
