from flask import Flask, render_template

app = Flask(__name__)

# Trip data: destination name, state, description, image URL (realistic high-quality images)
trips = [
    {
        "name": "Taj Mahal, Agra",
        "state": "Uttar Pradesh",
        "description": "The Taj Mahal, a UNESCO World Heritage Site, is an ivory-white marble mausoleum on the right bank of the Yamuna River. Built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal, it's the jewel of Muslim art in India and one of the universally admired masterpieces of the world's heritage.",
        "best_time": "October to March",
        "must_see": "Main mausoleum, reflecting pools, mosque, Mehtab Bagh",
        "image_url": "https://images.pexels.com/photos/1603650/taj-mahal-agra-india-1603650.jpg"
    },
    {
        "name": "Jaipur - Pink City",
        "state": "Rajasthan",
        "description": "Jaipur, the capital of Rajasthan, is known as the Pink City for its terracotta buildings. It's a vibrant blend of royal heritage, bustling bazaars, and magnificent forts. From the astronomical wonders of Jantar Mantar to the grandeur of City Palace, Jaipur offers an immersive royal experience.",
        "best_time": "November to February",
        "must_see": "Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, Jal Mahal",
        "image_url": "https://images.pexels.com/photos/2033997/pexels-photo-2033997.jpeg"
    },
    {
        "name": "Backwaters of Alleppey",
        "state": "Kerala",
        "description": "Alleppey, also known as Alappuzha, is famous for its serene backwaters, houseboats, and lush green paddy fields. A houseboat cruise through the network of lagoons, lakes, and canals offers a tranquil escape into God's Own Country.",
        "best_time": "September to March",
        "must_see": "Houseboat cruise, Kumarakom Bird Sanctuary, Marari Beach, Nehru Trophy Boat Race",
        "image_url": "https://images.pexels.com/photos/258117/pexels-photo-258117.jpeg"
    },
    {
        "name": "Goa Beaches",
        "state": "Goa",
        "description": "Goa is India's ultimate beach destination, known for its golden sands, vibrant nightlife, Portuguese-era churches, and laid-back atmosphere. From bustling Baga to serene Palolem, each beach has its unique charm.",
        "best_time": "November to February",
        "must_see": "Baga Beach, Basilica of Bom Jesus, Aguada Fort, Dudhsagar Falls, Anjuna Flea Market",
        "image_url": "https://images.pexels.com/photos/2317904/pexels-photo-2317904.jpeg"
    },
    {
        "name": "Varanasi Ghats",
        "state": "Uttar Pradesh",
        "description": "Varanasi, the spiritual capital of India, sits on the banks of the Ganges. The city's ghats are a mesmerizing spectacle of life, death, and devotion. Witness the Ganga Aarti at sunset for an unforgettable spiritual experience.",
        "best_time": "October to March",
        "must_see": "Dashashwamedh Ghat, Kashi Vishwanath Temple, Sarnath, Manikarnika Ghat, Boat ride at sunrise",
        "image_url": "https://images.pexels.com/photos/5558116/pexels-photo-5558116.jpeg"
    },
    {
        "name": "Leh-Ladakh",
        "state": "Ladakh",
        "description": "Leh-Ladakh is a high-altitude desert with dramatic landscapes, pristine lakes, and Buddhist monasteries. It's a paradise for adventure seekers and nature lovers, featuring some of the world's highest motorable roads.",
        "best_time": "June to September",
        "must_see": "Pangong Lake, Nubra Valley, Khardung La Pass, Magnetic Hill, Thiksey Monastery",
        "image_url": "https://images.pexels.com/photos/896876/pexels-photo-896876.jpeg"
    },
    {
        "name": "Mysore Palace",
        "state": "Karnataka",
        "description": "Mysore Palace, also known as Amba Vilas Palace, is a stunning example of Indo-Saracenic architecture. It's the former seat of the Wodeyar dynasty and is magnificently illuminated with nearly 100,000 bulbs during Sundays and festivals.",
        "best_time": "October to March",
        "must_see": "Palace interior, Dasara procession, Chamundi Hills, Brindavan Gardens, Mysore Zoo",
        "image_url": "https://images.pexels.com/photos/2583745/pexels-photo-2583745.jpeg"
    },
    {
        "name": "Darjeeling Himalayan Railway",
        "state": "West Bengal",
        "description": "The Darjeeling Himalayan Railway, a UNESCO World Heritage Site, is a narrow-gauge toy train that winds through stunning mountain scenery, tea gardens, and loops. The journey from New Jalpaiguri to Darjeeling is an unforgettable ride.",
        "best_time": "April to June, September to November",
        "must_see": "Toy train ride, Tiger Hill sunrise, Batasia Loop, Tea estates, Ghum Monastery",
        "image_url": "https://images.pexels.com/photos/6667322/pexels-photo-6667322.jpeg"
    },
    {
        "name": "Hampi Ruins",
        "state": "Karnataka",
        "description": "Hampi is a UNESCO World Heritage Site that once served as the capital of the Vijayanagara Empire. The surreal landscape dotted with boulders, temples, and royal ruins makes it a history lover's paradise.",
        "best_time": "October to March",
        "must_see": "Virupaksha Temple, Vittala Temple with stone chariot, Lotus Mahal, Elephant Stables, Matanga Hill sunset",
        "image_url": "https://images.pexels.com/photos/2088967/pexels-photo-2088967.jpeg"
    },
    {
        "name": "Amritsar - Golden Temple",
        "state": "Punjab",
        "description": "The Golden Temple (Harmandir Sahib) is the holiest shrine in Sikhism. Its shimmering gold sanctum surrounded by the holy Amrit Sarovar lake exudes peace and spirituality. The community kitchen (langar) serves free meals to thousands daily.",
        "best_time": "October to March",
        "must_see": "Golden Temple sanctum, Jallianwala Bagh, Wagah Border ceremony, Partition Museum, Langar meal",
        "image_url": "https://images.pexels.com/photos/13697486/pexels-photo-13697486.jpeg"
    }
]

@app.route('/')
def index():
    return render_template('index.html', trips=trips)

if __name__ == '__main__':
    app.run(debug=True)
