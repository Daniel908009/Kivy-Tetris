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
- [] Working display that shows what pieces will be next
- [] Make a mobile phone version (Kivy should make this possible, however I didnt try it out yet)  
- [] Better UI

## Screenshots

## PYPI/HIGH SEAS DEMO LINK (READ THIS IF YOU WANT TO CHECK IT OUT)
<p>The feedback AI at HighSeas told me that a lot of people got confused about what the demo link was, so I wrote this explanation, in case someone doesnt know.</p>
<p>Pypi is sort of like Github, but instead of uploading code, you upload a package.</p>
<p>Package contains everything needed to run a project (code, dependencies, etc.).</p>
<p>You can run the code inside the package by simply running an entry command, this command is different for every project.</p>
<p>To download the package, simply copy the command from the linked Pypi repo.</p>
<p>Link also here: </p>
<p>The copy button is at the top of the page, see image bellow.</p>

<p>After the instalation is done, you can run the package by typing this command: </p>
<p>In case this explanation isnt clear to you, please write it to the HighSeas feedback AI(the why did you vote for x input bar) or write it to me directly through the contact on Slack link. Any feedback is appreciated!</p>