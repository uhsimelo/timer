KEY=wtoirmke
DIR=./
NAME=WorkTime

exe_unixmac: main.py
	pyinstaller main.py --name $(NAME) -F --noupx

exe_window: main.py
	pyinstaller main.py --key $(KEY) --name $(NAME) -F --noconsole

clean:
	rm -r $(DIR)dist/
	rm -r $(DIR)build/
	rm $(DIR)$(NAME)*
