from pywebio.input import *
from pywebio.output import *


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

put_text('hello').style('color: red; font-size: 20px')

put_text(data)
# in combined output
put_row([
    put_text('hello').style('color: red'),
    put_markdown('markdown')
]).style('margin-top: 20px')

textarea('Code Edit', code={
            'mode': "python",
            'theme': 'darcula',
        }, value='import something\n# Write your python code', name="code")

put_row([
    put_column([
        put_code('A'),
        put_row([
            put_code('B1'), None,  # None represents the space between the output
            put_code('B2'), None,
            put_code('B3'),
        ]),
        put_code('C'),
    ]), None,
    put_code('D', textarea('Code Edit', code={
            'mode': "python",
            'theme': 'darcula',
        }, value='import something\n# Write your python code', name="code")), None,
    put_table([
    ['Type', 'Content','test'],
    ['html', put_html('X<sup>2</sup>'),'abc'],
    ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
    ['buttons', put_buttons(['A', 'B'], onclick=...)],  
    ['markdown', put_markdown('`Awesome PyWebIO!`')],
    ['file', put_file('hello.text', b'hello world')],
    ['table', put_table([['A', 'B'], ['C', 'D']])]
])
])