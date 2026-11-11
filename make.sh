#!/usr/bin/fish

source ~/.venv/bin/activate.fish
pyinstaller --noconfirm --clean --onefile --noconsole --name "Logo-para-switch.Palomitas.elf" --hidden-import=PIL._tkinter_finder --hidden-import=PIL._imagingtk --add-data "data.txt:." --add-data "logo.png:." --add-data "temp.png:." --add-data "open-folder.png:." --add-data "icon.ico:." "Logo-para-switch.Palomitas.py"

