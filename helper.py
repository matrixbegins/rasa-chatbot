import json, re
import constants, zomatopy

def get_slot_value(tracker, slot_name):
    return str(tracker.get_slot(slot_name)).lower()

def is_servicable_city(city_name):
    return city_name.lower() in constants.allowed_cities

def is_valid_cuisine(cuisine_name):
    return cuisine_name.lower() in constants.allowed_cuisines

def map_budget(budget_value):
    bmap = {
        "lesser than 300": {"min": 0, "max": 300},
        "300 to 700": {"min": 300, "max": 700},
        "more than 700": {"min": 700, "max": 25000}
    }
    return bmap.get(budget_value.lower(), None)

def prepare_email_subject(tracker):
    loc = get_slot_value(tracker, 'location')
    cuisine = get_slot_value(tracker, 'cuisine')
    # budget = get_slot_value(tracker, 'budget')

    return "Your {}restaurant search in {}.".format(cuisine + " ", loc)


def is_valid_email(email):
    pattern = "([^@|\s]+@[^@]+\.[^@|\s]+)"
    return re.match(pattern, email, re.M|re.I)


def get_city_details(city_name):
    return list(filter(lambda x: x.get("city_name") == city_name.lower(), constants.allowed_cities_data)).pop()


def search_process_data(city, cuisine, budget ):
    # getting city details of zomato
    cityObj = get_city_details(city)

    # finding the cuisine ID
    cuisine_dict = constants.cuisines_mapping
    if cuisine in cuisine_dict:
        cuisine_search_param = cuisine_dict.get(cuisine)
    else:
        cuisine_search_param = ""

    no_cuisine = False
    no_budget = False
    # performing the search
    dresults = quick_search(cityObj, cuisine_search_param, 10)

    if dresults['results_found'] == 0 and cuisine_search_param > 0:
        # for the given cuisine we couldn't find the search results now search without cuisine
        no_cuisine = True
        dresults = quick_search(cityObj, "", 10)

        # check even if we have results now.... complete city search with no budget and no cuisine ... still no results
        if dresults['results_found'] == 0:
            raise NoDataerror("No results found")

    # now we need to check for budget preference.
    # filter on price of two people if results not in budget, send email of restaurants of all budgets.
    final_results = filter_restaurant_price(dresults["restaurants"], budget)
    if len(final_results) < 5:
        no_budget = True
        final_results = dresults["restaurants"]

    return final_results, no_cuisine, no_budget


def quick_search(cityObj, cuisine_id, limit):
    config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
    zomato = zomatopy.initialize_app(config)

    results = zomato.restaurant_search(query="", latitude=cityObj.get("lat"), longitude=cityObj.get("lon"), cuisines=cuisine_id, limit=limit)
    return json.loads(results)


def filter_restaurant_price(results, budget):
    bdic = map_budget(budget.lower())
    if not bdic:
        return results

    # filter restaurants here.
    out = []
    for data in results:
        if data.get("restaurant").get("average_cost_for_two") >= bdic.get("min") and data.get("restaurant").get("average_cost_for_two") <= bdic.get("max"):
            out.append(data)

    return out



# defining the exception class
class NoDataerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg