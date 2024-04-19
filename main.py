from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Функция для захвата изображений и присвоения им имен
        в соответствии с текущим временем и датой.
        '''
        timestr = time.strftime("%Y%m%d_%H%M%S")
        print("Captured:", timestr)


class TestCamera(App):
    def build(self):
        return CameraClick()

if __name__ == '__main__':
    TestCamera().run()
