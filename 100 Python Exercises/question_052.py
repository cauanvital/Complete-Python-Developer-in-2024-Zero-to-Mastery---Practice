# Define a custom exception class which takes a string message as attribute.

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

raise CustomException('something gone wrong')
