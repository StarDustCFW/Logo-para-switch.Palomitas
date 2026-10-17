
pyinstaller --noconfirm --clean --onefile --noconsole --hidden-import=PIL._tkinter_finder --hidden-import=PIL._imagingtk --icon "temp.png" --add-data "data.txt:." --add-data "logo.png:." --add-data "temp.png:." --add-data "open-folder.png:." --add-data "icon.ico:." "Logo-para-switch.Palomitas.py"
