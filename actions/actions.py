# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict

# class ActionSaveUserInfo(Action):
#     def name(self) -> Text:
#         return "action_save_user_info"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     ) -> List[Dict[Text, Any]]:
#         name = tracker.get_slot("name")
#         location = tracker.get_slot("location")
#         # Do something with the user's name and location, such as storing it in a database
#         dispatcher.utter_message("Thanks for providing your information!")
#         return []