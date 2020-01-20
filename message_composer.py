import json
import constants


def get_message_text(restaurant_data):
    pass

def get_message_email(restaurant_data, subject):
    """
        function to prepare the HTML for the emailer that we have to send.
    """
    # @todo:: remove below line for live.
    # restaurant_data = constants.restaurant_master
    txt_items = []

    # prepare the restaurant data
    for rest in restaurant_data:
        # print("name:: ", rest.get("restaurant").get("name"))
        list_item_template = constants.restaurant_list_template
        rest_name = rest.get("restaurant").get("name")
        rest_add = rest.get("restaurant").get("location").get("address")
        rest_rating = rest.get("restaurant").get("user_rating").get("aggregate_rating")
        rest_cost = rest.get("restaurant").get("average_cost_for_two")
        rest_img = rest.get("restaurant").get("thumb")

        list_item_template = list_item_template.replace("{{{restaurant_name}}}", rest_name)
        list_item_template = list_item_template.replace("{{{restaurant_address}}}", rest_add)
        list_item_template = list_item_template.replace("{{{restaurant_rating}}}", str(rest_rating))
        list_item_template = list_item_template.replace("{{{restaurant_cost}}}", str(rest_cost))
        list_item_template = list_item_template.replace("{{{thumb_url}}}", rest_img)

        txt_items.append(list_item_template)

        # print("name:: {}, \t address:: {} \t rating:: {} \t cost:: {} \t img:: {} ".format(rest_name, rest_add, rest_rating, rest_cost ,rest_img ))


    # prepare email html
    html = constants.email_message_template
    html = html.replace("{{{mail_subject}}}", subject)
    html = html.replace("{{{restaurant_list}}}", "\n ".join(txt_items))

    return html


