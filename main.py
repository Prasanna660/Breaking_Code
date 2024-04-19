from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from random import choice

def get_quotes():
    qoutes = dict()

    abc = ["a","b","c"]

    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                key = str(i)+str(j)+str(k)
                qoutes[key] = [key+i for i in abc]
    return qoutes

class QuizApp(App):
    def __init__(self, **kwargs):
        super(QuizApp, self).__init__(**kwargs)
        self.answers = []
        self.level = 1
        self.texts = ["1","a"]

    def build(self):
        return self.create_quiz_layout()
   
    def create_quiz_layout(self):
        layout = BoxLayout(orientation='vertical')
        question_label = Label(text=f"Level {self.level} - Choose an option:")
        layout.add_widget(question_label)

        options_layout = BoxLayout(orientation='horizontal')
        for i in range(1, 4):
            option_button = Button(text=str(i), on_press=self.handle_option_selection)
            options_layout.add_widget(option_button)

        layout.add_widget(options_layout)
        return layout

    def handle_option_selection(self, instance):
        selected_option = instance.text
        self.answers.append(selected_option)

        if len(self.answers) < 3:
            self.level += 1

        if len(self.answers) <= 2:
            self.root.clear_widgets()
            self.root.add_widget(self.create_quiz_layout())
        elif len(self.answers) == 3:
            key = ''.join([str(i) for i in self.answers])
            quotes = get_quotes()
            self.texts = quotes[key]
            print(self.texts)
           
            self.display_result()

    def display_result(self):
        result_layout = BoxLayout(orientation='vertical')
        result_label = Label(text=f"Quiz completed! Your answers: {', '.join(self.answers)}")
        result_layout.add_widget(result_label)

        restart_button = Button(text="Let's start the therapy", on_press=self.clear_all)
        result_layout.add_widget(restart_button)

        self.root.clear_widgets()
        self.root.add_widget(result_layout)

    def clear_all(self, instance):
        self.root.clear_widgets()
        self.root.add_widget(self.display_msg())

    def display_msg(self):

        layout = BoxLayout(orientation="vertical")

        self.hello_msg = Label(text="Hello hooman",markup=True,font_size=50)
        layout.add_widget(self.hello_msg)
        restart_button = Button(text="Restart Quiz", size_hint=(.2, .2), size=(100, 50), pos_hint={'right': 1, 'y': 0})
        restart_button.bind(on_press=self.restart_quiz)
        layout.add_widget(restart_button)

        Clock.schedule_interval(self.update_text, 3)

        return layout
   
    def update_text(self, dt):
        txt = choice(self.texts)
        self.hello_msg.text = f'{txt}'

    def restart_quiz(self, instance):
        self.answers = []
        self.level = 1
        self.root.clear_widgets()
        self.root.add_widget(self.create_quiz_layout())

if __name__ == '__main__':
    QuizApp().run()

