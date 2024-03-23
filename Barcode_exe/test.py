# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('Data.db')
# cursor = conn.cursor()

# # Create a table to store the data
# cursor.execute('''CREATE TABLE Data (
#                     id TEXT PRIMARY KEY,
#                     content TEXT
#                 );''')
# conn.commit()

# # Read the file and add its contents to the database
# with open("new.txt", "r") as file:
#     for line in file.readlines():
#         line = line.split()
#         cursor.execute("INSERT INTO Data (id, content) VALUES (?, ?)", (line[0], line[1]))
#         conn.commit()
#         print('Inserted data:', line)

# # Close the database connection
# conn.close()


# f = open('./new.txt', 'w')
# with open('codes.txt', 'r') as file:
#     for content in file.readlines():
#         print(content)
#         new_content = content.split()
#         if len(new_content) > 2:
#             if new_content[0] == '0':
#                 for i in range(int(new_content[0][1::]), int(new_content[1][1::])+1):
#                     f.write(f'0{i} {new_content[2]}')
#                     f.write("\n")
#             else:
#                 for i in range(int(new_content[0]), int(new_content[1])+1):
#                     f.write(f'{i} {new_content[2]}')
#                     f.write("\n")
#         else:
#             f.write(content)
#             f.write("\n")
    

# f.close()
# print("finish")


# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button

# class MyBoxLayout(BoxLayout):
    
#     def __init__(self, **kwargs):
#         super(MyBoxLayout, self).__init__(**kwargs)
        
#         self.text_input = TextInput()
#         self.add_widget(self.text_input)
        
#         self.button = Button(text="Get Value")
#         self.button.bind(on_release=self.on_button_click)
#         self.add_widget(self.button)
    
#     def on_button_click(self, instance):
#         text_value = self.text_input.text
#         print("The value in the TextInput is:", text_value)

# class MyApp(App):
    
#     def build(self):
#         return MyBoxLayout()

# if __name__ == '__main__':
#     MyApp().run()


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class NotificationPopup(Popup):
    
    def __init__(self, **kwargs):
        super(NotificationPopup, self).__init__(**kwargs)
        
        self.title = 'Enter your name'
        
        layout = GridLayout(cols=1)
        
        self.input = TextInput(multiline=False)
        layout.add_widget(self.input)
        
        button = Button(text='Submit', on_press=self.submit)
        layout.add_widget(button)
        
        self.content = layout
    
    def submit(self, instance):
        name = self.input.text
        print('Your name is:', name)
        self.dismiss()

class TestApp(App):
    
    def build(self):
        button = Button(text='Show Popup', on_press=self.show_popup)
        return button
    
    def show_popup(self, instance):
        popup = NotificationPopup()
        popup.open()

if __name__ == '__main__':
    TestApp().run()
