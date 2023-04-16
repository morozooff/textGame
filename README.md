<h1 align = "center"> TextGame </h1>
<h1 align = "center" ><img src = "https://media.tenor.com/QPNYQfzQrEEAAAAC/lotr-lord.gif" height = 256></h1>
<h2>Description</h2>
<a> <i>Hello, this is Python text game. Its not about big and deep game project. Its just about learning Python</i> <a>
<h2>Getting Started</h2>
<p>You need Python on your computer. <a href = "https://www.python.org/downloads/">Install Python</a>, if you already didn't it<br>
To <b>start</b> game run on terminal the following commands<br>
To clone this repo on your computer:</p>
  
```
git clone https://github.com/morozooff/textGame.git 
```
<p> To start game on your computer:</p>
  
```
python3 textGame/ex45_game.py 
```
<p><i>Have a nice game!</i></p>
  
<h2>Files</h2>
<p>Lets check the project files.</p>
<h3>ex45_dice_roll.py</h3>
<p>This file realize a dice roll.<br>
In project dice roll used for checks your ability in different situation. This file realize randomizer and minimal interface for user.
</p>

<h3>ex45_artefacts.py</h3>
<p>The game has <b>artefacts</b> - powerful weapons and armor. User gets artefact after victory in battles. User can choice the sort of artefact <b>attack/defend</b>. Every artefact has random buff for user's abilities. <br>
This file realize naming of atefacts, lists contain different verbs.</p>

<h3>ex45_persons.py</h3>
<p>This file realize classes for creating new persons in the game (hero or enemy) and battle system.<br><br>
<b>Firstly</b>, lets speak about persons. Base class - Person. Hero and Enemy inherits Person, but only Hero implement new func.<br>
This classes realize creating abilities (<b>health points, melee, distant, knowledge</b>) of every person and interaction with it, like, you know, print, change, choose ability etc. <br><br>
<b>Secondly</b>, battle system. Battle system based on changing abilities, like, register hit (subtract health points) or different damage methods (enemy have only one sort of damage, but user can choice the sort of damage).<br>  
<i>Battle process:</i><br>
It step-by-step system. Every member of battle makes a turn (start with hero). Hero turn = ability + dice roll, Enemy turn = fixed ability. There is method isAlive, that checks hp status of member, if hp<0, return False and battle end. Else - battle continue.<br>
When battle over, hero get artefact and can choose sort of artefact (look <b>ex45_artefacts.py</b>)
</p>

<h3>ex45_scenes.py</h3>
<p>This file realize Engine and Scenes classes <br>
Scenes its a game locations and different game state (like victory or defeat). <br>
Actual list of scenes:<br>
<ol>
 <li><b>Start</b> - choose game difficulty</li>
 <li><b>Cave</b></li>
 <li><b>Cave entry</b> - first battle location</li>
 <li><b>Fork</b> - choose next room</li>
 <li><b>Horror room</b> - battle room</li>
 <li><b>Fear room</b> - battle room</li>
 <li><b>Mystery room</b> - ⁉️</li>
 <li><b>Boss room</b> - exam🤭</li>
 <li><b>Death</b> - defeat scene😵</li>
 <li><b>Victory</b> - victory scene😎</li>
</ol>
  
Class Map - there is stored reference on every location and methods for interaction with it. <br>
Engine cooperates with class Map and move game forward.
</p>

<h3>ex45_game.py</h3>
<p>This file just create object of class Engine (look <b>ex45_scenes.py</b>) with start localion (object of class Map) and start the game.</p>
