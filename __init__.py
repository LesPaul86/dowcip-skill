from mycroft import MycroftSkill, intent_file_handler


class Dowcip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dowcip.intent')
    def handle_dowcip(self, message):
        self.speak_dialog('dowcip')


def create_skill():
    return Dowcip()

