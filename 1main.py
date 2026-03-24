from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

history = [
    1.21,1.45,2.10,1.05,3.20,
    1.80,1.33,2.50,1.12,4.75,
    1.09,1.67,2.90,1.14,1.28,
    3.60,2.20,1.18,5.10,1.07
]

class AviatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        title = Label(text="PRO AVIATOR PREDICTOR")
        self.output = Label(text="Ready...")

        btn1 = Button(text="ANALYZE")
        btn2 = Button(text="HISTORY")
        btn3 = Button(text="STRATEGY")

        btn1.bind(on_press=self.analyze)
        btn2.bind(on_press=self.show_history)
        btn3.bind(on_press=self.strategy)

        layout.add_widget(title)
        layout.add_widget(self.output)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

    def analyze(self, instance):
        last10 = history[-10:]
        avg = sum(last10) / len(last10)

        reds = [x for x in last10 if x < 2]
        greens = [x for x in last10 if x >= 2]

        if len(reds) >= 6:
            signal = "🔥 BET NOW\nSAFE: 1.5x-2x"
        elif len(greens) >= 6:
            signal = "⚠️ WAIT"
        else:
            signal = "➡️ SMALL BET"

        self.output.text = f"AVG: {avg:.2f}x\n{signal}"

    def show_history(self, instance):
        self.output.text = str(history[-10:])

    def
