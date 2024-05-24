from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server

def main():
	a="2023-09-20"
	input("aaa",type="date",value=a)
start_server(main, port=8080, debug=True)
