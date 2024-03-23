from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle
import sqlite3 as sql



class NotificationPopup(Popup):
    def __init__(self, **kwargs):
        super(NotificationPopup, self).__init__(**kwargs)
        
        self.title = 'Enter new name'
        layout = GridLayout(cols=1)
        
        self.input = TextInput(multiline=False)
        layout.add_widget(self.input)
        
        button = Button(text='Edit', on_press=self.submit)
        layout.add_widget(button)
        
        self.content = layout
    
    def submit(self, instance):
        new_content = self.input.text
        self.edit(new_=new_content)
        self.dismiss()
    
    def edit(self, new_):
        if content == 'Unknown':
            # Connect to the SQLite database
            conn = sql.connect('Data.db')
            cursor = conn.cursor()
            # Execute an SQL query to retrieve data
            cursor.execute("INSERT INTO Data (id, content) VALUES (?, ?)", (code, new_))
            conn.commit()
            # Close the connectiontable_name
            conn.close()
        else:
            # Connect to the SQLite database
            conn = sql.connect('Data.db')
            cursor = conn.cursor()
            # Execute an SQL query to update data
            cursor.execute("UPDATE Data SET content = ? WHERE id = ?;", (new_, code))
            conn.commit()
            # Close the connection
            conn.close()

class Screen1(FloatLayout):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)

        bg_image           = Image(source='assets/bg.jpg')
        bg_image.opacity   = 0.3
        bg_image.size_hint = (1, 1)
        self.add_widget(bg_image)

        self.entry = TextInput(hint_text='First 3 number ...', size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(self.entry)

        button = Button(text='Search', size_hint=(.2, .1), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button.bind(on_press=self.on_button_click)
        self.add_widget(button)

    def on_button_click(self, instance):
        global code, content
        content = 'Unknown'
        code       = self.entry.text

        # Connect to the SQLite database
        conn = sql.connect('Data.db')
        cursor = conn.cursor()
        # Execute an SQL query to retrieve data
        cursor.execute("SELECT * FROM Data")
        rows = cursor.fetchall()
        # Iterate through the result set and print the data
        for row in rows:
            if row[0] == code:
                content = row[1]
                break
        # Close the connectiontable_name
        conn.close()

        self.parent.switch_to_screen2()

class Screen2(FloatLayout):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

        bg_image           = Image(source='assets/result.jpg')
        bg_image.opacity   = 0.4
        bg_image.size_hint = (1, 1)
        self.add_widget(bg_image)
        
        new2       = content.split('_')
        new2    = ' '.join(new2)

        text_label = Label(text=f'{new2}', color=(1, 1, 1, 1), font_size=30, size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(text_label)

        back  = Button(text='Back', size_hint=(.2, .1), pos_hint={'center_x': 0.4, 'center_y': 0.4})
        back.bind(on_press=self.on_button_click)
        edit = Button(text='Edit', size_hint=(.2, .1), pos_hint={'center_x': 0.6, 'center_y': 0.4})
        edit.bind(on_press=self.edit)
        self.add_widget(back)
        self.add_widget(edit)

    def on_button_click(self, instance):
        self.parent.switch_to_screen1()
    
    def edit(self, instance):
        popup = NotificationPopup()
        popup.open()
        


class MyLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.current_screen = Screen1()
        self.add_widget(self.current_screen)

    def switch_to_screen1(self):
        self.remove_widget(self.current_screen)
        self.current_screen = Screen1()
        self.add_widget(self.current_screen)

    def switch_to_screen2(self):
        self.remove_widget(self.current_screen)
        self.current_screen = Screen2()
        self.add_widget(self.current_screen)

class Bar_code_Rose(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Bar_code_Rose().run()
