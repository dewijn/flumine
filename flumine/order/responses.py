import datetime


class Responses:
    """Order responses"""

    def __init__(self):
        self.date_time_created = datetime.datetime.utcnow()
        self.place_response = None
        self.cancel_responses = []
        self.replace_responses = []
        self.update_responses = []
        self.date_time_placed = None

    def placed(self, response):
        self.place_response = response
        self.date_time_placed = datetime.datetime.utcnow()

    def cancelled(self, response):
        self.cancel_responses.append(response)

    def replaced(self, response):
        self.replace_responses.append(response)
        # self.date_time_placed = datetime.datetime.utcnow()  # todo?

    def updated(self, response):
        self.update_responses.append(response)
