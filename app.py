from flask import Flask, render_template, jsonify

# Initialize the Flask Application
app = Flask(__name__)

# --- Destination Data ---
# In a real application, this might come from a database.
# Coordinates are [Latitude, Longitude]
# --- ADD THESE 51 NEW DESTINATIONS TO YOUR EXISTING LIST IN app.py ---

destinations_data = [
    # --- The North ---
    {
        "name": "Yellowknife, Northwest Territories",
        "description": "The Aurora Capital of North America, offering unparalleled views of the northern lights from stunning wilderness lodges.",
        "avg_hotel_price": 260,
        "coords": [62.4540, -114.3718]
    },
    {
        "name": "Dawson City, Yukon",
        "description": "A living Gold Rush town with historic saloons, dirt streets, and a vibrant arts scene in the heart of the Klondike.",
        "avg_hotel_price": 220,
        "coords": [64.0673, -139.4300]
    },
    {
        "name": "Iqaluit, Nunavut",
        "description": "The capital of Nunavut on Baffin Island, a hub for Inuit culture, art, and expeditions into the Arctic wilderness.",
        "avg_hotel_price": 380,
        "coords": [63.7467, -68.5170]
    },
    {
        "name": "Kluane National Park, Yukon",
        "description": "Home to Mount Logan, Canada's highest peak. A land of massive glaciers, grizzly bears, and epic mountain landscapes.",
        "avg_hotel_price": 230,
        "coords": [60.8548, -139.3888]
    },
    {
        "name": "Nahanni National Park, Northwest Territories",
        "description": "A UNESCO World Heritage site accessible only by air, featuring deep canyons, huge waterfalls, and legendary wild rivers.",
        "avg_hotel_price": 450,
        "coords": [61.5926, -125.5910]
    },
    {
        "name": "Pangnirtung, Nunavut",
        "description": "Known as 'Pang,' this hamlet is the gateway to Auyuittuq National Park, famous for its dramatic fjords and Mount Thor.",
        "avg_hotel_price": 420,
        "coords": [66.1465, -65.7125]
    },
    {
        "name": "Churchill, Manitoba",
        "description": "The 'Polar Bear Capital of the World,' offering unique opportunities to see bears, beluga whales, and the aurora borealis.",
        "avg_hotel_price": 390,
        "coords": [58.7685, -94.1693]
    },

    # --- British Columbia ---
    {
        "name": "Victoria, British Columbia",
        "description": "The charming capital of BC, known for its beautiful Inner Harbour, historic architecture, and the world-famous Butchart Gardens.",
        "avg_hotel_price": 240,
        "coords": [48.4284, -123.3656]
    },
    {
        "name": "Kelowna, British Columbia",
        "description": "The heart of the Okanagan Valley, a lakeside city surrounded by vineyards, orchards, and sunny beaches.",
        "avg_hotel_price": 260,
        "coords": [49.8880, -119.4960]
    },
    {
        "name": "Revelstoke, British Columbia",
        "description": "A paradise for powder hounds and mountain bikers, boasting North America's greatest vertical drop at its ski resort.",
        "avg_hotel_price": 290,
        "coords": [50.9981, -118.1957]
    },
    {
        "name": "Haida Gwaii, British Columbia",
        "description": "A remote and mystical archipelago known as the 'Galapagos of the North,' rich in Haida culture and ancient rainforests.",
        "avg_hotel_price": 270,
        "coords": [53.2533, -132.0722]
    },
    {
        "name": "Nelson, British Columbia",
        "description": "A vibrant arts and culture hub nestled in the Selkirk Mountains, with a beautifully preserved historic downtown.",
        "avg_hotel_price": 190,
        "coords": [49.4921, -117.2945]
    },

    # --- The Prairies ---
    {
        "name": "Jasper, Alberta",
        "description": "A ruggedly beautiful mountain town in the world's second-largest Dark Sky Preserve, offering incredible stargazing and wildlife.",
        "avg_hotel_price": 320,
        "coords": [52.8734, -117.9543]
    },
    {
        "name": "Calgary, Alberta",
        "description": "A bustling city where the prairies meet the mountains, famous for the Calgary Stampede and its proximity to the Rockies.",
        "avg_hotel_price": 180,
        "coords": [51.0447, -114.0719]
    },
    {
        "name": "Drumheller, Alberta",
        "description": "The dinosaur capital of the world, set in the surreal landscape of the Canadian Badlands with its unique hoodoo rock formations.",
        "avg_hotel_price": 160,
        "coords": [51.4638, -112.7118]
    },
    {
        "name": "Waterton Lakes National Park, Alberta",
        "description": "A serene park where the Rocky Mountains dramatically rise from the prairies, forming an international peace park with Montana.",
        "avg_hotel_price": 250,
        "coords": [49.0558, -113.9100]
    },
    {
        "name": "Saskatoon, Saskatchewan",
        "description": "The 'City of Bridges,' a vibrant hub on the South Saskatchewan River with a thriving food scene and beautiful river valley parks.",
        "avg_hotel_price": 150,
        "coords": [52.1332, -106.6700]
    },
    {
        "name": "Regina, Saskatchewan",
        "description": "Saskatchewan's capital, built around the beautiful Wascana Lake and home to the training academy of the RCMP.",
        "avg_hotel_price": 140,
        "coords": [50.4452, -104.6189]
    },
    {
        "name": "Winnipeg, Manitoba",
        "description": "A cultural oasis on the prairies, featuring The Forks historic site and the architecturally stunning Canadian Museum for Human Rights.",
        "avg_hotel_price": 160,
        "coords": [49.8951, -97.1384]
    },
    
    # --- Ontario ---
    {
        "name": "Ottawa, Ontario",
        "description": "Canada's capital city, home to Parliament Hill, national museums, and the Rideau Canal, which becomes the world's largest skating rink.",
        "avg_hotel_price": 200,
        "coords": [45.4215, -75.6972]
    },
    {
        "name": "Niagara Falls, Ontario",
        "description": "Site of the world-famous Horseshoe Falls, offering breathtaking views, boat tours, and a vibrant entertainment district.",
        "avg_hotel_price": 220,
        "coords": [43.0896, -79.0849]
    },
    {
        "name": "Algonquin Provincial Park, Ontario",
        "description": "A vast expanse of maple hills, rocky ridges, and pristine lakes, perfect for backcountry canoeing, hiking, and moose spotting.",
        "avg_hotel_price": 180,
        "coords": [45.5513, -78.6015]
    },
    {
        "name": "Tobermory, Ontario",
        "description": "Located on the Bruce Peninsula, this town is a haven for hikers and divers, with crystal-clear turquoise waters and dramatic cliffs.",
        "avg_hotel_price": 240,
        "coords": [45.2559, -81.6661]
    },
    {
        "name": "Thunder Bay, Ontario",
        "description": "A rugged port city on the shore of Lake Superior, anchored by the iconic 'Sleeping Giant' landform and endless outdoor adventures.",
        "avg_hotel_price": 150,
        "coords": [48.3809, -89.2477]
    },
    {
        "name": "Muskoka, Ontario",
        "description": "Famous cottage country with thousands of sparkling lakes, granite outcrops, and charming towns perfect for a lakeside getaway.",
        "avg_hotel_price": 300,
        "coords": [45.0601, -79.6106]
    },

    # --- Quebec ---
    {
        "name": "Montreal, Quebec",
        "description": "A cosmopolitan city blending North American energy with European flair, known for its festivals, cuisine, and historic Old Port.",
        "avg_hotel_price": 230,
        "coords": [45.5017, -73.5673]
    },
    {
        "name": "Mont-Tremblant, Quebec",
        "description": "A premier four-season resort in the Laurentian Mountains, offering incredible skiing and a colorful, European-style pedestrian village.",
        "avg_hotel_price": 310,
        "coords": [46.1189, -74.5960]
    },
    {
        "name": "Percé, Quebec",
        "description": "A picturesque village on the tip of the Gaspé Peninsula, famous for the massive, iconic Percé Rock and Bonaventure Island bird sanctuary.",
        "avg_hotel_price": 190,
        "coords": [48.5230, -64.2144]
    },
    {
        "name": "Tadoussac, Quebec",
        "description": "One of the best whale-watching destinations in the world, located where the Saguenay Fjord meets the St. Lawrence River.",
        "avg_hotel_price": 200,
        "coords": [48.1449, -69.7155]
    },
    {
        "name": "Saguenay Fjord National Park, Quebec",
        "description": "Protecting a majestic and dramatic fjord carved by glaciers, perfect for kayaking, hiking, and exploring breathtaking lookouts.",
        "avg_hotel_price": 170,
        "coords": [48.2917, -70.2520]
    },
    {
        "name": "Îles-de-la-Madeleine, Quebec",
        "description": "A remote archipelago in the Gulf of St. Lawrence known for its red cliffs, sand dunes, and unique Acadian culture.",
        "avg_hotel_price": 250,
        "coords": [47.4165, -61.7057]
    },
    
    # --- The Maritimes ---
    {
        "name": "Fredericton, New Brunswick",
        "description": "New Brunswick's charming capital, a cultural hub with riverside trails, historic architecture, and a renowned art gallery.",
        "avg_hotel_price": 160,
        "coords": [45.9636, -66.6431]
    },
    {
        "name": "Fundy National Park, New Brunswick",
        "description": "Home to the world's highest tides, offering coastal exploration at low tide, lush forests, and dozens of waterfalls.",
        "avg_hotel_price": 180,
        "coords": [45.5925, -65.0543]
    },
    {
        "name": "Hopewell Rocks, New Brunswick",
        "description": "Iconic 'flowerpot' rock formations carved by tidal erosion. Walk on the ocean floor at low tide and kayak around the rocks at high tide.",
        "avg_hotel_price": 170,
        "coords": [45.8202, -64.5778]
    },
    {
        "name": "Cape Breton Highlands National Park, Nova Scotia",
        "description": "Where the mountains meet the sea. The world-famous Cabot Trail winds through this park, offering spectacular ocean vistas.",
        "avg_hotel_price": 210,
        "coords": [46.7210, -60.6508]
    },
    {
        "name": "Lunenburg, Nova Scotia",
        "description": "A UNESCO World Heritage site with brightly coloured buildings, a rich maritime history, and the home port of the famous Bluenose II.",
        "avg_hotel_price": 190,
        "coords": [44.3772, -64.3190]
    },
    {
        "name": "Peggy's Cove, Nova Scotia",
        "description": "An iconic fishing village built on a massive granite outcrop, home to one of the most photographed lighthouses in the world.",
        "avg_hotel_price": 200,
        "coords": [44.4929, -63.9174]
    },
    {
        "name": "Charlottetown, Prince Edward Island",
        "description": "The birthplace of Confederation, a historic city with Victorian architecture, a bustling waterfront, and a vibrant theatre scene.",
        "avg_hotel_price": 220,
        "coords": [46.2382, -63.1311]
    },
    {
        "name": "Cavendish, Prince Edward Island",
        "description": "Home to the Green Gables Heritage Place that inspired 'Anne of Green Gables,' surrounded by red sand beaches and coastal dunes.",
        "avg_hotel_price": 200,
        "coords": [46.4862, -63.3854]
    },

    # --- Newfoundland & Labrador ---
    {
        "name": "Gros Morne National Park, Newfoundland",
        "description": "A geological wonder and UNESCO site where you can walk on the Earth's mantle, cruise freshwater fjords, and hike dramatic tablelands.",
        "avg_hotel_price": 190,
        "coords": [49.5786, -57.7656]
    },
    {
        "name": "Twillingate, Newfoundland",
        "description": "Known as the 'Iceberg Capital of the World,' this charming outport town is a prime spot for viewing icebergs, whales, and coastal scenery.",
        "avg_hotel_price": 180,
        "coords": [49.6521, -54.7677]
    },
    {
        "name": "L'Anse aux Meadows, Newfoundland",
        "description": "The only authenticated Norse site in North America, this UNESCO site offers a glimpse into the life of Vikings in the new world.",
        "avg_hotel_price": 160,
        "coords": [51.5956, -55.5342]
    },
    {
        "name": "Fogo Island, Newfoundland",
        "description": "A remote and ruggedly beautiful island with a thriving artistic community, traditional fishing stages, and the stunning Fogo Island Inn.",
        "avg_hotel_price": 500,
        "coords": [49.6675, -54.1834]
    },

    # --- More Rocky Mountain Adventure ---
    {
        "name": "Canmore, Alberta",
        "description": "A vibrant mountain town just outside Banff National Park, offering world-class hiking, climbing, and a more local mountain-life vibe.",
        "avg_hotel_price": 280,
        "coords": [51.0877, -115.3482]
    },
    {
        "name": "Kananaskis Country, Alberta",
        "description": "A sprawling region of provincial parks in the Rockies, providing a rugged and less-crowded alternative to the national parks.",
        "avg_hotel_price": 300,
        "coords": [50.9161, -115.1408]
    },
    {
        "name": "Ucluelet, British Columbia",
        "description": "Tofino's rugged neighbour on Vancouver Island, famous for the Wild Pacific Trail which offers dramatic coastal storm-watching.",
        "avg_hotel_price": 280,
        "coords": [48.9419, -125.5463]
    },
    {
        "name": "Squamish, British Columbia",
        "description": "The 'Outdoor Recreation Capital of Canada,' situated between Vancouver and Whistler, known for rock climbing, kiteboarding, and hiking.",
        "avg_hotel_price": 250,
        "coords": [49.7018, -123.1554]
    },
    {
        "name": "Gatineau Park, Quebec",
        "description": "A vast conservation park just minutes from Ottawa, offering four-season outdoor activities from hiking and swimming to cross-country skiing.",
        "avg_hotel_price": 180,
        "coords": [45.5218, -75.8702]
    },
    {
        "name": "Prince Albert National Park, Saskatchewan",
        "description": "A transition zone from prairie to boreal forest, this park is a wilderness refuge for free-ranging bison, wolves, and pristine lakes.",
        "avg_hotel_price": 170,
        "coords": [53.9535, -106.3113]
    },
    {
        "name": "Riding Mountain National Park, Manitoba",
        "description": "An island of wilderness rising from the prairies, offering a diverse landscape of forests, grasslands, and lakes.",
        "avg_hotel_price": 160,
        "coords": [50.7679, -100.0520]
    },
# IN YOUR app.py FILE, COMBINE THE LISTS LIKE THIS:
# destinations_data.extend(more_destinations_data)
    {
        "name": "Vancouver, British Columbia",
        "description": "A vibrant coastal city nestled between the mountains and the ocean, known for its scenic beauty and outdoor activities.",
        "avg_hotel_price": 280,
        "coords": [49.2827, -123.1207]
    },
    {
        "name": "Banff, Alberta",
        "description": "A stunning resort town in the heart of the Rocky Mountains, offering breathtaking landscapes and world-class skiing.",
        "avg_hotel_price": 350,
        "coords": [51.1784, -115.5708]
    },
    {
        "name": "Tofino, British Columbia",
        "description": "Canada's surf capital on the rugged west coast of Vancouver Island, famous for its wild beaches and ancient rainforests.",
        "avg_hotel_price": 310,
        "coords": [49.1522, -125.9061]
    },
    {
        "name": "Quebec City, Quebec",
        "description": "A historic treasure with cobblestone streets, 17th-century architecture, and a distinct European charm.",
        "avg_hotel_price": 210,
        "coords": [46.8139, -71.2080]
    },
    {
        "name": "Toronto, Ontario",
        "description": "Canada's largest city, a dynamic multicultural hub featuring iconic landmarks, diverse neighborhoods, and a thriving arts scene.",
        "avg_hotel_price": 250,
        "coords": [43.6532, -79.3832]
    },
    {
        "name": "St. John's, Newfoundland",
        "description": "The easternmost city in North America, known for its colorful row houses, dramatic coastline, and rich maritime history.",
        "avg_hotel_price": 180,
        "coords": [47.5615, -52.7126]
    },
    {
        "name": "Halifax, Nova Scotia",
        "description": "A friendly maritime city with a bustling waterfront, historic sites, and a lively music scene.",
        "avg_hotel_price": 190,
        "coords": [44.6488, -63.5752]
    },
    {
        "name": "Whitehorse, Yukon",
        "description": "The 'Wilderness City' on the banks of the Yukon River, a gateway to the spectacular northern lights and vast natural parks.",
        "avg_hotel_price": 200,
        "coords": [60.7212, -135.0568]
    }
]

# --- Web Routes ---

@app.route('/')
def home():
    """Renders the main page with destination data."""
    return render_template('index.html', destinations=destinations_data)

@app.route('/api/destinations')
def api_destinations():
    """Provides the destination data as a JSON API for the map script."""
    return jsonify(destinations_data)

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)
