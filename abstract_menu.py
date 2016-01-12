import sys


class Action(object):
    def __init__(self, id, method, description, *method_args):
        self.id = id
        self.method = method
        self.description = description
        self.method_args = method_args

    def execute(self):
        self.method(self.method_args)


class AbstractMenu(object):
    def __init__(self, title, app=None, prev_menu=None):
        self.title = title
        self.actions = []
        self.app = app
        self.prev_menu = prev_menu
        self.register_back_action()

    def register_action(self, id, method, description):
        self.actions.append(Action(id, method, description))

    def register_back_action(self):
        self.actions.append(Action(0, self.back, "Back"))

    def back(self):
        if self.prev_menu:
            self.prev_menu.start()
        else:
            self.app.exit()

    def start(self):
        while True:
            self.print_menu()
            self.choice()

    def choice(self):
        id = input(">> ")
        for action in self.actions:
            if id == action.id:
                action.execute()

    def print_menu(self):
        print self.title
        for action in self.actions:
            print "%s. %s" % (action.id, action.description)


class App(object):
    def exit(self):
        sys.exit(0)


class ExampleMenu(AbstractMenu):
    def __init__(self, title, app, prev_menu):
        AbstractMenu.__init__(self, title, app, prev_menu)
        self.register_action(1, self.say_hi, "Say Hi")

    def say_hi(self):
        print "HI"


if __name__ == "__main__":
    app = App()
    am = ExampleMenu("Exaple Menu", app, None)
    am.start()
