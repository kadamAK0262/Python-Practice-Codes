def button_click_handler(event):
    print("Button clicked!")

def register_button_click_handler(button, handler):
    button.on_click(handler)

class Button:
    def __init__(self):
        self.handlers = []

    def on_click(self, handler):
        self.handlers.append(handler)

button = Button()
register_button_click_handler(button, button_click_handler)
