from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class PageGarde(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Titre très grand et en GRAS
        layout.add_widget(Label(text="E-TRANSACTION\nBIENVENUE", 
                                font_size=40, bold=True, color=(1, 0.5, 0, 1)))
        
        # PIN très grand
        self.pin = TextInput(hint_text="Code PIN", password=True, multiline=False, font_size=30)
        layout.add_widget(self.pin)
        
        btn_acces = Button(text="ACCÉDER", font_size=25, bold=True, background_color=(0, 0.7, 1, 1))
        btn_acces.bind(on_release=self.verifier_pin)
        layout.add_widget(btn_acces)
        
        # Pied de page (Police agrandie)
        pied = Label(text="Sénateur Technologie\n+22667491520 / 70536364 / 69691343", 
                     font_size=18, bold=True, color=(0.5, 0.8, 1, 1))
        layout.add_widget(pied)
        self.add_widget(layout)

    def verifier_pin(self, instance):
        if self.pin.text == "0000":
            self.manager.current = 'form'
        else:
            self.pin.text = ""
            self.pin.hint_text = "PIN ERRONÉ"

class FormulaireScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="REGISTRE CLIENTS", font_size=30, color=(0, 1, 0.5, 1)))
        
        self.ops = Spinner(text="Opérateur", values=("Orange", "Telecel", "Moov", "Sank", "Wave"), font_size=22)
        layout.add_widget(self.ops)
        
        # Champs élargis
        self.nom = TextInput(hint_text="Nom", multiline=False, font_size=22)
        self.prenom = TextInput(hint_text="Prénom", multiline=False, font_size=22)
        self.tel = TextInput(hint_text="Téléphone", multiline=False, font_size=22)
        self.montant = TextInput(hint_text="Montant", multiline=False, font_size=22)
        
        for w in [self.nom, self.prenom, self.tel, self.montant]:
            layout.add_widget(w)
        
        self.affichage = Label(text="Liste des transactions", font_size=18)
        layout.add_widget(self.affichage)
        
        btn_box = BoxLayout(size_hint_y=0.2, spacing=10)
        btn_retour = Button(text="RETOUR", font_size=20, background_color=(1, 0, 0, 1))
        btn_retour.bind(on_release=lambda x: setattr(self.manager, 'current', 'garde'))
        btn_save = Button(text="ENREGISTRER", font_size=20, background_color=(0, 1, 0, 1))
        btn_save.bind(on_release=self.enregistrer)
        btn_voir = Button(text="COMPILATION", font_size=20, background_color=(0, 0.5, 1, 1))
        btn_voir.bind(on_release=self.voir_liste)
        
        for b in [btn_retour, btn_save, btn_voir]: btn_box.add_widget(b)
        layout.add_widget(btn_box)
        self.add_widget(layout)

    def enregistrer(self, instance):
        ligne = f"{self.ops.text} | {self.nom.text} {self.prenom.text} | {self.montant.text}"
        self.data.append(ligne)
        for w in [self.nom, self.prenom, self.tel, self.montant]: w.text = ""

    def voir_liste(self, instance):
        self.affichage.text = "\n".join(self.data)

class ETransactionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PageGarde(name='garde'))
        sm.add_widget(FormulaireScreen(name='form'))
        return sm

if __name__ == '__main__':
    ETransactionApp().run()