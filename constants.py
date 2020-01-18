
allowed_cuisines = ["chinese","mexican","italian","american","south indian","north indian"]

cuisines_mapping = { "chinese":25,  "mexican":73,  "italian":55,  "south indian":85, "american": 1,  "north indian":50  }

allowed_cities = ["bangalore",
"chennai",
"delhi",
"hyderabad",
"kolkata",
"mumbai",
"ahmedabad",
"pune",
"agra",
"ajmer",
"aligarh",
"amravati",
"amritsar",
"asansol",
"aurangabad",
"bareilly",
"belgaum",
"bhavnagar",
"bhiwandi",
"bhopal",
"bhubaneswar",
"bikaner",
"bilaspur",
"bokaro",
"chandigarh",
"coimbatore",
"nagpur",
"cuttack",
"dehradun",
"dhanbad",
"bhilai",
"durgapur",
"erode",
"faridabad",
"firozabad",
"ghaziabad",
"gorakhpur",
"gulbarga",
"guntur",
"gwalior",
"gurgaon",
"guwahati",
"hamirpur",
"hubli-dharwad",
"indore",
"jabalpur",
"jaipur",
"jalandhar",
"jammu",
"jamnagar",
"jamshedpur",
"jhansi",
"jodhpur",
"kakinada",
"kannur",
"kanpur",
"kochi",
"kolhapur",
"kollam",
"kozhikode",
"kurnool",
"ludhiana",
"lucknow",
"madurai",
"malappuram",
"mathura",
"goa",
"mangalore",
"meerut",
"moradabad",
"mysore",
"nanded",
"nashik",
"nellore",
"noida",
"patna",
"pondicherry",
"purulia",
"prayagraj",
"raipur",
"rajkot",
"rajahmundry",
"ranchi",
"rourkela",
"salem",
"sangli",
"shimla",
"siliguri",
"solapur",
"srinagar",
"thiruvananthapuram",
"thrissur",
"tiruchirappalli",
"tiruppur",
"ujjain",
"bijapur",
"vadodara",
"varanasi",
"vasai-virar",
"vijayawada",
"vellore",
"warangal",
"surat",
"visakhapatnam"]


allowed_cities_data = [{'city_id': 4, 'city_name': 'bangalore', 'zomato_city_name': 'Bengaluru', 'lat': 13.004781, 'lon': 77.569029},
{'city_id': 7, 'city_name': 'chennai', 'zomato_city_name': 'Chennai', 'lat': 13.083889, 'lon': 80.27},
{'city_id': 1, 'city_name': 'delhi', 'zomato_city_name': 'Delhi NCR', 'lat': 28.625789, 'lon': 77.210276},
{'city_id': 6, 'city_name': 'hyderabad', 'zomato_city_name': 'Hyderabad', 'lat': 17.366, 'lon': 78.476},
{'city_id': 2, 'city_name': 'kolkata', 'zomato_city_name': 'Kolkata', 'lat': 22.572646, 'lon': 88.363895},
{'city_id': 3, 'city_name': 'mumbai', 'zomato_city_name': 'Mumbai', 'lat': 19.017656, 'lon': 72.856178},
{'city_id': 11, 'city_name': 'ahmedabad', 'zomato_city_name': 'Ahmedabad', 'lat': 23.042662, 'lon': 72.566729},
{'city_id': 5, 'city_name': 'pune', 'zomato_city_name': 'Pune', 'lat': 18.520469, 'lon': 73.85662},
{'city_id': 34, 'city_name': 'agra', 'zomato_city_name': 'Agra', 'lat': 27.18, 'lon': 78.02},
{'city_id': 11303, 'city_name': 'ajmer', 'zomato_city_name': 'Ajmer', 'lat': 26.450431, 'lon': 74.639195},
{'city_id': 11379, 'city_name': 'aligarh', 'zomato_city_name': 'Aligarh', 'lat': 27.8973944, 'lon': 78.0880129},
{'city_id': 11335, 'city_name': 'amravati', 'zomato_city_name': 'Amravati', 'lat': 20.937404, 'lon': 77.779438},
{'city_id': 22, 'city_name': 'amritsar', 'zomato_city_name': 'Amritsar', 'lat': 31.64, 'lon': 74.86},
{'city_id': 11423, 'city_name': 'asansol', 'zomato_city_name': 'Asansol', 'lat': 23.6739452, 'lon': 86.9523954},
{'city_id': 25, 'city_name': 'aurangabad', 'zomato_city_name': 'Aurangabad', 'lat': 19.88, 'lon': 75.32},
{'city_id': 11343, 'city_name': 'bareilly', 'zomato_city_name': 'Bareilly', 'lat': 28.367032, 'lon': 79.430419},
{'city_id': 11382, 'city_name': 'belgaum', 'zomato_city_name': 'Belgaum', 'lat': 15.8496953, 'lon': 74.4976741},
{'city_id': 11384, 'city_name': 'bhavnagar', 'zomato_city_name': 'Bhavnagar', 'lat': 21.7644725, 'lon': 72.1519304},
{'city_id': 11459, 'city_name': 'bhiwandi', 'zomato_city_name': 'Bhiwadi', 'lat': 28.2088, 'lon': 76.8446},
{'city_id': 26, 'city_name': 'bhopal', 'zomato_city_name': 'Bhopal', 'lat': 23.25, 'lon': 77.4167},
{'city_id': 29, 'city_name': 'bhubaneswar', 'zomato_city_name': 'Bhubaneswar', 'lat': 20.27, 'lon': 85.84},
{'city_id': 11346, 'city_name': 'bikaner', 'zomato_city_name': 'Bikaner', 'lat': 28.022937, 'lon': 73.31192},
{'city_id': 11325, 'city_name': 'bilaspur', 'zomato_city_name': 'Bilaspur', 'lat': 22.079625, 'lon': 82.139155},
{'city_id': 11385, 'city_name': 'bokaro', 'zomato_city_name': 'Bokaro', 'lat': 23.6692956, 'lon': 86.151112},
{'city_id': 12, 'city_name': 'chandigarh', 'zomato_city_name': 'Chandigarh', 'lat': 30.737793, 'lon': 76.77515},
{'city_id': 30, 'city_name': 'coimbatore', 'zomato_city_name': 'Coimbatore', 'lat': 11.0183, 'lon': 76.9725},
{'city_id': 33, 'city_name': 'nagpur', 'zomato_city_name': 'Nagpur', 'lat': 21.15, 'lon': 79.09},
{'city_id': 11289, 'city_name': 'cuttack', 'zomato_city_name': 'Cuttack', 'lat': 20.46252, 'lon': 85.882989},
{'city_id': 35, 'city_name': 'dehradun', 'zomato_city_name': 'Dehradun', 'lat': 30.318, 'lon': 78.029},
{'city_id': 11387, 'city_name': 'dhanbad', 'zomato_city_name': 'Dhanbad', 'lat': 23.7956531, 'lon': 86.4303859},
{'city_id': 11345, 'city_name': 'bhilai', 'zomato_city_name': 'Durg Bhilai', 'lat': 21.19385, 'lon': 81.350941},
{'city_id': 11388, 'city_name': 'durgapur', 'zomato_city_name': 'Durgapur', 'lat': 23.5204443, 'lon': 87.3119227},
{'city_id': 11350, 'city_name': 'erode', 'zomato_city_name': 'Erode', 'lat': 11.341037, 'lon': 77.717163},
{'city_id': 1, 'city_name': 'faridabad', 'zomato_city_name': 'Delhi NCR', 'lat': 28.3956, 'lon': 77.319399},
{'city_id': 11541, 'city_name': 'firozabad', 'zomato_city_name': 'Firozabad', 'lat': 27.159083, 'lon': 78.395755},
{'city_id': 1, 'city_name': 'ghaziabad', 'zomato_city_name': 'Delhi NCR', 'lat': 28.641711, 'lon': 77.371731},
{'city_id': 11311, 'city_name': 'gorakhpur', 'zomato_city_name': 'Gorakhpur', 'lat': 26.760574, 'lon': 83.373133},
{'city_id': 11403, 'city_name': 'gulbarga', 'zomato_city_name': 'Gulbarga', 'lat': 17.329731, 'lon': 76.8342957},
{'city_id': 11339, 'city_name': 'guntur', 'zomato_city_name': 'Guntur', 'lat': 16.306655, 'lon': 80.436529},
{'city_id': 11337, 'city_name': 'gwalior', 'zomato_city_name': 'Gwalior', 'lat': 26.218278, 'lon': 78.182815},
{'city_id': 1, 'city_name': 'gurgaon', 'zomato_city_name': 'Delhi NCR', 'lat': 28.494587, 'lon': 77.089595},
{'city_id': 21, 'city_name': 'guwahati', 'zomato_city_name': 'Guwahati', 'lat': 26.146, 'lon': 91.736},
{'city_id': 11768, 'city_name': 'hamirpur', 'zomato_city_name': 'Hamirpur', 'lat': 31.686189, 'lon': 76.521298},
{'city_id': 11374, 'city_name': 'hubli-dharwad', 'zomato_city_name': 'Dharwad', 'lat': 15.458922, 'lon': 75.00781},
{'city_id': 14, 'city_name': 'indore', 'zomato_city_name': 'Indore', 'lat': 22.7252, 'lon': 75.857},
{'city_id': 11336, 'city_name': 'jabalpur', 'zomato_city_name': 'Jabalpur', 'lat': 23.181504, 'lon': 79.986415},
{'city_id': 10, 'city_name': 'jaipur', 'zomato_city_name': 'Jaipur', 'lat': 26.916087, 'lon': 75.809695},
{'city_id': 11306, 'city_name': 'jalandhar', 'zomato_city_name': 'Jalandhar', 'lat': 31.326022, 'lon': 75.576161},
{'city_id': 11307, 'city_name': 'jammu', 'zomato_city_name': 'Jammu', 'lat': 32.726603, 'lon': 74.857022},
{'city_id': 11321, 'city_name': 'jamnagar', 'zomato_city_name': 'Jamnagar', 'lat': 22.470751, 'lon': 70.05768},
{'city_id': 11338, 'city_name': 'jamshedpur', 'zomato_city_name': 'Jamshedpur', 'lat': 22.804575, 'lon': 86.202908},
{'city_id': 11352, 'city_name': 'jhansi', 'zomato_city_name': 'Jhansi', 'lat': 25.448782, 'lon': 78.568405},
{'city_id': 11301, 'city_name': 'jodhpur', 'zomato_city_name': 'Jodhpur', 'lat': 26.241115, 'lon': 73.022906},
{'city_id': 11401, 'city_name': 'kakinada', 'zomato_city_name': 'Kakinada', 'lat': 16.9890648, 'lon': 82.2474648},
{'city_id': 11772, 'city_name': 'kannur', 'zomato_city_name': 'Kannur', 'lat': 11.874634, 'lon': 75.3707},
{'city_id': 23, 'city_name': 'kanpur', 'zomato_city_name': 'Kanpur', 'lat': 26.4607, 'lon': 80.3334},
{'city_id': 9, 'city_name': 'kochi', 'zomato_city_name': 'Kochi', 'lat': 9.97, 'lon': 76.28},
{'city_id': 11334, 'city_name': 'kolhapur', 'zomato_city_name': 'Kolhapur', 'lat': 16.704988, 'lon': 74.243249},
{'city_id': 11472, 'city_name': 'kollam', 'zomato_city_name': 'Kollam', 'lat': 8.8932, 'lon': 82.55},
{'city_id': 11296, 'city_name': 'kozhikode', 'zomato_city_name': 'Kozhikode', 'lat': 11.258792, 'lon': 75.780387},
{'city_id': 11391, 'city_name': 'kurnool', 'zomato_city_name': 'Kurnool', 'lat': 15.8281257, 'lon': 78.0372792},
{'city_id': 20, 'city_name': 'ludhiana', 'zomato_city_name': 'Ludhiana', 'lat': 30.914597, 'lon': 75.849924},
{'city_id': 8, 'city_name': 'lucknow', 'zomato_city_name': 'Lucknow', 'lat': 26.864, 'lon': 80.95},
{'city_id': 11295, 'city_name': 'madurai', 'zomato_city_name': 'Madurai', 'lat': 9.92525, 'lon': 78.119755},
{'city_id': 11775, 'city_name': 'malappuram', 'zomato_city_name': 'Malappuram', 'lat': 11.051235, 'lon': 76.07074},
{'city_id': 11392, 'city_name': 'mathura', 'zomato_city_name': 'Mathura', 'lat': 27.4924134, 'lon': 77.673673},
{'city_id': 13, 'city_name': 'goa', 'zomato_city_name': 'Goa', 'lat': 15.4989, 'lon': 73.8278},
{'city_id': 31, 'city_name': 'mangalore', 'zomato_city_name': 'Mangalore', 'lat': 12.87, 'lon': 74.88},
{'city_id': 11329, 'city_name': 'meerut', 'zomato_city_name': 'Meerut', 'lat': 28.984458, 'lon': 77.706416},
{'city_id': 11393, 'city_name': 'moradabad', 'zomato_city_name': 'Moradabad', 'lat': 28.8386481, 'lon': 78.7733286},
{'city_id': 36, 'city_name': 'mysore', 'zomato_city_name': 'Mysore', 'lat': 12.3, 'lon': 76.65},
{'city_id': 11395, 'city_name': 'nanded', 'zomato_city_name': 'Nanded', 'lat': 19.1382514, 'lon': 77.3209555},
{'city_id': 16, 'city_name': 'nashik', 'zomato_city_name': 'Nashik', 'lat': 20, 'lon': 73.78},
{'city_id': 11396, 'city_name': 'nellore', 'zomato_city_name': 'Nellore', 'lat': 14.4425987, 'lon': 79.986456},
{'city_id': 1, 'city_name': 'noida', 'zomato_city_name': 'Delhi NCR', 'lat': 28.57005, 'lon': 77.32317},
{'city_id': 40, 'city_name': 'patna', 'zomato_city_name': 'Patna', 'lat': 25.611, 'lon': 85.144},
{'city_id': 7, 'city_name': 'pondicherry', 'zomato_city_name': 'Chennai', 'lat': 13.016020371429, 'lon': 80.2465949},
{'city_id': 11859, 'city_name': 'purulia', 'zomato_city_name': 'Purulia', 'lat': 23.331587, 'lon': 86.361695},
{'city_id': 24, 'city_name': 'prayagraj', 'zomato_city_name': 'Allahabad', 'lat': 25.45, 'lon': 81.85},
{'city_id': 11310, 'city_name': 'raipur', 'zomato_city_name': 'Raipur', 'lat': 21.251703, 'lon': 81.629684},
{'city_id': 11294, 'city_name': 'rajkot', 'zomato_city_name': 'Rajkot', 'lat': 22.303894, 'lon': 70.802154},
{'city_id': 11402, 'city_name': 'rajahmundry', 'zomato_city_name': 'Rajahmundry', 'lat': 17.0005383, 'lon': 81.8040345},
{'city_id': 27, 'city_name': 'ranchi', 'zomato_city_name': 'Ranchi', 'lat': 23.35, 'lon': 85.33},
{'city_id': 11358, 'city_name': 'rourkela', 'zomato_city_name': 'Rourkela', 'lat': 22.260435, 'lon': 84.853593},
{'city_id': 11331, 'city_name': 'salem', 'zomato_city_name': 'Salem', 'lat': 11.664338, 'lon': 78.146039},
{'city_id': 11431, 'city_name': 'sangli', 'zomato_city_name': 'Sangli', 'lat': 16.8523973, 'lon': 74.5814773},
{'city_id': 19, 'city_name': 'shimla', 'zomato_city_name': 'Shimla', 'lat': 31.104822, 'lon': 77.173394},
{'city_id': 11327, 'city_name': 'siliguri', 'zomato_city_name': 'Siliguri', 'lat': 26.727101, 'lon': 88.395286},
{'city_id': 11397, 'city_name': 'solapur', 'zomato_city_name': 'Solapur', 'lat': 17.6599188, 'lon': 75.9063906},
{'city_id': 11076, 'city_name': 'srinagar', 'zomato_city_name': 'Srinagar', 'lat': 34.083715, 'lon': 74.79731},
{'city_id': 11290, 'city_name': 'thiruvananthapuram', 'zomato_city_name': 'Trivandrum', 'lat': 8.52414, 'lon': 76.936638},
{'city_id': 11298, 'city_name': 'thrissur', 'zomato_city_name': 'Thrissur', 'lat': 10.527656, 'lon': 76.214427},
{'city_id': 11368, 'city_name': 'tiruppur', 'zomato_city_name': 'Tiruppur', 'lat': 11.108862, 'lon': 77.340996},
{'city_id': 11316, 'city_name': 'ujjain', 'zomato_city_name': 'Ujjain', 'lat': 23.179306, 'lon': 75.784909},
{'city_id': 11480, 'city_name': 'bijapur', 'zomato_city_name': 'Bijapur', 'lat': 16.8302, 'lon': 75.71},
{'city_id': 32, 'city_name': 'vadodara', 'zomato_city_name': 'Vadodara', 'lat': 22.3, 'lon': 73.2003},
{'city_id': 39, 'city_name': 'varanasi', 'zomato_city_name': 'Varanasi', 'lat': 25.282, 'lon': 82.9563},
{'city_id': 3, 'city_name': 'vasai-virar', 'zomato_city_name': 'Mumbai', 'lat': 19.4542657892, 'lon': 72.8068814013},
{'city_id': 11300, 'city_name': 'vijayawada', 'zomato_city_name': 'Vijayawada', 'lat': 16.506195, 'lon': 80.64798},
{'city_id': 11330, 'city_name': 'vellore', 'zomato_city_name': 'Vellore', 'lat': 12.916519, 'lon': 79.1325},
{'city_id': 11372, 'city_name': 'warangal', 'zomato_city_name': 'Warangal', 'lat': 17.969007, 'lon': 79.59393},
{'city_id': 38, 'city_name': 'surat', 'zomato_city_name': 'Surat', 'lat': 21.17, 'lon': 72.83},
{'city_id': 28, 'city_name': 'visakhapatnam', 'zomato_city_name': 'Visakhapatnam', 'lat': 17.6883, 'lon': 83.2186}]


# restaurant_master = [
#     {
#       "restaurant": {
#         "apikey": "f4924dc9ad672ee8c4f8c84743301af5",
#         "id": "18614733",
#         "name": "Garden Grille & Bar - Hilton Garden Inn",
#         "url": "https://www.zomato.com/lucknow/garden-grille-bar-hilton-garden-inn-gomti-nagar?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
#         "location": {
#           "address": "Hilton Garden Inn, TCG 7/7, Vibhuti Khand, Gomti Nagar, Lucknow",
#           "locality": "Gomti Nagar",
#           "city": "Lucknow",
#           "city_id": 8,
#           "latitude": "26.8641216804",
#           "longitude": "81.0082154721",
#           "zipcode": "",
#           "country_id": 1,
#           "locality_verbose": "Gomti Nagar, Lucknow"
#         },
#         "cuisines": "Chinese, Continental, North Indian, Mughlai",
#         "timings": "7 AM to 11 PM",
#         "average_cost_for_two": 2000,
#         "price_range": 4,
#         "currency": "Rs.",
#         "is_zomato_book_res": 0,
#         "mezzo_provider": "OTHER",
#         "is_book_form_web_view": 0,
#         "book_form_web_view_url": "",
#         "book_again_url": "",
#         "thumb": "https://b.zmtcdn.com/data/res_imagery/18614733_RESTAURANT_3a934bb2edaafbe4eeab834d912d9d32.jpg?fit=around%7C200%3A200&crop=200%3A200%3B%2A%2C%2A",
#         "user_rating": {
#           "aggregate_rating": "4.9",
#           "rating_text": "Excelente",
#           "rating_color": "3F7E00",
#           "rating_obj": {
#             "title": {
#               "text": "4.9"
#             }
#           }
#         }
#       }
#     },
#     {
#       "restaurant": {
#         "R": {
#           "has_menu_status": {
#             "delivery": -1,
#             "takeaway": -1
#           },
#           "res_id": 18625649
#         },
#         "apikey": "f4924dc9ad672ee8c4f8c84743301af5",
#         "id": "18625649",
#         "name": "Fusion Flavour",
#         "url": "https://www.zomato.com/lucknow/fusion-flavour-aliganj?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
#         "location": {
#           "address": "Plot 10, Sector 9, Vikas Nagar, Aliganj, Lucknow",
#           "locality": "Aliganj",
#           "city": "Lucknow",
#           "city_id": 8,
#           "latitude": "26.8902184516",
#           "longitude": "80.9616087377",
#           "zipcode": "226024",
#           "country_id": 1,
#           "locality_verbose": "Aliganj, Lucknow"
#         },

#         "cuisines": "North Indian, Biryani, Mughlai, Chinese",
#         "timings": "11 AM to 11 PM",
#         "average_cost_for_two": 750,
#         "price_range": 3,
#         "currency": "Rs.",
#         "mezzo_provider": "ZOMATO_BOOK",
#         "is_book_form_web_view": 0,
#         "book_form_web_view_url": "",
#         "thumb": "https://b.zmtcdn.com/data/pictures/9/18625649/ec3679a39594a9db70935a559cc277ba.jpg?fit=around%7C200%3A200&crop=200%3A200%3B%2A%2C%2A",
#         "user_rating": {
#           "aggregate_rating": "4.7",
#           "rating_text": "Excellent",
#           "rating_color": "3F7E00",
#           "rating_obj": {
#             "title": {
#               "text": "4.7"
#             }
#           }
#         }
#       }
#     }
#   ]


text_message_template = ""

email_message_template = """
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Oxygen Survey</title>

  <style type="text/css">
    img { max-width: 600px; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic;}
    a img { border: none; }
    table { border-collapse: collapse !important;}
    #outlook a { padding:0; }
    .ReadMsgBody { width: 100%; }
    .ExternalClass { width: 100%; }
    .backgroundTable { margin: 0 auto; padding: 0; width: 100% !important; }
    table td { border-collapse: collapse; }
    .ExternalClass * { line-height: 115%; }
    .container-for-gmail-android { min-width: 600px; }

    /* General styling */
    * {font-family: Helvetica, Arial, sans-serif;}

    body {
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: none;
      width: 100% !important;
      margin: 0 !important;
      height: 100%;
      color: #676767;
    }

    td {
      font-family: Helvetica, Arial, sans-serif;
      font-size: 14px;
      color: #777777;
      text-align: center;
      line-height: 21px;
    }

    a {color: #676767;text-decoration: none !important;}
    .pull-left {text-align: left}
    .pull-right {text-align: right}

    .header-lg,
    .header-md,
    .header-sm {
      font-size: 32px;
      font-weight: 700;
      line-height: normal;
      padding: 35px 0 0;
      color: #4d4d4d;
    }

    .header-md {font-size: 24px;}

    .header-sm {
      padding: 5px 0;
      font-size: 18px;
      line-height: 1.3;
      padding-bottom: 30px;
      font-weight: 400;
    }

    .header-rname {
      font-size: 18px;
      line-height: 1.3;
      padding-bottom: 10px;
      font-weight: bolder;
    }
    .content-padding {padding: 20px 0 30px}

    .mobile-header-padding-right {
      width: 290px;
      text-align: right;
      padding-left: 10px;
    }

    .mobile-header-padding-left {
      width: 290px;
      text-align: left;
      padding-left: 10px;
    }

    .free-text {width: 100% !important;padding: 10px 60px 0px;}

    .mini-block-container {
      padding: 30px 50px;
      width: 500px;
    }
    .mini-block {
      background-color: #ffffff;
      width: 498px;
      border: 1px solid #cccccc;
      border-radius: 5px;
      padding: 20px
    }
    .center-txt {padding-left: 40px;}

  td.pull-left.rating{
      font-size: 18px;
    }
    img.rating{
      width: 25px;
      vertical-align: bottom;
      padding-top: 15px;
    }

    .force-width-gmail {
      min-width:600px;
      height: 0px !important;
      line-height: 1px !important;
      font-size: 1px !important;
    }

  </style>

  <style type="text/css" media="screen">
    @import url(http://fonts.googleapis.com/css?family=Oxygen:400,700);
  </style>

  <style type="text/css" media="screen">
    @media screen {
      * {
        font-family: 'Oxygen', 'Helvetica Neue', 'Arial', 'sans-serif' !important;
      }
    }
  </style>

  <style type="text/css" media="only screen and (max-width: 480px)">
    /* Mobile styles */
    @media only screen and (max-width: 480px) {

      table[class*="container-for-gmail-android"] {
        min-width: 290px !important;
        width: 100% !important;
      }

      table[class="w320"] {
        width: 320px !important;
      }

      img[class="force-width-gmail"] {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
      }

      td[class*="mobile-header-padding-left"] {
        width: 160px !important;
        padding-left: 0 !important;
      }

      td[class*="mobile-header-padding-right"] {
        width: 160px !important;
        padding-right: 0 !important;
      }

      td[class="header-lg"] {
        font-size: 24px !important;
        padding: 10px 50px 0 !important;
      }

      td[class="header-md"] {
        font-size: 18px !important;
        padding-bottom: 5px !important;
      }

      td[class="content-padding"] {
        padding: 5px 0 30px !important;
      }

       td[class="button"] {
        padding: 5px !important;
      }

      td[class*="free-text"] {
        padding: 10px 18px 30px !important;
      }

      td[class="mini-block-container"] {
        padding: 8px 20px !important;
        width: 280px !important;
      }

      td[class="mini-block"] {
        padding: 20px !important;
      }

      td[class="center-txt"] {
        padding-left: 3px !important;
      }
    }
  </style>
</head>

<body bgcolor="#f7f7f7">
<table align="center" cellpadding="0" cellspacing="0" class="container-for-gmail-android" width="100%">
  <tr>
    <td align="left" valign="top" width="100%">
      <center>
      <img src="http://s3.amazonaws.com/swu-filepicker/SBb2fQPrQ5ezxmqUTgCr_transparent.png" class="force-width-gmail">
        <table cellspacing="0" cellpadding="0" width="100%" bgcolor="#ffffff" background="http://s3.amazonaws.com/swu-filepicker/4E687TRe69Ld95IDWyEg_bg_top_02.jpg" style="background-color:transparent">
          <tr>
            <td width="100%" height="80" valign="top" style="text-align: center; vertical-align:middle;">
            <!--[if gte mso 9]>
            <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="mso-width-percent:1000;height:80px; v-text-anchor:middle;">
              <v:fill type="tile" src="http://s3.amazonaws.com/swu-filepicker/4E687TRe69Ld95IDWyEg_bg_top_02.jpg" color="#ffffff" />
              <v:textbox inset="0,0,0,0">
            <![endif]-->
              <center>
                <table cellpadding="0" cellspacing="0" width="600" class="w320">
                  <tr>
                    <td class="pull-left mobile-header-padding-left" style="vertical-align: middle;">
                      <a href=""><img width="137" height="47" src="https://imgur.com/TJvmm6c.png" alt="logo"></a>
                    </td>
                    <td class="pull-right mobile-header-padding-right" style="color: #4d4d4d;">
                    </td>
                  </tr>
                </table>
              </center>
              <!--[if gte mso 9]>
              </v:textbox>
            </v:rect>
            <![endif]-->
            </td>
          </tr>
        </table>
      </center>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="100%" style="background-color: #f7f7f7;" class="content-padding">
      <center>
        <table cellspacing="0" cellpadding="0" width="600" class="w320">
          <tr>
            <td class="header-lg">
              {{{mail_subject}}}
            </td>
          </tr>
          <tr>
            <td class="free-text">
              We found following best matches for your search criteria. Let us know how we did :)
            </td>
          </tr>
          <tr>
            <td class="mini-block-container">
              {{{restaurant_list}}}
            </td>
          </tr>
        </table>
      </center>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top" width="100%" style="background-color: #ffffff; border-top:1px solid #cccccc; height: 100px;">
      <center>
        <table cellspacing="0" cellpadding="0" width="600" class="w320">
          <tr>
            <td style="padding: 25px 0 25px">
              <strong>Foodiee: Your food friend</strong><br />

            </td>
          </tr>
        </table>
      </center>
    </td>
  </tr>
</table>
</body>
</html>
"""


restaurant_list_template="""
<table cellspacing="0" cellpadding="0" width="100%"  style="border-collapse:separate !important; padding-bottom: 10px">
  <tr>
    <td class="mini-block">
      <table cellspacing="0" cellpadding="0" width="100%">
        <tr>
          <td width="20%" style="text-align: left">
            <img src="{{{thumb_url}}}" width="80px" alt="1" />
          </td>
          <td  width="80%" style="text-align: left">
            <table cellspacing="0" cellpadding="0" width="100%"  style="border-collapse:separate !important;">
              <tr><td class="header-rname pull-left">{{{restaurant_name}}}</td></tr>
              <tr> <td class="pull-left">{{{restaurant_address}}}</td></tr>
            </table>
          </td>
        </tr>
        <tr>
          <td width="20%" class="pull-left rating">
            <img class="rating" src="http://s3.amazonaws.com/swu-filepicker/JJ7YmPzNQJujBPJq6yVi_star_03.jpg" alt="1" /> {{{restaurant_rating}}}
          </td>
          <td width="80%" class="pull-right">Cost of two: Rs.{{{restaurant_cost}}}</td>
        </tr>
      </table>
    </td>
  </tr>
</table>
"""