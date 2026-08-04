# Simple Keypress Software with Python
This software is a simple and easily modifiable automatic keypressing software that you can for example use to do simple afk movements in any game you need.

## The use of the compiled software
The absoftware.exe file inside the dist folder is the compiled software which will start a fast press of the keyboard's a, s, d and w keys (pressing and holding each key for 0.1 seconds) when the user presses the "start" button. This makes the character on any game just spin around fast in a circle. To stop the virtual keyboard presses, the user can press the "stop button".

The .exe file and all the other required files were built by the following command from the absoftware.py file: pyinstaller --onefile --windowed absoftware.py
