## complete happy with sending email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* information{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* information{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* information{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
* affirm
    - utter_goodbye


## complete happy with sending email + goodbye
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* information{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* information{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* information{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"price": "lesser than 300"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* goodbye
    - utter_goodbye



## conversation with city given and no email option
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* information{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* information{"price": "greater than 700"}
    - slot{"price": "greater than 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "greater than 700"}
* deny
    - utter_goodbye

## conversation with city and email option
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* information{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* information{"price": "greater than 700"}
    - slot{"price": "greater than 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "greater than 700"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* goodbye
    - utter_goodbye


## conversation with city given and no email option with no price preference
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* information{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* information{"price": "no_prefenrence"}
    - slot{"price": "no_prefenrence"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "no_prefenrence"}
* deny
    - utter_goodbye


## conversation with city given and no price preference no email option
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* information{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* information{"price": "no_prefenrence"}
    - slot{"price": "no_prefenrence"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "no_prefenrence"}
* deny
    - utter_goodbye


## conversation with cuisine given and no budget preference with email
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* information{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* information{"price": "no_preference"}
    - slot{"price": "no_preference"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "no_preference"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - utter_goodbye
    - action_restart

## conversation with cuisine given and no budget preference with NO email option
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* information{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* information{"price": "no_preference"}
    - slot{"price": "no_preference"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "no_preference"}
* deny
    - utter_goodbye

## conversation with cuisine and budget preference with NO email option
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* information{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* information{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
* deny
    - utter_goodbye



## conversation with city and cuisine given with email and also invalid email case
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* information{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"price": "more than 700"}
* affirm
    - utter_ask_email
* send_email{"user_email": "nomail@g"}
    - slot{"user_email": "nomail@g"}
    - action_send_email
    - slot{"user_email": null}
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* affirm
    - utter_goodbye

## conversation with city and cuisine given and NO email option
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* information{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"price": "more than 700"}
* deny
    - utter_goodbye


## conversation with budget given and send email
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_ask_location
* information{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* information{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"price": "more than 700"}
* affirm
    - utter_ask_email
* information{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* goodbye
    - utter_goodbye

## conversation with budget given and NO email option
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_ask_location
* information{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* information{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"price": "more than 700"}
* deny
    - utter_goodbye



## conversation with budget and price given with NO email option
* restaurant_search{"price": "lesser than 300", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "lesser than 300"}
    - utter_ask_cuisine
* information{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"price": "lesser than 300"}
* deny
    - utter_goodbye

## conversation with budget and price given with email
* restaurant_search{"price": "lesser than 300", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "lesser than 300"}
    - utter_ask_cuisine
* information{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"price": "lesser than 300"}
* affirm
    - utter_ask_email
* information{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* goodbye
    - utter_goodbye



## conversation with all three inputs given and with email
* restaurant_search{"price": "300 to 700", "cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* goodbye
    - utter_goodbye

## conversation with all three inputs given and with no email option
* restaurant_search{"price": "300 to 700", "cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
* deny
    - utter_goodbye


## conversation with budget and cuisine and no email option
* restaurant_search{"price": "300 to 700", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
    - utter_ask_location
* information{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
* deny
    - utter_goodbye

## conversation with budget and cuisine WITH email option
* restaurant_search{"price": "300 to 700", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
    - utter_ask_location
* information{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
* affirm
    - utter_ask_email
* send_email{"user_email": "matrixbegins@gmail.com"}
    - slot{"user_email": "matrixbegins@gmail.com"}
    - action_send_email
    - slot{"user_email": "matrixbegins@gmail.com"}
    - slot{"cuisine": null}
    - slot{"price": null}
* goodbye
    - utter_goodbye

