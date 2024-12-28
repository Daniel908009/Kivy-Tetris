## What is it?
<p>This project is a Tetris app made in Kivy(multiplatform, naturaly resizable framework for Python)</p>

## Features and goals
- [X] Functional game logic
- [X] Dynamic piece rotating (this took a while because the game grid is asymetrical so I coudnt simply rotate it around, eventualy I figured out a way around it using a copy of the grid that is resized to a square. If this doesnt make sense and you know Python, you can check the code, it is in the moveObject function under if "rotate" statement)
- [X] Resizable tiles that always keep a square shape.
- [X] Basic UI layout
- [X] Basic scoring and colision detection
- [] Piece designer (this is why the rotating was done dynamicaly)
- [] Saving piece designs to a .json file
- [] Switch the drawing to a separate thread from the game logic (this will improve the player experience when resizing the game)
- [] Full settings window
- [] Working display that shows what pieces will be next (this is the white empty rectangle that is currently in the app)
- [] Make a mobile phone version (Kivy should make this possible, however I didnt try it out yet)  
- [] Better UI

## PYPI/HIGH SEAS DEMO LINK (READ THIS IF YOU WANT TO CHECK IT OUT)
<p>The feedback AI at HighSeas told me that a lot of people got confused about what the demo link was, so I wrote this explanation, in case someone doesnt know.</p>
<p>First of all you will need pip to download this project from Pypi, if you do not have it and you still want to try this project, follow this guide: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/</p>
<p>Pypi is sort of like Github, but instead of uploading code, you upload a package.</p>
<p>Package contains everything needed to run a project (code, dependencies, etc.).</p>
<p>You can run the code inside the package by simply running an entry command, this command is different for every project.</p>
<p>To download the package, simply copy the command from the linked Pypi repo (should be something like pip install XYZ).</p>
<p>Link also here: https://pypi.org/project/kivy-tetris-package/ </p>
<p>The copy button is at the top of the page, see image bellow.</p>
![image](https://github.com/user-attachments/assets/3b852bc1-4947-452c-a381-15e4beb35aa9)

<p>After the instalation is done, you can run the package by typing this command: kivy_tetris_package</p>
<p>In case this explanation isnt clear to you, please write it to the HighSeas feedback AI (the why did you vote for x input bar) or write it to me directly through the 'contact on Slack link'. Any feedback is appreciated!</p>

## Screenshots
![image](https://github.com/user-attachments/assets/ab102417-aef8-4689-a3cd-fdc27b72dedb)

<h1>Download instructions</h1>
*Note the links are instructional images <br>
**Note the images used bellow are from a different Github repository, however the overall procces is allways the same. <br>
<h2>Using graphic UI</h2>
<h3>Downloading source code </h3>
First click on the code button as shown in the picture bellow, then click the option Download ZIP <br>
(https://github.com/user-attachments/assets/801a8deb-b6e5-475e-9b6b-262b56fd6a23) <br>
After its downloaded you can find it on your computer through file explorer. After you have found it right click it, it should display option called "Extract" <br>
Click on it and wait a moment. A new directory should appear containing all the files neccesary for the game.<br>
Now open a console and enter the folowing code: pip install -r /path/to/requirements.txt <br>
*Replace the /path/to/requirements.txt with the actual path. <br>
Enjoy! <br>
<h2>Using command prompt</h2>
<h3>Downloading source code </h3>
Open your command prompt and enter the folowing code without the " letters <br>
"https://github.com/Daniel908009/Kivy-Recipe-Finder.git" <br>
This code adress of the site can also be found if you click the code button inside the github repository UI <br>
If you dont have git than first enter the folowing command: sudo apt install git <br>
Now open a console and enter the folowing code: pip install -r /path/to/requirements.txt <br>
*Replace the /path/to/requirements.txt with the actual path. <br>
Enjoy! <br>
