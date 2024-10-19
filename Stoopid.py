from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from plyer import flashlight

class FlashlightApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Create the button widget
        self.flash_button = Button(text="Turn On Flashlight", font_size=32, size_hint=(1, 0.3))
        self.flash_button.bind(on_press=self.toggle_flashlight)
        
        # Add the button to the layout
        layout.add_widget(self.flash_button)

        return layout

    def toggle_flashlight(self, instance):
        # Toggle the flashlight
        if self.flash_button.text == "Turn On Flashlight":
            flashlight.on()
            self.flash_button.text = "Turn Off Flashlight"
        else:
            flashlight.off()
            self.flash_button.text = "Turn On Flashlight"

if __name__ == '__main__':
    FlashlightApp().run()
