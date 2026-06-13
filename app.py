from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change-this-in-production')
app.config['JSON_SORT_KEYS'] = False

trips = [
    {
        "id": 1,
        "name": "Taj Mahal, Agra",
        "state": "Uttar Pradesh",
        "category": "Historical",
        "description": "The Taj Mahal, a UNESCO World Heritage Site, is an ivory-white marble mausoleum on the right bank of the Yamuna River. Built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal, it's the jewel of Muslim art in India and one of the universally admired masterpieces of the world's heritage.",
        "best_time": "October to March",
        "must_see": "Main mausoleum, reflecting pools, mosque, Mehtab Bagh",
        "image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&h=600&fit=crop",
        "entry_fee": "₹50 (Indians), ₹1100 (Foreigners)",
        "time_needed": "3-4 hours"
    },
    {
        "id": 2,
        "name": "Amer Fort, Jaipur",
        "state": "Rajasthan",
        "category": "Historical",
        "description": "Amer Fort, perched on a hilltop, is a magnificent blend of Hindu and Mughal architecture. Known for its artistic style, the fort features large ramparts, series of gates, cobbled paths, and the famous Sheesh Mahal (Mirror Palace).",
        "best_time": "November to February",
        "must_see": "Sheesh Mahal, Sukh Niwas, Ganesh Pol, Light & Sound Show",
        "image_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop",
        "entry_fee": "₹100 (Indians), ₹500 (Foreigners)",
        "time_needed": "2-3 hours"
    },
    {
        "id": 3,
        "name": "Alleppey Backwaters",
        "state": "Kerala",
        "category": "Nature",
        "description": "Alleppey, also known as Alappuzha, is famous for its serene backwaters, houseboats, and lush green paddy fields. A houseboat cruise through the network of lagoons, lakes, and canals offers a tranquil escape into God's Own Country.",
        "best_time": "September to March",
        "must_see": "Houseboat cruise, Kumarakom Bird Sanctuary, Marari Beach",
        "image_url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=800&h=600&fit=crop",
        "entry_fee": "Houseboat: ₹5000-15000/night",
        "time_needed": "1-2 days"
    },
    {
        "id": 4,
        "name": "Palolem Beach, Goa",
        "state": "Goa",
        "category": "Beach",
        "description": "Palolem Beach is one of Goa's most beautiful and serene beaches, known for its crescent-shaped shoreline, calm waters, and stunning sunset views. Perfect blend of natural beauty and relaxed vibes.",
        "best_time": "November to February",
        "must_see": "Dolphin spotting, Butterfly Island, Silent Noise Party",
        "image_url": "https://images.unsplash.com/photo-1519046904884-53103b34b206?w=800&h=600&fit=crop",
        "entry_fee": "Free",
        "time_needed": "1-2 days"
    },
    {
        "id": 5,
        "name": "Varanasi Ghats",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "description": "Varanasi, the spiritual capital of India, sits on the banks of the Ganges. The city's ghats are a mesmerizing spectacle of life, death, and devotion. Witness the Ganga Aarti at sunset for an unforgettable spiritual experience.",
        "best_time": "October to March",
        "must_see": "Dashashwamedh Ghat, Kashi Vishwanath Temple, Sarnath",
        "image_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop",
        "entry_fee": "Free (Boat ride: ₹300-500)",
        "time_needed": "2-3 days"
    },
    {
        "id": 6,
        "name": "Pangong Lake, Ladakh",
        "state": "Ladakh",
        "category": "Nature",
        "description": "Pangong Lake is a stunning high-altitude lake at 4,350m, stretching from India to China. Famous for its ever-changing shades of blue and dramatic mountain backdrop.",
        "best_time": "June to September",
        "must_see": "Pangong Lake, Nubra Valley, Khardung La Pass",
        "image_url": "https://images.unsplash.com/photo-1588106135363-efc70848ecf5?w=800&h=600&fit=crop",
        "entry_fee": "₹500 (Inner Line Permit)",
        "time_needed": "1-2 days"
    },
    {
        "id": 7,
        "name": "Mysore Palace",
        "state": "Karnataka",
        "category": "Historical",
        "description": "Mysore Palace, also known as Amba Vilas Palace, is a stunning example of Indo-Saracenic architecture. It's illuminated with nearly 100,000 bulbs during Sundays and festivals.",
        "best_time": "October to March",
        "must_see": "Palace interior, Dasara procession, Chamundi Hills",
        "image_url": "https://images.unsplash.com/photo-1599661046827-dacff0c0f09c?w=800&h=600&fit=crop",
        "entry_fee": "₹70 (Indians), ₹200 (Foreigners)",
        "time_needed": "2-3 hours"
    },
    {
        "id": 8,
        "name": "Darjeeling Himalayan Railway",
        "state": "West Bengal",
        "category": "Adventure",
        "description": "The Darjeeling Himalayan Railway, a UNESCO World Heritage Site, is a narrow-gauge toy train that winds through stunning mountain scenery, tea gardens, and loops.",
        "best_time": "April to June, September to November",
        "must_see": "Toy train ride, Tiger Hill sunrise, Batasia Loop",
        "image_url": "https://images.unsplash.com/photo-1588106135363-efc70848ecf5?w=800&h=600&fit=crop",
        "entry_fee": "₹1500-3000 for joy ride",
        "time_needed": "1 day"
    },
    {
        "id": 9,
        "name": "Hampi Ruins",
        "state": "Karnataka",
        "category": "Historical",
        "description": "Hampi is a UNESCO World Heritage Site that once served as the capital of the Vijayanagara Empire. The surreal landscape dotted with boulders and ancient ruins.",
        "best_time": "October to March",
        "must_see": "Virupaksha Temple, Vittala Temple, Lotus Mahal",
        "image_url": "https://images.unsplash.com/photo-1600359122753-5a9d0027e4c4?w=800&h=600&fit=crop",
        "entry_fee": "₹40 (Indians), ₹600 (Foreigners)",
        "time_needed": "2-3 days"
    },
    {
        "id": 10,
        "name": "Golden Temple, Amritsar",
        "state": "Punjab",
        "category": "Spiritual",
        "description": "The Golden Temple (Harmandir Sahib) is the holiest shrine in Sikhism. Its shimmering gold sanctum surrounded by the holy Amrit Sarovar lake exudes peace.",
        "best_time": "October to March",
        "must_see": "Golden Temple sanctum, Jallianwala Bagh, Wagah Border",
        "image_url": "https://images.unsplash.com/photo-1568271679568-1afaab8b5c1c?w=800&h=600&fit=crop",
        "entry_fee": "Free",
        "time_needed": "3-4 hours"
    },
    {
        "id": 11,
        "name": "Khajuraho Temples",
        "state": "Madhya Pradesh",
        "category": "Historical",
        "description": "The Khajuraho Group of Monuments is a UNESCO World Heritage Site famous for its stunning Nagara-style architecture and intricate sculptures.",
        "best_time": "July to March",
        "must_see": "Kandariya Mahadev Temple, Lakshmana Temple",
        "image_url": "https://images.unsplash.com/photo-1566838610721-5bfefca6f4d1?w=800&h=600&fit=crop",
        "entry_fee": "₹40 (Indians), ₹600 (Foreigners)",
        "time_needed": "4-5 hours"
    },
    {
        "id": 12,
        "name": "Valley of Flowers",
        "state": "Uttarakhand",
        "category": "Nature",
        "description": "The Valley of Flowers is a UNESCO World Heritage Site known for its meadows of endemic alpine flowers and diverse flora with over 500 species.",
        "best_time": "July to September",
        "must_see": "Valley trek, Hemkund Sahib, Pushpawati River",
        "image_url": "https://images.unsplash.com/photo-1588106135363-efc70848ecf5?w=800&h=600&fit=crop",
        "entry_fee": "₹150 (Indians), ₹300 (Foreigners)",
        "time_needed": "1-2 days"
    },
    {
        "id": 13,
        "name": "Munnar Tea Gardens",
        "state": "Kerala",
        "category": "Nature",
        "description": "Munnar is a picturesque hill station famous for its vast tea plantations, rolling hills, and cool climate with endless stretches of emerald tea gardens.",
        "best_time": "September to May",
        "must_see": "Tea Museum, Mattupetty Dam, Eravikulam National Park",
        "image_url": "https://images.unsplash.com/photo-1588106135363-efc70848ecf5?w=800&h=600&fit=crop",
        "entry_fee": "Tea Museum: ₹100",
        "time_needed": "2-3 days"
    },
    {
        "id": 14,
        "name": "Mahabalipuram Shore Temple",
        "state": "Tamil Nadu",
        "category": "Historical",
        "description": "The Shore Temple at Mahabalipuram is a UNESCO World Heritage Site overlooking the Bay of Bengal, built in the 8th century during the Pallava dynasty.",
        "best_time": "November to February",
        "must_see": "Shore Temple, Pancha Rathas, Arjuna's Penance",
        "image_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop",
        "entry_fee": "₹40 (Indians), ₹600 (Foreigners)",
        "time_needed": "3-4 hours"
    },
    {
        "id": 15,
        "name": "Andaman Islands",
        "state": "Andaman & Nicobar",
        "category": "Beach",
        "description": "The Andaman Islands are a tropical paradise known for pristine white-sand beaches, crystal-clear turquoise waters, and vibrant coral reefs.",
        "best_time": "October to May",
        "must_see": "Radhanagar Beach, Cellular Jail, Havelock Island",
        "image_url": "https://images.unsplash.com/photo-1519046904884-53103b34b206?w=800&h=600&fit=crop",
        "entry_fee": "₹50 entry (some islands)",
        "time_needed": "5-7 days"
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
