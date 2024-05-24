from pywebio.input import *
from pywebio.output import *
put_table([
    ['Commodity', 'Price'],
    ['Apple', '5.5'],
    ['Banana', '7'],
])

# Text Output
put_text("Hello world!")

# Table Output
put_table([
    ['Commodity', 'Price'],
    ['Apple', '5.5'],
    ['Banana', '7'],
])

# Image Output
#put_image(open('/path/to/some/image.png', 'rb').read())  # local image 
put_image('http://example.com/some-image.png')  # internet image 

# Markdown Output
put_markdown('~~Strikethrough~~')

# File Output
put_file('hello_word.txt', b'hello word!')

# Show a PopUp
popup('popup title', 'popup text content')

# Show a notification message
toast('New message 🔔')


put_table([
    ['Type', 'Content','test'],
    ['html', put_html('X<sup>2</sup>'),'abc'],
    ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
    ['buttons', put_buttons(['A', 'B'], onclick=...)],  
    ['markdown', put_markdown('`Awesome PyWebIO!`')],
    ['file', put_file('hello.text', b'hello world')],
    ['table', put_table([['A', 'B'], ['C', 'D']])]
])