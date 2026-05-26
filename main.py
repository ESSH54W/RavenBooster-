from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# Raven (Kuzgun) teması için koyu arka plan
Window.clearcolor = (0.05, 0.05, 0.05, 1) 

class RavenInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=50, spacing=25, **kwargs)
        
        # RavenBooster Başlığı
        self.add_widget(Label(
            text='RAVEN BOOSTER', 
            font_size='35sp', 
            color=(0.6, 0, 1, 1), # Mor renk
            bold=True
        ))
        
        self.status = Label(
            text='Sistem Analizi Bekleniyor...', 
            font_size='16sp',
            color=(0.8,
      
