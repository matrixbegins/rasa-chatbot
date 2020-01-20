from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy, constants
import emailsender as sender, helper, message_composer
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		print("inside :: ", self.name())
		print(tracker.current_slot_values())

		# getting input values
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = helper.get_slot_value(tracker, 'price')

		if not helper.is_servicable_city(loc):
			dispatcher.utter_message("Oh no! the city you requested is not currently served by us. Care to try another city?")
			return [SlotSet('location',None)]

		try:
			dresults, no_cuisine_flag, no_budget_flag = helper.search_process_data(loc, cuisine, budget)
		except helper.NoDataerror as e:
			print("No data found for city:: {} \t cuisine:: {} \t budget:: {} ".format(loc, cuisine, budget) )
			dispatcher.utter_message("I was unable to find the requested data against your query. Can you try with changing your preferences?")
			return [SlotSet('location',loc)]

		response = "\U0001F374 Showing you the best results from {} \n".format(loc.title())
		response = response + "\n *Your preferences*: Cuisine Type: {} and Budget: {} \n".format(cuisine.title(), budget)

		if no_cuisine_flag:
			response = response + "\n\n The cuisine preference couldn't be matched. Showing all cuisines"
		if no_budget_flag:
			response = response + "\n\n The budget preference couldn't be matched. Showing all restaurants"

		response = response + "\n"
		# display only 5 restaurant to user
		for restaurant in dresults[0:5]:
			# print(restaurant)
			response = response + "\n - *" + restaurant.get("restaurant").get("name") + "*"
			response = response + " in "+ restaurant.get("restaurant").get("location").get("address")
			response = response + " has been rated \U00002B50 {}".format(restaurant.get("restaurant").get("user_rating").get("aggregate_rating"))

		response = response + """\n\n
		Would you like me to share this information on your email ?"""
		dispatcher.utter_message(response)
		return [SlotSet('location',loc), SlotSet('cuisine',cuisine), SlotSet('price',budget)]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		print("inside :: ", self.name())
		print(tracker.current_slot_values())

		# get all slot values.
		# at this point we assume all the valid slots are filled and the information provided is correct
		loc = helper.get_slot_value(tracker, 'location')
		cuisine = helper.get_slot_value(tracker, 'cuisine')
		budget = helper.get_slot_value(tracker, 'price')
		email = helper.get_slot_value(tracker, 'user_email')

		if not helper.is_valid_email(email):
			dispatcher.utter_message("It seems that the given email is invalid. Can you please provide me a correct email?")
			return [SlotSet('user_email',None)]

		try:
			dresults, no_cuisine_flag, no_budget_flag = helper.search_process_data(loc, cuisine, budget)
		except helper.NoDataerror as e:
			print("No data found for city:: {} \t cuisine:: {} \t budget:: {} ".format(loc, cuisine, budget) )
			dispatcher.utter_message("I was unable to find the requested data for sending the email.")
			return [SlotSet('user_email',email)]

		# we have results. parse and show them
		mail_subject = helper.prepare_email_subject(tracker);
		html = message_composer.get_message_email(dresults, mail_subject)

		try:
			sender.send_email_message(mail_subject, email, html)
			dispatcher.utter_message("✅ Email sent to " + email)
			# resetting the slot values to be filled again.
			return [SlotSet('user_email',email), SlotSet('cuisine',None), SlotSet('price',None)]
		except Exception as e:
			print(e)
			dispatcher.utter_message("I am facing a problem in sending the email. \n Please try again in sometime.")
			return [SlotSet('user_email',email), SlotSet('cuisine',None), SlotSet('price',None)]