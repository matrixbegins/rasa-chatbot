## conversation with cuisine given and no budget preference with email
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* information{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* information{"price": "no_preference"}
    - slot{"price": "no_preference"}
    - slot{"price": "no_preference"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "no_preference"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - utter_goodbye   <!-- predicted: action_send_email -->
    - action_restart


