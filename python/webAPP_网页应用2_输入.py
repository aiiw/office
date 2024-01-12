from pywebio.input import *

# Password input
password = input("Input password", type=PASSWORD)

# Drop-down selection
gift = select('Which gift you want?', ['keyboard', 'ipad'])

# Checkbox
agree = checkbox("User Term", options=['I agree to terms and conditions'])

# Single choice
answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

# Multi-line text input
text = textarea('Text Area', rows=3, placeholder='Some text')

# File Upload
img = file_upload("Select a image:", accept="image/*")


data = input_group("Basic info", [ # 1
        input("what's name", type=TEXT, placeholder='This is placeholder',
              help_text='This is help text', required=True, name="name"),
       
        input("Input password", type=PASSWORD, name="password"),

        # Drop-down selection
        select('Which gift you want?', ['keyboard', 'ipad'], name="gift"),

        # Checkbox
        checkbox("User Term", options=['I agree to terms and conditions'], name="term"),

        # Single choice
        radio("Choose one", options=['A', 'B', 'C', 'D'], name="choose"),

        # Multi-line text input
        textarea('Text Area', rows=3, placeholder='Some text', name="text"),

        textarea('Code Edit', code={
            'mode': "python",
            'theme': 'darcula',
        }, value='import something\n# Write your python code', name="code"),
        # File Upload
        file_upload("Select a image:", accept="image/*", name="file")
    ])