from cmu_graphics import *
import cmu_graphics
##### -- Asteroid Blaster Redux -- #####
###
#only turn on when update is still in work
wip = False
###

###credits###
#FastEagle -- lead designer,ideas
#marronCapybara4011 -- lead programmer,ideas
#connor -- playtester :)
#RITISCOLL-random programmer

#the leaderboard is farther down :)

###changelog###
#beta 0.1 4/7/2026
    #added game settings
    #changed laser code to be more compact and optimised
    #changed lose sequence
    #reduced asteroid spawn time to 2 seconds (60 frames)
#beta 0.2 4/8/2026
    #added health bar
    #redid starship deadly collision detection
    #added boss asteroid
    #reworked player movement (made it glide)
    #added comet
    #made ship continue to look at cursor even if dragging (made me annoyed because it looked choppy when spamming)
    #increased boss health since it was too easy to kill
#beta 0.3 4/9/2026
    #made special comet explosion effect (if ur inside the explosion then u get damaged)
    #reduced comet chance since they pile up too quickly farther in the game
    #made player healthbar more dynamic (compatible with higher health values)
#beta 0.4 4/14/26
    #added rapid asteroid (asteroid*2.5)
    #increased minimum spawn rate because its impossible :(
#beta 0.5 4/15/26
    #added shooting star
#beta 0.6 4/17/26
    #added main menu preview (planning to implement for #beta 0.8 4/22/26)
#beta 0.7 4/20/26
    #finalized blackhole and shooting star
    #made comet's speed dependent on app.asteroid_speed
    #made laser an oval
#beta 0.8 4/22/26
    #sorry for the delay i was sick
    #reverted laser back to rectangle
    #fixed comet bug
    #added official main menu along with normal and hard mode
#beta 0.9 4/23/26
    #made ability to return to menu after death
#release 1.0 4/24/26
    #made normal mode actually work after changing from another gamemode
    #also someone made onmousedrag shoot, we quickly fixed that (when i say we i mean me :))
#release 1.1 4/29/26
    #added alien space ship 
#release 1.2 5/6/26
    #alien space ship updates
#release 1.3 5/8/26
    #finally finalized alien space ship
    #rapid asteroid now doesnt go over menu buttons :D
    #added leaderboard settings/options
#release 1.4 5/11/26
    #added leaderboard options
    #all leaderboards open for scores now
#release 1.5 5/12/26
    #added smooth leaderboard transition
    #fixed bug where alien lasers transfered to the next game :|
    #renamed diffuculties to play because people kept getting confused and also recolored it :D
#release 1.6 5/12/26
    #added SHOP
    #added splashtexts!!!!, also to the death screen :)
    #made score submit form (rishi :D)
#release 1.7 5/13/26
    #added wip warning
    #not much else since goofy bug
#release 1.8 5/14/26
    #l1.shop almost done
    #fixed boss asteroid on menu
    #fixed alien ship not getting absorbed by black hole
    #boss asteroid now has different health levels depending on the difficulty
#release 1.9 5/14/26
    #made laser trail
    #fixed boss asteroid not damaging you and not deactivating after you start a new round
    #added charged laser (shop)
#release 2.0 5/19/26
    #made explosions dissipate instead of dissapearing
    #added sounds
    #added low detail mode (bro it looks awful)
#release 2.1 5/20/26
    #added asteroid wall
    #added ingame menu
#release 2.2 11/19/26 (omg gta 6 is out)
    #added a mobile toggle button
    #added mobile back button
    #fixed heatwave persistance on main menu


##### BIG UPDATE
#release 2.2 11/?/?
    ### in progress
    #added ingame menu finishing touches
        #switch between inventory and items in the ingame menu button
        #use [q] and [e] to change between items and powerups when selected
        #use [space] to activate/use powerup or item
    #added main screen customizations
        #hovering over a menu button adds the "square effect"
        #hovering over a menu button enlarges it and highlights it in green
        #added 'floaty effect' to buttons
        #more splashtexts (death included)
        #added sfx to WHOLE main menu
    #added break-off asteroid
    #added metal asteroid
    #optimized 'blackhole' and 'alien ship'
        #blackhole now sucks in asteroids near it instead of just absorbing them
        #added a 'gun' to the alien ship
    #added boss alien ship
    #added 'inventory' along side the ingame menu for powerups
        #items such as the 'repair kit' will now spawn ingame
    #added KEYBINDS
    #added background details/designs
    #added shop buttons
        #'ship customization'
        #'upgrades list'
#release 2.3 ?/?/?
    ### COMING SOON
    
    
    
##### BUGS TO FIX!!
# no bugs to fix
#####

##### Ingame MENU!!! (POWERUPS)
# keybinds - [Q] and [E] to change between purchased powerups
# keybinds - [space] to use powerup
# WILL DISPLAY PICTURE/DESIGN in [Placeholder] 
# WILL DISPLAY AMOUNT OF THAT SPECIFIC POWERUP YOU HAVE PURCHASED in [?] (placeholder)
# DO NOT GET CONFUSED. THE NUMBER HIGHER THAN [Placeholder] IS YOUR SCORE!!!
# when ingame, it will show you what powerup you have equipped and the cost to buy one. (bottom left)
# the goal with this was to make a menu that looked nice whilst not talking up to much space :D👍
#####

##### MINI MENU 3: HEATWAVE CODE
# minimenuHeat = Group(
#     Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
#     Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
#     Label('l.1',113.5, 113, bold=True, size=11, font='orbitron'),
#     Label('[Heatwave]', 170, 113, bold=True, size=13, font='orbitron'),
#     Label('.', 114, 132, bold=True, size=30, font='orbitron'),
#     Label('Sends out a blast of heat that destroys', 206, 132, bold=True, size=8, font='orbitron'),
#     Label('all asteroids hit (excluding blackholes)', 202, 142, bold=True, size=8, font='orbitron'),
#     Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
#     Rect(110, 200.875, 180, 1.5),
#     Label('.', 114, 210, bold=True, size=30, font='orbitron'),
#     Label('If a blackhole obstructs you from', 192.5, 210, bold=True, size=8, font='orbitron'),
#     Label('asteroids, this might save you.', 187, 220, bold=True, size=8, font='orbitron'),
#     )
#####

##### MINI MENU 4: POCKET VACCUM CODE
# minimenuPockVac = Group(
#     Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
#     Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
#     Label('l.1',113.5, 113, bold=True, size=11, font='orbitron'),
#     Label('[Pocket Vaccum]', 189, 113, bold=True, size=13, font='orbitron'),
#     Label('.', 114, 132, bold=True, size=30, font='orbitron'),
#     Label('Sends out a mini vaccum that sucks in', 206, 132, bold=True, size=8, font='orbitron'),
#     Label('all asteroids in vicinty', 170, 142, bold=True, size=8, font='orbitron'),
#     Label('>', 114, 157.5, bold=True, size=15, font='orbitron'),
#     Label('Lasts for 10 seconds, then dissipates', 205, 157.5, bold=True, size=8, font='orbitron'),
#     Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
#     Rect(110, 200.875, 180, 1.5),
#     Label('.', 114, 210, bold=True, size=30, font='orbitron'),
#     Label('BREAK TIME!!! ', 153.5, 210, bold=True, size=8, font='orbitron'),
#     )
#####

##### MINI MENU 5: EXTRA GUN CODE
# minimenuXtraGun = Group(
#     Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
#     Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
#     Label('l.2',114, 113, bold=True, size=11, font='orbitron'),
#     Label('[Extra Gun]', 168, 113, bold=True, size=13, font='orbitron'),
#     Label('.', 114, 132, bold=True, size=30, font='orbitron'),
#     Label('Gives the player an extra laser gun', 200.75, 132, bold=True, size=8, font='orbitron'),
#     Label('that fires an additional laser.', 185.5, 142, bold=True, size=8, font='orbitron'),
#     Label('>', 114, 157.5, bold=True, size=15, font='orbitron'),
#     Label('Goes in the same direction as the', 195.75, 157.5, bold=True, size=8, font='orbitron'),
#     Label('normal laser', 150, 167.5, bold=True, size=8, font='orbitron'),
#     Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
#     Rect(110, 200.875, 180, 1.5),
#     Label('.', 114, 210, bold=True, size=30, font='orbitron'),
#     Label('Cannot be aimed seperately. youll', 197.5, 210, bold=True, size=8, font='orbitron'),
#     Label('have to move your ship.', 175.5, 220, bold=True, size=8, font='orbitron'),
#     )
#####

##### SPRITE 1: HEATWAVE CODE
# spriteHeat = Group(
#     Rect(140, 290, 45, 15, fill=gradient('orange', 'orange', 'red', 'red')),
#     Rect(135, 286.5, 55, 22, fill='orange', opacity=45),
#     )
#####

##### SPRITE 2: POCKET VACCUM CODE
# spritePockVac = Group(
#     Circle(319, 309, 13.25, fill=gradient('red', 'lightCoral'),border='white'),
#     Line(338, 300, 300, 316, fill='white'),
#     Line(298, 297, 339, 313, fill='white')
#     )
#####
###todo list###
##put a "x" inside of each item's "[]" when set item is completed  
#powerups []
#asteroid types []
#level system []
#add expert mode/baby mode options []

###chat### [no deleting messages unless aboslutly necessary] [no editing other people's messages] [no pretending to be others]
#[mc4011]: evan you need to fill the in the game name and your username
#[mc4011]: hey evan, lets put away the forsaken vip please [horse rush sound]
#[mc4011]: EVEY EEEEEEEEEEEEEE
#[mc4011]: could you grab the plans my locker is [redacted]
#[mc4011]: also use the same format as me for chatting plz
#[mc4011]: im serious
#[fe]: michelle jorksalot
#[mc4011]: ok evan goonov
#[mc4011]: thats not the format for typing evan
#[mc4011]: i got the boss working, try getting to 100 points and the boss will spawn
#[fe]: it dosent spin MICHELLE EEEEEE
#[mc4011]: make it spin EVAN EEEEEEE
#[mc4011]: evan i did it i made the movement work
#[mc4011]: now its ur turn to make the main menu and modes or i will send fin after you :)
#[mc4011]: i made the comets
#[mc4011]: also i beat you by 2 points XD
#[fe]: look at the leaderboard you absolute donut
#[mc4011]: i did monkey
#[fe]: also can you make the laser firing normal again so connor can play please
#[mc4011]: remove the first line of the def onstep
#[mc4011]: dont worry about stopping my game cmu bugged out and even if you edit the code i can still play :)
#[fe]: i am working on the shooting star
#[fe]: michelle jorksalot i will work on the main menu on a sandbox
#[mc4011]: YOU NOT EVEN ON THE COLLABORATIVE TASK EVAN JORKSALOT E
#[mc4011]: get on evan eeee
#[mc4011]: ok i got this:
#[fe]: take this model
#[fe]: michelle jorksalot, work on the alien ship eeee
#[fe]: michelle jorksalot, why arent comets and blackholes spawning?
#[fe]: michelle jorksalot, if you go to the bottom of the code, there is the main menu design. please work on it 
#[fe]: michelle jorksalot, im changing the laser back to a rectangle.
#[fe]: FIX IT AHH
#[fe]: Can you make it so that after you press leaderboard and the labels 'normal mode', and the little box arrow that i made go away and come back if you press the button again
#[fe]: rishi please dont edit the code
#[fe]: i could make the speed of the asteroids a specific speed in each mode
#[bO2801]:make the asteroids spawn speen faster   can i do that? ok come down to line 334
#[fe]: fix hardmode activating after pressing return to main menu and selecting normal mode michelle
#[fe]: michelle jorksalot, i have a few ideas. its kinda for cosmetics though and not gameplay
#[fe]: basically when you die at a certain score in any mode, there will be a death message based on how high your score was
#[fe]: scores are 
# 1-100 : pay attention bro
# 101-1000 : you can do better i know you can 
# 1001 - 3rd place player's score: for example: 1001-3455: congrats, your on the podium
# 3rd P score + 1 - 1st place player score : your on the podium, but not in 1st. keep going!!
# 1st P score + 1 - highest score : Congrats, your in first place
#[fe]: next idea is that there will be a random flavortext on the menu everytime you reload the code or press back to main menu
#[fe]: im trying to run the game
#[mc4011]: oh you need much more then just python to run cmu code
#[mc4011]: you need to install pip so that you can get the cmu library
#[mc4011]: and then... that it.
#[mc4011]: library installation with pip is super simple
#[mc4011]: when you install pip all you have to do it type in cmd "pip install cmu_graphics"
#[mc4011]: and then it gets installed
#[mc4011]: all you have to do then is put "import cmu_graphics"
#[mc4011]:https://pypi.org/project/pip/#files
#[fe]: i set it to comic sans so that when we copy the code and paste it into python it wont mess it up
#[fe]: ill put the code to the shop menu at the bottom so you can work on part 1
#[mc4011]: ok, also NO COMIC SANS IT DOESNT  WORK IN CMU 
#[fe]: also tell me when you edit the code so i can update the game in python for players
#[mc4011]: EVAN HOW MANY TIMES DO I HAVE TO TELL YOU, YOU CANT USE COMIC SANS IN CMU!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#[mc4011]: ok i added the shop now what
#[fe]: disable the warning when you press leaderboard mihail nikolov ahhhhh
#[mc4011]: ook
#[C2D7M9]hey mihail
#[C2D7M9]why don't you make the black hole spawn chance to be 1 in a thousand
#[fe]: bro what the heck did you do who the hell is this 
#[mc4011]: ok i made it visual :)
#[mc4011]: i fixed the heatwaves staying on the main menu
#[mc4011]: also thx for setting up the mobile button on every menu!
#[system]: RTISCOLL has joined the chat
#[RTISCOLL]: hi thx for letting me code on this game *cough* i will try to not break it

# ----Asteroid  Designs/Types------#
###
#Default Asteroid (done)
#Boss Asteroid (done)
#Rapid Asteroid(done)
#Asteroid Wall(done)
#Alien Ship(done)
#Comet (done)
#Asteroid Belt
#Shooting Star(done)
#Black Hole(in progress)
###

###leaderboard###
#=======================================#
#=============LEADERBOARD===============#
#=============[Easy Mode]===============#
#1: 
#2: 
#3: 
#=======================================#


#======================================#
#=============LEADERBOARD==============# #BETA Ver 0.0 (original gamemode)
#============[Normal Mode]=============#
#1:  Connor     : 4709   ️👑 Gold
#2:  Evan       : 3455   🥈 Silver
#3:  Mihail     : 2775   🥉 Bronze
#4:  Sreethan   : 802   
#5:  Vrishank   : 432
#=======================================#


#=======================================#
#=============LEADERBOARD===============#
#=============[Hard Mode]===============#
#1: Evan        : 653    👑 Gold
#2: Rowan       : 223   ️ 🥈 Silver
#3: Mihail      : 164    🥉 Bronze
#=======================================#

#=======================================#
#=============LEADERBOARD===============#
#=============[joke mode]===============#
#1:?????????????????????????  :0     👑 Gold
#=======================================#

#####game#####   
import random
from math import *
import time as t
app.setMaxShapeCount(999999999999999)
app.stepsPerSecond = 30
youLoseLabel = Label('Game Over!!', 200, 120, fill='white', font='orbitron', size=20, bold=True, visible=False)
youLoseLabel2 = Label('Score', 200, 160, fill='white', font='orbitron', size=20, bold=True, opacity=0)
youLoseLabel3 = Rect(150, 175, 105, 5, fill='white', opacity=0)
youLoseScore = Label(0, 200, 200, fill='white', bold=True, font='orbitron',border='red', borderWidth=1, size=20, visible=False)
mmllb = Rect(115, 225, 170, 40, fill='lightGrey', border='gray', borderWidth=3, opacity=0)
mmLoseLabelB = Group(
    mmllb,
    Label('Back to Main Menu',200, 245, fill='black',size= 15.5, font='orbitron'),
    )
currencyEarned = Group(
    Label('Moon Rocks Earned:', 160, 350, fill='white', bold=True, font='orbitron', size=20),
    )
currencyEarnedAmt = Label(0, 305, 350, fill='white', bold=True, font='orbitron', size=20, opacity = 0)
    
app.lost = False

app.stepsPerSecond = 30
app.showFontWarnings = False

#settings
#===========================#
app.laser_speed = 10
app.asteroid_speed = -2.3         
app.player_health = 100         
app.boss_min_points = 100
app.min_spawn_rate = 10
app.comet_chance = 10
app.rapid_chance = 20
app.rapid_speed_multiplier = 2.3
app.star_chance = 15
app.bh_chance = 35
app.alien_spaceship_chance = 2
app.asteroid_wall_chance = 30 
#===========================

#external files
#================================
explosionso = []
#================================


flavorText1 = Label('',200,280, fill='white', font='orbitron', size=15, bold=True, opacity=0)
    

    
youLoseScreen = Group(
    Rect(0, 0, 400, 400, fill=gradient('black','black','red'), visible=False),
    youLoseLabel,
    youLoseScore
    )
    

    
app.background = 'black'
app.starAmount = 100
bgStars = Group()
for i in range(app.starAmount):
    bgStars.add(Circle(randrange(0, 400), randrange(0, 400), randrange(1, 3), fill='white'))
    
starship = Group( 
    Polygon(70, 182, 23, 182, 13, 194, 23, 212, 70, 212, 70, 202, 51, 202, 51, 191, 70, 191, 70, 182, fill=gradient('grey', 'darkGrey', 'grey', start='left')),
    Polygon(70, 182, 81, 186, 70, 191, fill=gradient('grey', 'red', start='left')),
    Polygon(70, 212, 81, 202, 70, 202, fill=gradient('grey', 'red', start='left')),
    Rect(27, 188, 20,  20, fill=gradient('red', 'maroon')),
    Rect(31, 176, 40, 3.45, fill='grey'),
    Circle(32, 180, 7, fill=gradient('red', 'fireBrick')),
    )
starship.dy = 0
bossasteroidModel = Star(550, random.randint(40, 360), random.randint(95, 150), 15, fill=gradient('tan', 'grey'), roundness=95)
bossasteroidModel.health = 1000
bossasteroidModel.active = False

#misc groups
explosions = Group()
lasers = Group()
laserstrail = Group()
heatwaves = Group()
pctvcm = Group()

#asteroid groups
asteroids    = Group()
comettrail   = Group()
comets       = Group()
rapidtrail   = Group()
rapid        = Group()  
blackhole    = Group()
sstrail      = Group()
shootingstar   = Group()
alienSP      = Group()
alienlasers = Group()
SPlasertrail = Group()

#healthbar plr
#playerhealthModel determines the position of the entire healthbar
app.plr_health = app.player_health
playerhealthModel = Rect(160, 160, 60, 15, fill='red')
playerhealthBorder = Rect(157,157,66,21,fill=None,border='green',borderWidth = 2,dashes=True)
healthbar = Rect(160, 160, 60, 15, fill='lime')

def moonrocks_give_1000():
    app.moonrocks += 1000

def placeex(x,y):
    if not app.ldmtog:
        explosion = Group(
            Star(200,200,randrange(30,50),20,fill='red'),
            Star(200,200,randrange(20,30),15,fill='orange'),
            Star(200,200,randrange(10,20),10,fill='white')
            )
        explosion.centerX,explosion.centerY = x,y
        explosion.time = 50
        explosions.add(explosion)
    if app.sfxtog: choice(explosionso).play(restart=True)
# center(0, 0, 0.1)
def lose():
    placeex(starship.centerX,starship.centerY)
    # t.sleep(0.5)
    t.sleep(0.5)
    explosions.clear()
    lasers.clear()
    laserstrail.clear()
    asteroids.clear()
    comettrail.clear()
    comets.clear()
    rapidtrail.clear()
    rapid.clear()
    blackhole.clear()
    sstrail.clear()
    shootingstar.clear()
    alienSP.clear()
    alienlasers.clear()
    SPlasertrail.clear()
    bossasteroidModel.centerX,bossasteroidModel.centerY = 550, random.randint(95, 150)
    bossasteroidModel.health = randrange(32,100)
    bossasteroidModel.active = False
    app.dif = False
    app.led = False
    app.cred = False
    app.set = False
    starship.opacity = 0
    starship.centerY = 200
    starship.dy = 0
    app.wait = 0
    app.waittime = 60
    app.waite = 0
    app.waitelime = 10
    playerhealthModel.opacity = 0
    playerhealthBorder.opacity = 0
    app.plr_health = 100
    healthbar.opacity = 0
    youLoseScreen.visible=True
    youLoseScreen.toFront()
    youLoseScore.value = score.value
    youLoseLabel2.toFront()
    youLoseLabel3.toFront()
    youLoseLabel2.opacity=100
    youLoseLabel3.opacity=100
    mmLoseLabelB.opacity=100
    bgStars.toFront()
    mmLoseLabelB.toFront()
    flavorText1.toFront()
    flavorText1.opacity=100
    dt = [
        '10 Pts = 1 Moon Rock',
        'maybe you just genuinly suck at this',
        'your did it!!! (maybe)',
        'gg',
        'did you get absorbed by a blackhole?',
        '3, 2, 1, and (playername here) is dead',
        'go play the original game!! (Asteroids)',
        'top ten saddest anime deaths',
        'ma main goal is to blow up',
        'in space, nobody can hear your screams.',
        'somebody died, i was on break so i didnt see.'
        ':)',
        'Nice light show',
        'stinkin aliens',
        'imagine dying',
        'hey, watch where your remains are floating!',
        'this wont look good on my resume',
        'i know you died to a comet before hitting 10.',
        'dont go sounding like a COD lobby now'
        '[perish]:starship',
        'You reeeeally need the forcefield upgrade..'
        ]
        
    flavorText1.value = random.choice(dt)
    
    
    currencyEarned.toFront()
    currencyEarned.opacity=100
    currencyEarnedAmt.toFront()
    currencyEarnedAmt.opacity=100
    currencyEarnedAmt.value = score.value//10
    app.moonrocks += int(score.value)//10
    score.value = 0
    app.lost = True

m = Circle(200,200,0.1)

#wip warning
w = Label('update in progress',200,200,size=35,fill='white',font='orbitron',bold=True,opacity = 25)

#menu
#===========================
app.in_menu = True

menuBackground = Rect(0,0,400,400)
#rishi
#do not

app.starAmount = 100
menuStars = Group()
for i in range(app.starAmount):
    menuStars.add(Circle(randrange(0, 400), randrange(0, 400), randrange(1, 3), fill='white'))
    
astModel = Group(
    Star(430, randrange(40, 360), randrange(30,55), 15, fill=gradient('tan', 'grey'), roundness=95)
    )

rapidTrailModel = Group()
rapdModel = Group(
    Star(430, randrange(40, 360), randrange(20, 22), 13, fill=gradient('tan', 'grey'), roundness=95)
    )

splashtexts = [
    'pew pew bam!',
    'the game where you can (legally) shoot stuff',
    'share the link with your friends!',
    'IM FIRIN MA LAZER!',
    'tip: shoot the black holes to win',
    'never say never say never!',
    'bro, you left the laser machine on since B. 0.1',
    'officer, i swear the asteroid jumped out at me!',
    'turning off sfx makes the game more realistic',
    'tip 2: eat the asteroids',
    'tip 3: upgrades make the game harder!',
    'dont forget to turn off capslock!!',
    'pro tip: dont die',
    'you will die',
    'couldnt you just go AROUND the asteroids?',
    'Why are moonrocks the main currency?',
    'THATS A GODDANG ASTEROID!!',
    'Goodluck to mobile players',
    'COME NOW COME ALL! Suffer through our game!',
    ]

mainMenuLabel = Label('Asteroid Blaster Redux', 200, 50, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5,rotateAngle=-5)
mainMenuLabel2 = Label(random.choice(splashtexts), 200, 75, fill='white', border='grey', font='arial', bold=True, size=15, borderWidth=1.5,rotateAngle=-5)
##### VERSION LABEL #####
mainMenuLabel3 = Label('ASTEROID BLASTER REDUX | VERSION 2.1', 115, 390, fill='white', font='orbitron', bold=True, size=9,rotateAngle=0)
#####               #####
mainMenuLabel4 = Label('[Backspace] BACK TO MAIN MENU', 110, 366, fill='white', font='orbitron', bold=True, size=10,rotateAngle=0)

wwg = ['yellow' if i%2 == 0 else 'black' for i in range(20)]

wipwarn = Group(
    Rect(5, 360, 390, 20, fill='lightGrey',border=gradient(*wwg,start='left')),
    Label('WARNING: update is in progress, bugs may arise, please be patient. thank you!',200,370,fill='black', font='orbitron', bold=True, size=8.8)
    )
wipwarn.opacity = 0

dLabel = Label('Select a Difficulty', 200, 50, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=-5, opacity=0)
d1frame = Rect(100, 120, 200, 50, fill=gradient('black', 'black', 'black',  'lime'), border='lime', borderWidth=4,opacity=0)
d1 = Group(
    d1frame,
    Label('Casual Mode', 200, 145, fill='lime', font='orbitron', border='green', size=22.5, bold=True,opacity=0),
    )
d2frame = Rect(100, 180, 200, 50, fill=gradient('black', 'black', 'black',  'gold'), border='gold', borderWidth=4,opacity=0)   
d2 = Group(
    d2frame,
    Label('Standard Mode', 200, 205, fill='gold', font='orbitron', border='yellow', size=22.5, bold=True,opacity=0),
    )
d3frame = Rect(100, 240, 200, 50, fill=gradient('black', 'black', 'black',  'red'), border='maroon', borderWidth=4, opacity=0)
d3 = Group(
    d3frame,
    Label('Extreme Mode', 200, 262.5, fill='red', font='orbitron', border='maroon', size=22.5, bold=True, opacity=0),
    )
#lLabel2 = Label('Normal Mode', 200, 20, fill=gradient('grey', 'white', 'white'), border='white', font='orbitron', bold=True, size=15, borderWidth=1.5, rotateAngle=0, opacity=0)
lBoardAT = Group(
    Rect(5, 5, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 5, 5, 390, fill='white',border='grey', opacity=0),          #centerY 90
    Rect(390, 5, 5, 390, fill='white',border='grey', opacity=0),
    Rect(5, 390, 390, 5, fill='white',border='grey', opacity=0),
    )
lBoardAt2 = Group(
    Rect(5, 90, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 140, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 190, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 240, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 290, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 340, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 390, 390, 5, fill='white',border='grey', opacity=0),
    Rect(5, 400, 390, 5, fill='white',border='grey', opacity=0),
    )
#easy is 0, normal is 1, hard is 2, etc...

app.ledstep = 1

nled = Group(
    Label('Player', 70, 120, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=0, opacity=0),
    Rect(260, 90, 5, 390, fill='white', border='grey', opacity=0),
    Label('Score', 328.75, 120, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=0, opacity=0),
    #place
    Label('1:', 30, 165, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('2:', 30, 215, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('3:', 30, 265, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('4:', 30, 315, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('5:', 30, 365, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    #player
    Label('Cyn',95, 165, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Connor',95, 215, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Evan',95, 265, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Mihail',95, 315, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Rowan',95, 365, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    #score
    Label('5417',330, 165, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('4709',330, 215, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('3455',330, 265, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('2828',330, 315, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('906',330, 365, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0)
)
hled = Group(
    Label('Player', 70, 120, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=0, opacity=0),
    Rect(260, 90, 5, 390, fill='white', border='grey', opacity=0),
    Label('Score', 328.75, 120, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=0, opacity=0),
    #place
    Label('1:', 30, 165, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('2:', 30, 215, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('3:', 30, 265, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('4:', 30, 315, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('5:', 30, 365, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    #player
    Label('Connor',95, 165, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Evan',95, 215, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Rishi',95, 265, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Mihail',95, 315, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Aryan',95, 365, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    #score
    Label('776',330, 165, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('460',330, 215, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('146',330, 265, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('124',330, 315, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('17',330, 365, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0)
)
hled.centerX = 600
eled = Group(
    Label('Player', 70, 120, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=0, opacity=0),
    Rect(260, 90, 5, 390, fill='white', border='grey', opacity=0),
    Label('Score', 328.75, 120, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=0, opacity=0),
    #place
    Label('1:', 30, 165, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('2:', 30, 215, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('3:', 30, 265, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('4:', 30, 315, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    Label('5:', 30, 365, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, opacity=0),
    #player
    Label('Evan',95, 165, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Rishi',95, 215, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Aadith',95, 265, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Max',95, 315, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('Rowan',95, 365, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    #score
    Label('1399',330, 165, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('400',330, 215, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('285',330, 265, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('67',330, 315, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0),
    Label('50',330, 365, fill='white', border='grey', font='orbitron', bold=True, size=16.5, borderWidth=1.5, opacity=0)
)
eled.centerX = -200
lL1 = Label('Casual Leaderboard', eled.centerX, 50, fill=gradient('grey', 'white'), border='white', font='orbitron', bold=True, size=18, borderWidth=1.5, rotateAngle=-5, opacity=0)
lL2 = Label('Standard Leaderboard', nled.centerX, 50, fill=gradient('grey', 'white'), border='white', font='orbitron', bold=True, size=16, borderWidth=1.5, rotateAngle=-5, opacity=0)
lL3 = Label('Extreme Leaderboard', hled.centerX, 50, fill=gradient('grey', 'white'), border='white', font='orbitron', bold=True, size=17.5, borderWidth=1.5, rotateAngle=-5, opacity=0)
leds = Group(hled,lL3,nled,lL2,eled,lL1)
leds.dx = 0
e = 600
n = 200
h = -200

lButton2 = Group(
    Rect(310, 30, 50, 50, fill='lightGrey', border='gray', borderWidth=3, opacity=0),
    RegularPolygon(330, 54, 20, 3,fill='lightGrey', border='gray', borderWidth=10, rotateAngle=90, opacity=0),
    )
lButton1 = Group(
    Rect(310, 30, 50, 50, fill='lightGrey', border='gray', borderWidth=3, opacity=0),
    RegularPolygon(330, 54, 20, 3,fill='lightGrey', border='gray', borderWidth=10, rotateAngle=90, opacity=0),
    )
lButton1.rotateAngle = 180
lButton1.centerX = 62

cLabel = Label('Credits', 200, 50, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=-5, opacity=0)
Credits1 = Label('marronCapybara4011: Programmer, ideas', 200, 120, fill='white', border='grey', font='orbitron', bold=True, size=17.5, borderWidth=1.5, rotateAngle=0, opacity=0)
Credits2 = Label('FastEagle: Designer, ideas', 200, 160, fill='white', border='grey', font='orbitron', bold=True, size=17.5, borderWidth=1.5, rotateAngle=0, opacity=0)
Credits3 = Label('red_Immune_Cell-_-C2D7M9_1472: ideas', 200, 200, fill='white', border='grey', font='orbitron', bold=True, size=16, borderWidth=1.5, rotateAngle=0, opacity=0)
Credits4 = Label('blueOtter2801: Website Developer', 200, 240, fill='white', border='grey', font='orbitron', bold=True, size=16, borderWidth=1.5, rotateAngle=0, opacity=0)

formLab = Group(
    Label('to submit your score, follow this link:',200,180,fill='white', border='grey', font='orbitron', bold=True, size=16, borderWidth=1.5),
    Label('https://tinyurl.com/submitformblueotter',200,200,fill='white', border='grey', font='orbitron', bold=True,size=16, borderWidth=1.5),
    )
formLab.opacity = 0

app.sfxtog = False
app.ldmtog = False
app.mmtog = False
app.spawnX=450
app.spawnY=360

sLabel = Label('Settings', 200, 50, fill='white', border='grey', font='orbitron', bold=True, size=25, borderWidth=1.5, rotateAngle=-5)

    
sfxButton=Rect(200, 100, 60, 40, fill='lightGrey', border='red', borderWidth=3, opacity=0)

sfxLabel = Label('Off', 230, 120, fill='black', size=15.5, font='orbitron', opacity=0)

sfx = Group(
    Label('Sound Effects:', 100, 120, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, rotateAngle=0, opacity=0),
    sfxButton,
    sfxLabel,
    )    
    
    
ldmButton=Rect(200, 150, 60, 40, fill='lightGrey', border='red', borderWidth=3, opacity=0)
ldmLabel = Label('Off', 230, 170, fill='black', size=15.5, font='orbitron', opacity=0)
ldm = Group(
    Label('Low Detail Mode:', 100, 170, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, rotateAngle=0, opacity=0),
    ldmButton,
    ldmLabel,
    )

mmButton = Rect(200, 200, 60, 40, fill='lightGrey', border='red', borderWidth=3, opacity=0)
mmLabel = Label('Off', 230, 220, fill='black', size=15.5, font='orbitron', opacity=0)
mm = Group(
    Label('Mobile Mode:', 100, 220, fill='white', border='grey', font='orbitron', bold=True, size=20, borderWidth=1.5, rotateAngle=0, opacity=0),
    mmButton,
    mmLabel,
    )

keybds = Group(
    Rect(22, 19, 90, 40, fill='lightGrey', border='gray', borderWidth=3, opacity=0),
    Label('Keybinds',67, 37, fill='black', size=15.5, font='orbitron', opacity=0),
    )
    
mmbbb = Rect(265, 350, 140, 40, fill='lightGrey', border='gray', borderWidth=3, opacity=0)
mmBackButtonB = Group(
    mmbbb,
    Label('Back to Main Menu',mmbbb.centerX, mmbbb.centerY, fill='black',size= 12, font='orbitron', opacity=0),
    )

powerUpMenu = Group(
    Rect(20, 100, 360, 280, fill='lightGrey', border='gray', borderWidth=5),
    )
powerUpMenu.opacity = 0

astModelDeco = Group(
    Star(34, 364, 14, 15, fill=gradient('tan', 'grey'), roundness=95),
    Star(34, 356, 14, 15, fill=gradient('tan', 'grey'), roundness=95),
    Star(50, 364, 14, 15, fill=gradient('tan', 'grey'), roundness=95),
    Star(50, 364, 14, 15, fill=gradient('tan', 'grey'), roundness=95),
    Star(64, 364, 14, 15, fill=gradient('tan', 'grey'), roundness=95),
    Star(78, 364, 14, 15, fill=gradient('tan', 'grey'), roundness=95),
    )
astModelDeco.opacity = 0
lasModels = Group(
    Rect(25, 230, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-20),
    Rect(45, 231, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-10),
    Rect(52, 224, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=20),
    Rect(43, 222, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-40),
    Rect(77, 230, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-20),
    Rect(85, 226, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-10),
    Rect(92, 233, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=20),
    Rect(64, 234, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-16),
    Rect(115, 230, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-10),
    Rect(110, 235, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=20),
    Rect(64, 234, 20, 10, fill=gradient('red', 'maroon'), rotateAngle=-16),
    )
lasModels.opacity = 0
superChargedlasModels = Group(
    Rect(33, 312, 20, 10, fill=gradient('red', 'orange'), rotateAngle=-20),
    Rect(25, 310, 20, 10, fill=gradient('red', 'orange'), rotateAngle=15),
    Rect(57, 314, 20, 10, fill=gradient('red', 'orange'), rotateAngle=15),
    Rect(67, 311, 20, 10, fill=gradient('red', 'orange'), rotateAngle=15),
    Rect(52, 316, 20, 10, fill=gradient('red', 'orange'), rotateAngle=5),
    Rect(91, 316, 20, 10, fill=gradient('red', 'orange'), rotateAngle=-20),
    Rect(105, 314, 20, 10, fill=gradient('red', 'orange'), rotateAngle=5),
    Rect(86, 310, 20, 10, fill=gradient('red', 'orange'), rotateAngle=15),
    Rect(67, 311, 20, 10, fill=gradient('red', 'orange'), rotateAngle=20),
    Rect(123, 311, 20, 10, fill=gradient('red', 'orange'), rotateAngle=-25),
    )
superChargedlasModels.opacity = 0

heatWaveModel = Group(
    Rect(267, 226, 100, 15, fill=gradient('orange', 'orange', 'red', 'red')),
    )
heatWaveModel2 = Group(
    Rect(262, 223, 110, 25, fill='orange', opacity=0),
    )
heatWaveModel.opacity = 0
pocketVaccumModel = Group(
    Circle(319, 309, 13.25, fill=gradient('red', 'lightCoral'),border='white'),
    Line(338, 300, 300, 316, fill='white'),
    Line(298, 297, 339, 313, fill='white')
    )
pocketVaccumModel.opacity = 0
pocketVaccumModel2 = Group(
    Circle(319, 309, 13.25, fill=gradient('red', 'lightCoral'),border='white'),
    Line(338, 300, 300, 316, fill='white'),
    Line(298, 297, 339, 313, fill='white')
    )
pocketVaccumModel2.opacity = 0
pocketVaccumModel3 = Group(
    Circle(319, 309, 13.25, fill=gradient('red', 'lightCoral'),border='white'),
    Line(338, 300, 300, 316, fill='white'),
    Line(298, 297, 339, 313, fill='white')
    )
pocketVaccumModel3.opacity = 0
starShipModel = Group(
    Polygon(70, 182, 23, 182, 13, 194, 23, 212, 70, 212, 70, 202, 51, 202, 51, 191, 70, 191, 70, 182, fill=gradient('grey', 'darkGrey', 'grey', start='left')),
    Polygon(70, 182, 81, 186, 70, 191, fill=gradient('grey', 'green', start='left')),
    Polygon(70, 212, 81, 202, 70, 202, fill=gradient('green', 'darkGreen')),
    Rect(27, 188, 20, 20, fill=gradient('lime', 'green')),
    Rect(31, 176, 40, 3.45, fill='grey'),
    Circle(32, 180, 7, fill=gradient('green', 'darkGreen')),
    )
starShipModel.opacity = 0
upgradesLabel = Group(
    Rect(81, 100, 5, 37, fill=None, border='grey'),
    Label('Upgrades', 83, 140, fill='white',border='dimgrey', borderWidth=1, bold=True, font='orbitron', size=18),
    )
upgradesLabel.opacity = 0
powerupsLabel = Group(
    Rect(319, 100, 5, 37, fill=None, border='grey'),
    Label('Powerups', 321, 140, fill='white', border='dimGrey', borderWidth=1, bold=True, font='orbitron', size=18),
    )
powerupsLabel.opacity = 0

shipCst = ""
    
shelf1 = Group(
    Rect(23, 163, 120, 10, fill='dimGrey', opacity=50),
    Rect(23, 163, 125, 5, fill='grey'),
    )
shelf1.opacity = 0

shelf2 = Group(
    Rect(23, 243, 120, 10, fill='dimGrey', opacity=50),
    Rect(23, 243, 125, 5, fill='grey'),
    )
shelf2.opacity = 0
shelf3 = Group(
    Rect(23, 323, 120, 10, fill='dimGrey', opacity=50),
    Rect(23, 323, 125, 5, fill='grey'),
    )
shelf3.opacity = 0
shelf4 = Group(
    Rect(258, 163, 120, 10, fill='dimGrey', opacity=50),
    Rect(252, 163, 125, 5, fill='grey'),
    )

shelf4.opacity = 0
shelf5 = Group(
    Rect(258, 323, 125, 10, fill='dimGrey', opacity=50),
    Rect(252, 323, 125, 5, fill='grey'),
    )
shelf5.opacity = 0
shelf6 = Group(
    Rect(258, 243, 125, 10, fill='dimGrey', opacity=50),
    Rect(252, 243, 125, 5, fill='grey'),
    )
shelf6.opacity = 0
moonRocksCount = Group(
    Rect(278, 127, 5, 30, fill='grey'),
    Rect(328, 127, 5, 30, fill='grey'),
    Rect(254, 134, 100, 40, fill='grey', border='dimGrey'),
    )
moonRocksCount.opacity = 0
mRLabel = Group(
    Label('Moon Rocks', 304, 142.5, fill='white', bold=True, font='orbitron'),
    Rect(257, 150, 94, 2, fill='white'),
    )
mRLabel.opacity = 0
mRAmount = Label(0, 304, 161, fill='white', bold=True, font='orbitron')
mRAmount.opacity = 0
    
Frame1 = Group(
    Rect(47, 170, 5, 15, fill='grey'),
    Rect(120, 170, 5, 15, fill='grey'),
    Rect(36, 180, 98, 30, fill='grey', border='dimGrey', borderWidth=2),
    Label('Drag Upgrade',85, 186, fill='white', bold=True, font='orbitron'),
    Rect(40, 193, 91, 5, fill='white', border='grey', borderWidth=2),
    Label('100 Moon Rocks',85, 202, fill='white', bold=True, font='orbitron', size=10),
    )
Frame1.opacity = 0

Frame2 = Group(
    Rect(47, 251, 5, 15, fill='grey'),
    Rect(120, 251, 5, 15, fill='grey'),
    Rect(36, 261, 98, 30, fill='grey', border='dimGrey', borderWidth=2),
    Label('Charged Lasers',85, 268, fill='white', bold=True, font='orbitron', size=9.75),
    Rect(40, 273, 91, 5, fill='white', border='grey', borderWidth=2),
    Label('150 Moon Rocks',85, 282, fill='white', bold=True, font='orbitron', size=9.75),
    )
Frame2.opacity = 0
Frame3 = Group(
    Rect(279, 170, 5, 15, fill='grey'),
    Rect(356, 170, 5, 15, fill='grey'),
    Rect(270, 180, 98, 30, fill='grey', border='dimGrey', borderWidth=2),
    Label('Heatwave',319, 187, fill='white', bold=True, font='orbitron', size=11),
    Rect(274, 193, 91, 5, fill='white', border='grey', borderWidth=2),
    Label('20 Moon Rocks',319, 202, fill='white', bold=True, font='orbitron', size=9.75),
    )
Frame3.opacity = 0
Frame4 = Group(
    Rect(279, 251, 5, 15, fill='grey'),
    Rect(356, 251, 5, 15, fill='grey'),
    Rect(270, 261, 98, 30, fill='grey', border='dimGrey', borderWidth=2),
    Label('Pocket Vacuum',319, 268, fill='white', bold=True, font='orbitron', size=10),
    Rect(274, 273, 91, 5, fill='white', border='grey', borderWidth=2),
    Label('30 Moon Rocks',319, 283, fill='white', bold=True, font='orbitron', size=9.75),
    )
Frame4.opacity = 0
flag = Group(
    Polygon(175, 171, 228, 171, 228, 235, 202, 271, 175, 235, fill=gradient('red', 'maroon'), border='gold'),
    Circle(202, 205, 15, fill=gradient('grey', 'gainsboro')),
    Circle(195, 199, 4, fill='grey'),
    Circle(209, 208, 4, fill='grey'),
    )
flag.opacity = 0

buyupnoti = 30
app.curnoti = buyupnoti

Purchased = Group(
    Label('Purchased!', 200, 350, fill='lime', border='green', bold=True, size=15, borderWidth=1, font='orbitron', opacity=0),
    )
InsufficientFunds = Group(
    Label('Insufficient Funds', 200, 350, fill='red', border='maroon', bold=True, size=15, borderWidth=1, font='orbitron', opacity=0),
    )

pwlabel = Label('Shop', 200, 50, fill='white', border='gray', bold=True, font='orbitron', size=25, borderWidth=1.5, rotateAngle=-5)
pwlabel.opacity = 0
shopL = Label('L.1', 200, 75, fill='white', border='gray', bold=True, font='orbitron', size=19.75, borderWidth=1.5, rotateAngle =-5)
shopL.opacity = 0
tb1frame = Rect(50, 120, 120, 40, fill='lightGrey', border='grey', borderWidth=5)
playlab = Label('Play',110, 140, fill='black',size= 15.5, bold=True, font='orbitron')
playIcon = RegularPolygon(185, 140, 14, 3,fill='black', border='grey', borderWidth=3, rotateAngle=90)
tB1 = Group(
    tb1frame,
    playlab,
    playIcon,
    )

tb2frame = Rect(210, 120, 120, 40, fill='lightGrey', border='grey', borderWidth=5)
setIcon = Group(
    RegularPolygon(350, 140, 14, 6, fill='grey', border='grey', borderWidth=3, rotateAngle=30),
    Circle(350, 140, 7, fill='black'),
    )
tB2 = Group(
    tb2frame,
    setIcon,
    Label('Settings',272.5,140,fill='black',size= 15.5, bold=True, font='orbitron')
    )
tb3frame = Rect(310, 300, 80, 40, fill='lightGrey', border='gray', borderWidth=5)
tB3 = Group(
    tb3frame,
    Label('Credits',350,320,fill='black',size= 15.5,bold=True,  font='orbitron')
    )

tb4frame = Rect(210, 175, 120, 40, fill='lightGrey', border='grey', borderWidth=5)
ledIcon = Group(
    Rect(340, 200, 6, 15, fill='grey'),
    Rect(349, 195, 6, 20, fill='grey'),
    Rect(358, 205, 6, 10, fill='grey'),
    )
tB4 = Group(
    tb4frame,
    ledIcon,
    Label('Leaderboard',270,195,fill='black',size= 14.5,bold=True,  font='orbitron')
    )

tb5frame = Rect(50, 175, 120, 40, fill='lightGrey', border='grey', borderWidth=5)
shopIcon = Group(
    Polygon(179, 190, 199, 190, 193, 199, 183, 199, fill='grey'),
    Line(183, 196, 183, 205, fill='grey', lineWidth=3),
    Line(183, 205, 195, 205, fill='grey', lineWidth=3),
    Line(183, 192, 175, 183, fill='grey', lineWidth=3),
    Circle(184, 207, 3, fill='grey'),
    Circle(194, 207, 3, fill='grey'),
    )
tB5 = Group(
    tb5frame,
    shopIcon,
    Label('Shop', 110, 195, fill='black', size=15.5, bold=True, font='orbitron')
    )
    
tb6frame = Rect(270, 350, 120, 40, fill='lightGrey', border='gray', borderWidth=5)
tB6 = Group(
    tb6frame,
    Label('Submit Score', 330, 369, fill='black', size=15, bold=True,  font='orbitron'),
    )


app.rotateflag =False
app.count=0
app.dif = False
app.led = False
app.cred = False
app.set = False
app.setkeybds = False
app.sho = False
app.form = False


app.drag = False
app.charged = False
app.heat = 0
app.poctvacc = 0

pows = ['heatwave','pocket vaccum']
app.selit = 0


heatcdsec = 30
pctcdsec = 20
app.pctcd = False
app.heatcd = False
app.heatcooldown = heatcdsec*app.stepsPerSecond
app.pctcooldown = heatcdsec*app.stepsPerSecond

cornerEffect1 = Group(
    Rect(68, 128, 15, 4, fill='white'),
    Rect(68, 128, 4, 15, fill='white'),
    )
cornerEffect2 = Group(
    Rect(176, 128, 15, 4, fill='white'),
    Rect(187, 128, 4, 15, fill='white'),
    )
cornerEffect3 = Group(
    Rect(68, 175, 4, 15, fill='white'), 
    Rect(68, 188, 15, 4, fill='white'),
    )
cornerEffect4 = Group(
    Rect(187, 175, 4, 15, fill='white'), 
    Rect(176, 188, 15, 4, fill='white'),
    )

minimenuDrag = Group(
    Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
    Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
    Label('l.1',113.5, 113, bold=True, size=11, font='orbitron'),
    Label('[Drag Upgrade]', 180, 113, bold=True, size=13, font='orbitron'),
    Label('.', 114, 132, bold=True, size=30, font='orbitron'),
    Label('Allows you to dragfire lasers for 2', 200, 132, bold=True, size=8, font='orbitron'),
    Label('seconds indicated by a charge meter', 200, 142, bold=True, size=8, font='orbitron'),
    Label('.', 114, 160, bold=True, size=30, font='orbitron'),
    Label('Charge meter takes 15 seconds to fill', 205, 160, bold=True, size=8, font='orbitron'),
    Label('>', 114, 170, bold=True, size=15, font='orbitron'),
    Label('Ability wont work unless charge meter', 207.75, 170, bold=True, size=8, font='orbitron'),
    Label('is full', 133.25, 180, bold=True, size=8, font='orbitron'),
    Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
    Rect(110, 200.875, 180, 1.5),
    Label('.', 114, 210, bold=True, size=30, font='orbitron'),
    Label('Useful in a pinch.', 157.5, 210, bold=True, size=8, font='orbitron'),
    )
minimenuDrag.opacity = 0

minimenuChargLas = Group(
    Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
    Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
    Label('l.1',113.5, 113, bold=True, size=11, font='orbitron'),
    Label('[Charged Lasers]', 190, 113, bold=True, size=13, font='orbitron'),
    Label('.', 114, 132, bold=True, size=30, font='orbitron'),
    Label('Changes laser speed: 10 > 12.5 whilst', 202.5, 132, bold=True, size=8, font='orbitron'),
    Label('making the lasers be able to go through', 200, 142, bold=True, size=8, font='orbitron'),
    Label('multiple asteroids', 152, 152, bold=True, size=8, font='orbitron'),
    Label('>', 114, 163.5, bold=True, size=15, font='orbitron'),
    Label('Can be upgraded a second time in L.3', 202.5, 163.5, bold=True, size=8, font='orbitron'),
    Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
    Rect(110, 200.875, 180, 1.5),
    Label('.', 114, 210, bold=True, size=30, font='orbitron'),
    Label('I need more speed!!', 165, 210, bold=True, size=8, font='orbitron'),
    )
minimenuChargLas.opacity = 0

minimenuHeat = Group(
    Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
    Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
    Label('l.1',113.5, 113, bold=True, size=11, font='orbitron'),
    Label('[Heatwave]', 170, 113, bold=True, size=13, font='orbitron'),
    Label('.', 114, 132, bold=True, size=30, font='orbitron'),
    Label('Sends out a blast of heat that destroys', 206, 132, bold=True, size=8, font='orbitron'),
    Label('all asteroids hit (excluding blackholes)', 202, 142, bold=True, size=8, font='orbitron'),
    Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
    Rect(110, 200.875, 180, 1.5),
    Label('.', 114, 210, bold=True, size=30, font='orbitron'),
    Label('If a blackhole obstructs you from', 192.5, 210, bold=True, size=8, font='orbitron'),
    Label('asteroids, this might save you.', 187, 220, bold=True, size=8, font='orbitron'),
    )
minimenuHeat.opacity = 0

minimenuPockVac = Group(
    Rect(100, 100, 200, 150, fill='paleGoldenRod', border='gold', borderWidth=5),
    Circle(113.75, 113, 10, fill=None, border='black', borderWidth=2),
    Label('l.1',113.5, 113, bold=True, size=11, font='orbitron'),
    Label('[Pocket Vaccum]', 189, 113, bold=True, size=13, font='orbitron'),
    Label('.', 114, 132, bold=True, size=30, font='orbitron'),
    Label('Sends out a mini vaccum that sucks in', 206, 132, bold=True, size=8, font='orbitron'),
    Label('all asteroids in vicinty', 170, 142, bold=True, size=8, font='orbitron'),
    Label('>', 114, 157.5, bold=True, size=15, font='orbitron'),
    Label('Lasts for 10 seconds, then dissipates', 205, 157.5, bold=True, size=8, font='orbitron'),
    Label('Tips', 200, 190, bold=True, size=13, font='orbitron'),
    Rect(110, 200.875, 180, 1.5),
    Label('.', 114, 210, bold=True, size=30, font='orbitron'),
    Label('BREAK TIME!!! ', 153.5, 210, bold=True, size=8, font='orbitron'),
    )
minimenuPockVac.opacity = 0

#ingame menu

f = ['black' if i%2 == 0 else 'black' for i in range(15)]

amount = Label('[0]', 200, 57.5, fill='white', bold=True, size=13, font='orbitron')
hwicon = Group(
    Rect(176.5, 27.5, 45, 15, fill=gradient('orange', 'orange', 'red', 'red')),
    Rect(171, 24.5, 55, 22, fill='orange', opacity=45)
    )
pvicon = Group(
    Circle(319, 309, 13.25, fill=gradient('red', 'lightCoral'),border='white'),
    Line(338, 300, 300, 316, fill='white'),
    Line(298, 297, 339, 313, fill='white')
    )
pvicon.centerX,pvicon.centerY = 198.5,35.5
equiped = Label('', 67, 370, fill='white', bold=True, size=13, font='orbitron')
cost = Label('Cost: [0]', 36.75, 387.5, fill='white', bold=True, size=13, font='orbitron')
cdtimer = Label(0, 360, 15, fill='white', bold=True, size=13, font='orbitron')
ingamemenu = Group(
    Polygon(70, 40, 115, 18, 103, 40, 115, 62, fill=None, border='white', borderWidth=3),
    Label('[Q]', 93, 70, fill='white', bold=True, size=15, font='orbitron'),
    Polygon(330, 40, 285, 18, 297, 40, 285, 62, fill=None, border='white', borderWidth=3),
    Label('[E]', 307, 70, fill='white', bold=True, size=15, font='orbitron'),
    hwicon,
    pvicon,
    amount,
    cdtimer,
    Label('Equipped:', 38.5, 372.5, fill='white', bold=True, size=13, font='orbitron'),
    equiped,
    cost,
    )
    

ingamemenu.visible = False

if ingamemenu.visible == True:
    pvicon.centerX = 200
    pvicon.centerY = 37
    hwicon.centerX = 200
    hwicon.centerY = 37
#===========================

def firelaser(x,y):
    if not app.charged:
        las = Rect(800, 800, 20, 10,fill='red')
        las.centerX,las.centerY = starship.centerX, starship.centerY
        lasers.add(las)
        las.rotateAngle = angleTo(las.centerX, las.centerY,x,y)-90
        las.shot=True
        las.dx=cos(radians(las.rotateAngle))
        las.dy=sin(radians(las.rotateAngle))
        las.time=50
    else:
        las = Rect(800, 800, 20, 10,fill=gradient('red','orange',start='left'))
        las.centerX,las.centerY = starship.centerX, starship.centerY
        lasers.add(las)
        las.rotateAngle = angleTo(las.centerX, las.centerY,x,y)-90
        las.shot=True
        las.dx=cos(radians(las.rotateAngle))*1.25
        las.dy=sin(radians(las.rotateAngle))*1.25
        las.time=50

#####score values
score = Label(0, 200, 15, fill='white', bold=True, font='orbitron', size=20, borderWidth=1)
score.opacity = 0
app.moonrocks = 0
#####

keey = set()
def onMousePress(mx, my):
    if app.in_menu:
        if (tB1.contains(mx,my) and tB1.opacity != 0):
            app.dif = True
            app.led = False
            app.cred = False
            app.set = False
            app.sho = False
            app.form = False
            mainMenuLabel4.centerY=366
            
        if (tB4.contains(mx,my) and tB4.opacity != 0):
            app.dif = False
            app.led = True
            app.cred = False
            app.set = False
            app.sho = False
            app.form = False
            mainMenuLabel4.centerY=366
        if (tB3.contains(mx, my) and tB3.opacity != 0):
            app.dif = False
            app.led = False
            app.cred = True
            app.set = False
            app.sho = False
            app.form = False
            mainMenuLabel4.centerY=366
        if (tB2.contains(mx,my) and tB2.opacity != 0):
            app.dif = False
            app.led = False
            app.cred = False
            app.set = True
            app.sho = False
            app.form = False
            mainMenuLabel4.centerY=366
        if (tB5.contains(mx,my) and tB5.opacity != 0):
            app.dif = False
            app.led = False
            app.cred = False
            app.set = False
            app.sho = True
            app.form = False
            mainMenuLabel4.centerY=366
        if (tB6.contains(mx,my) and tB6.opacity != 0):
            app.dif = False
            app.led = False
            app.cred = False
            app.set = False
            app.sho = False
            app.form = True
            mainMenuLabel4.centerY=366
        if app.dif:
            if d1.hits(mx,my) and d1.opacity != 0:
                app.comet_chance = 20
                app.rapid_chance = 25
                app.star_chance =  30
                app.alien_spaceship_chance = 475000000000000000000000
                app.min_spawn_rate = 12  #Default minspawnrate 12                              
                app.asteroid_speed = -2 #default speed 2
                app.bh_chance = 100
                bossasteroidModel.health = randrange(10,20)
                app.in_menu=False
            if d2.hits(mx,my) and d2.opacity != 0:
                app.laser_speed = 10             
                app.asteroid_speed = -3      
                app.player_health = 100            
                app.boss_min_points = 100
                app.min_spawn_rate = 10
                app.comet_chance = 10
                app.rapid_chance = 20
                app.rapid_speed_multiplier = 2.3
                app.star_chance = 15
                app.bh_chance = 50
                app.alien_spaceship_chance = 30
                bossasteroidModel.health = randrange(32,100)
                app.in_menu = False
            if d3.hits(mx,my) and d3.opacity != 0:
                app.comet_chance = 4
                app.rapid_chance = 4
                app.star_chance = 4
                app.min_spawn_rate = 5   #default minspawnrate 5
                app.asteroid_speed = -4.5
                app.bh_chance = 35
                app.alien_spaceship_chance = 15
                bossasteroidModel.health = randrange(100,1000)
                app.in_menu = False
        if app.led:
            if lButton2.hits(mx,my) and lButton2.opacity != 0:
                app.ledstep += 1
                if app.ledstep > 2:
                    app.ledstep = 2
                if app.ledstep < 0:
                    app.ledstep = 0
            if lButton1.hits(mx,my) and lButton1.opacity != 0:
                app.ledstep -= 1
                if app.ledstep > 2:
                    app.ledstep = 2
                if app.ledstep < 0:
                    app.ledstep = 0
        if app.sho:
            if Frame1.hits(mx,my) and Frame1.opacity != 0:
                if app.moonrocks < 100:
                    InsufficientFunds.opacity = 100
                elif not app.drag:
                    Purchased.opacity = 100
                    app.moonrocks -= 100
                    app.drag = True
            if Frame2.hits(mx,my) and Frame2.opacity != 0:
                if app.moonrocks < 150:
                    InsufficientFunds.opacity = 100
                elif not app.charged:
                    Purchased.opacity = 100
                    app.moonrocks -= 150
                    app.charged = True
            if Frame3.hits(mx,my) and Frame3.opacity != 0:
                if app.moonrocks < 20:
                    InsufficientFunds.opacity = 100
                else:
                    Purchased.opacity = 100
                    app.moonrocks -= 20
                    app.heat +=1
            if Frame4.hits(mx,my) and Frame4.opacity != 0:
                if app.moonrocks < 30:
                    InsufficientFunds.opacity = 100
                else:
                    Purchased.opacity = 100
                    app.moonrocks -= 30
                    app.poctvacc += 1
        if app.set:
            if sfx.hits(mx,my) and sfx.opacity != 0:
                if sfxLabel.value=='Off':
                    sfxLabel.value='On'
                    sfxButton.border='lime'
                    app.sfxtog = True
                elif sfxLabel.value=='On':
                    sfxLabel.value='Off'
                    sfxButton.border='red'
                    app.sfxtog = False
            if ldm.hits(mx,my) and ldm.opacity != 0:
                if ldmLabel.value=='Off':
                    ldmLabel.value='On'
                    ldmButton.border='lime'
                    app.ldmtog = True
                elif ldmLabel.value=='On':
                    ldmLabel.value='Off'
                    ldmButton.border='red'
                    app.ldmtog = False
            if mm.hits(mx,my) and mm.opacity != 0:
                if mmLabel.value=='Off':
                    mmLabel.value='On'
                    mmButton.border='lime'
                    app.mmtog = True
                elif mmLabel.value=='On':
                    mmLabel.value='Off'
                    mmButton.border='red'
                    app.mmtog = False
        if mmBackButtonB.hits(mx,my) and mmBackButtonB.opacity != 0:
            if app.dif or app.led or app.cred or app.set or app.sho or app.form:
                mainMenuLabel2.value = random.choice(splashtexts)
                mainMenuLabel4.centerY=366
                heatWaveModel2.opacity=0
            app.dif = False
            app.led = False
            app.cred = False
            app.set = False
            app.sho = False
            app.form = False
                
    if app.lost:
        if mmLoseLabelB.hits(mx,my) and mmLoseLabelB.opacity != 0:
            app.in_menu = True
            app.lost = False
            score.opacity=0
            ingamemenu.visible = False
            mainMenuLabel3.opacity=100
            flavorText1.opacity=0
            mainMenuLabel2.value = random.choice(splashtexts)
            
            
    if not app.in_menu:
        mmBackButtonB.opacity = 0
        if ingamemenu.contains(mx,my) and ingamemenu.visible:
            pass
        else:
            firelaser(mx, my)
            

ogtb1 = [tb1frame.left,tb1frame.top,tb1frame.width,tb1frame.height,tb1frame.border]
ogtb2 = [tb2frame.left,tb2frame.top,tb2frame.width,tb2frame.height,tb2frame.border]
ogtb3 = [tb3frame.left,tb3frame.top,tb3frame.width,tb3frame.height,tb3frame.border]
ogtb4 = [tb4frame.left,tb4frame.top,tb4frame.width,tb4frame.height,tb4frame.border]
ogtb5 = [tb5frame.left,tb5frame.top,tb5frame.width,tb5frame.height,tb5frame.border]
ogtb6 = [tb6frame.left,tb6frame.top,tb6frame.width,tb6frame.height,tb6frame.border]

ogd1 = [d1frame.left,d1frame.top,d1frame.width,d1frame.height]
ogd2 = [d2frame.left,d2frame.top,d2frame.width,d2frame.height]
ogd3 = [d3frame.left,d3frame.top,d3frame.width,d3frame.height]

ogbtmm = [mmllb.left,mmllb.top,mmllb.width,mmllb.height]

app.tb1sel = False
app.tb2sel = False
app.tb3sel = False
app.tb4sel = False
app.tb5sel = False
app.tb6sel = False
app.lb1 = False
app.lb2 = False
app.ssfx = False
app.sldm = False
app.smm = False
app.smmbbb = False
app.d1 = False
app.d2 = False
app.d3 = False
app.f1 = False
app.f2 = False
app.f3 = False
app.f4 = False
app.btmm = False

app.keybinds = ['enter','q','e','space','backspace','w','s']

def onMouseMove(mx, my):
    m.centerX,m.centerY = mx,my
    if not app.in_menu:
        cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 0,0,0,0
def onMouseDrag(x,y):
    if not app.in_menu:
        m.centerX,m.centerY = x,y
    if app.drag:
        firelaser(x,y)
def onKeyHold(k):
    if app.drag and app.keybinds[0] in k:
        firelaser(m.centerX,m.centerY)
def onKeyPress(key):
    if not app.in_menu:
        keey.add(key)
        if key == app.keybinds[0]:
            firelaser(m.centerX,m.centerY)
        if key == app.keybinds[1]:
            app.selit = max(0,app.selit-1)
        if key == app.keybinds[2]:
            app.selit = min(len(pows)-1,app.selit+1)
        if key == app.keybinds[3]:
            if pows[app.selit] == 'heatwave' and app.heat > 0 and not app.heatcd:
                app.heat-=1
                hw = Group(
                    Rect(200,200,40,300,fill='orange',opacity = 45),
                    Rect(205,205,30,290,fill=gradient('orange','orange','red','red'))
                    )
                hw.centerX,hw.centerY = starship.centerX+50,starship.centerY
                heatwaves.add(hw)
                app.heatcd = True
            if pows[app.selit] == 'pocket vaccum' and app.poctvacc > 0 and not app.pctcd:
                app.poctvacc -= 1
                spritePockVac = Group(
                    Circle(319, 309, 13.25, fill=gradient('red', 'lightCoral'),border='white'),
                    Line(338, 300, 300, 316, fill='white'),
                    Line(298, 297, 339, 313, fill='white')
                    )
                spritePockVac.dx = cos(radians(starship.rotateAngle))
                spritePockVac.dy = sin(radians(starship.rotateAngle))
                spritePockVac.speed = 2
                spritePockVac.centerX,spritePockVac.centerY = starship.centerX+spritePockVac.dx*5,starship.centerY+spritePockVac.dy*5
                pctvcm.add(spritePockVac)
                app.pctcd = True
                print('pct')
            
    else:
        if key == app.keybinds[4]:
            if app.dif or app.led or app.cred or app.set or app.sho or app.form:
                mainMenuLabel2.value = random.choice(splashtexts)
                mainMenuLabel4.centerY=366
                heatWaveModel2.opacity=0
            app.dif = False
            app.led = False
            app.cred = False
            app.set = False
            app.sho = False
            app.form = False
def onKeyRelease(key):
    if not app.in_menu:
        keey.remove(key)
    
# asteroids.centerX = 425
    

app.wait = 0
app.waittime = 60
app.waite = 0
app.waitelime = 10

def bhf(g,i):
    for b in blackhole:
        if i.hitsShape(b):
            g.remove(i)
            b.radius += 1

if wip:
    print('WARNING: update is in progress, bugs may arise, please be patient. thank you!')
    wipwarn.opacity = 100
else:
    w.opacity = 0
    wipwarn.opacity = 0

offset = 4
speed = 2
color = gradient(rgb(0,255,0), rgb(0,100,0),rgb(0,100,0))

def onStep():
    if wip:
        w.toFront()
        wipwarn.toFront()
    else:
        w.opacity = 0
        wipwarn.opacity = 0
    if app.in_menu:
        if wip:
            wipwarn.opacity = 100
        explosions.clear()
        lasers.clear()
        asteroids.clear()
        comettrail.clear()
        comets.clear()
        rapidtrail.clear()
        rapid.clear()
        blackhole.clear()
        sstrail.clear()
        shootingstar.clear()
        alienSP.clear()
        heatwaves.clear()
        alienbeam = []
        menuStars.opacity = 100
        ingamemenu.visible = False
        
        outset = 0
        if not app.tb1sel and not app.tb2sel and not app.tb3sel and not app.tb4sel and not app.tb5sel and not app.tb6sel and not app.lb1 and not app.lb2 and not app.ssfx and not app.sldm and not app.smm and not app.d1 and not app.d2 and not app.d3 and not app.f1 and not app.f2 and not app.f3 and not app.f4 and not app.btmm and not app.smmbbb:
            cornerEffect1.centerX,cornerEffect1.centerY = m.centerX-5,m.centerY-5
            cornerEffect2.centerX,cornerEffect2.centerY = m.centerX+15,m.centerY-5
            cornerEffect3.centerX,cornerEffect3.centerY = m.centerX-5,m.centerY+20
            cornerEffect4.centerX,cornerEffect4.centerY = m.centerX+15,m.centerY+20
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 20,20,20,20
        elif app.tb1sel:
            cornerEffect1.centerX,cornerEffect1.centerY = tb1frame.left-outset,tb1frame.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = tb1frame.left+tb1frame.width+outset,tb1frame.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = tb1frame.left-outset,tb1frame.top+tb1frame.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = tb1frame.left+tb1frame.width+outset,tb1frame.top+tb1frame.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.tb2sel:
            cornerEffect1.centerX,cornerEffect1.centerY = tb2frame.left-outset,tb2frame.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = tb2frame.left+tb2frame.width+outset,tb2frame.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = tb2frame.left-outset,tb2frame.top+tb2frame.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = tb2frame.left+tb2frame.width+outset,tb2frame.top+tb2frame.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.tb3sel:
            cornerEffect1.centerX,cornerEffect1.centerY = tb3frame.left-outset,tb3frame.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = tb3frame.left+tb3frame.width+outset,tb3frame.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = tb3frame.left-outset,tb3frame.top+tb3frame.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = tb3frame.left+tb3frame.width+outset,tb3frame.top+tb3frame.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.tb4sel:
            cornerEffect1.centerX,cornerEffect1.centerY = tb4frame.left-outset,tb4frame.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = tb4frame.left+tb4frame.width+outset,tb4frame.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = tb4frame.left-outset,tb4frame.top+tb4frame.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = tb4frame.left+tb4frame.width+outset,tb4frame.top+tb4frame.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.tb5sel:
            cornerEffect1.centerX,cornerEffect1.centerY = tb5frame.left-outset,tb5frame.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = tb5frame.left+tb5frame.width+outset,tb5frame.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = tb5frame.left-outset,tb5frame.top+tb5frame.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = tb5frame.left+tb5frame.width+outset,tb5frame.top+tb5frame.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.tb6sel:
            cornerEffect1.centerX,cornerEffect1.centerY = tb6frame.left-outset,tb6frame.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = tb6frame.left+tb6frame.width+outset,tb6frame.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = tb6frame.left-outset,tb6frame.top+tb6frame.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = tb6frame.left+tb6frame.width+outset,tb6frame.top+tb6frame.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.lb1:
            cornerEffect1.centerX,cornerEffect1.centerY = lButton1.left-outset,lButton1.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = lButton1.left+lButton1.width+outset,lButton1.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = lButton1.left-outset,lButton1.top+lButton1.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = lButton1.left+lButton1.width+outset,lButton1.top+lButton1.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.lb2:
            cornerEffect1.centerX,cornerEffect1.centerY = lButton2.left-outset,lButton2.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = lButton2.left+lButton2.width+outset,lButton2.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = lButton2.left-outset,lButton2.top+lButton2.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = lButton2.left+lButton2.width+outset,lButton2.top+lButton2.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.ssfx:
            cornerEffect1.centerX,cornerEffect1.centerY = sfxButton.left-outset,sfxButton.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = sfxButton.left+sfxButton.width+outset,sfxButton.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = sfxButton.left-outset,sfxButton.top+sfxButton.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = sfxButton.left+sfxButton.width+outset,sfxButton.top+sfxButton.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.sldm:
            cornerEffect1.centerX,cornerEffect1.centerY = ldmButton.left-outset,ldmButton.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = ldmButton.left+ldmButton.width+outset,ldmButton.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = ldmButton.left-outset,ldmButton.top+ldmButton.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = ldmButton.left+ldmButton.width+outset,ldmButton.top+ldmButton.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.smm:
            cornerEffect1.centerX,cornerEffect1.centerY = mmButton.left-outset,mmButton.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = mmButton.left+mmButton.width+outset,mmButton.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = mmButton.left-outset,mmButton.top+mmButton.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = mmButton.left+mmButton.width+outset,mmButton.top+mmButton.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.smmbbb:
            cornerEffect1.centerX,cornerEffect1.centerY = mmbbb.left-outset,mmbbb.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = mmbbb.left+mmbbb.width+outset,mmbbb.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = mmbbb.left-outset,mmbbb.top+mmbbb.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = mmbbb.left+mmbbb.width+outset,mmbbb.top+mmbbb.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.d1:
            cornerEffect1.centerX,cornerEffect1.centerY = d1.left-outset,d1.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = d1.left+d1.width+outset,d1.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = d1.left-outset,d1.top+d1.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = d1.left+d1.width+outset,d1.top+d1.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.d2:
            cornerEffect1.centerX,cornerEffect1.centerY = d2.left-outset,d2.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = d2.left+d2.width+outset,d2.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = d2.left-outset,d2.top+d2.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = d2.left+d2.width+outset,d2.top+d2.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.d3:
            cornerEffect1.centerX,cornerEffect1.centerY = d3.left-outset,d3.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = d3.left+d3.width+outset,d3.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = d3.left-outset,d3.top+d3.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = d3.left+d3.width+outset,d3.top+d3.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.f1:
            cornerEffect1.centerX,cornerEffect1.centerY = Frame1.left-outset,Frame1.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = Frame1.left+Frame1.width+outset,Frame1.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = Frame1.left-outset,Frame1.top+Frame1.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = Frame1.left+Frame1.width+outset,Frame1.top+Frame1.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.f2:
            cornerEffect1.centerX,cornerEffect1.centerY = Frame2.left-outset,Frame2.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = Frame2.left+Frame2.width+outset,Frame2.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = Frame2.left-outset,Frame2.top+Frame2.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = Frame2.left+Frame2.width+outset,Frame2.top+Frame2.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.f3:
            cornerEffect1.centerX,cornerEffect1.centerY = Frame3.left-outset,Frame3.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = Frame3.left+Frame3.width+outset,Frame3.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = Frame3.left-outset,Frame3.top+Frame3.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = Frame3.left+Frame3.width+outset,Frame3.top+Frame3.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        elif app.f4:
            cornerEffect1.centerX,cornerEffect1.centerY = Frame4.left-outset,Frame4.top-outset
            cornerEffect2.centerX,cornerEffect2.centerY = Frame4.left+Frame4.width+outset,Frame4.top-outset
            cornerEffect3.centerX,cornerEffect3.centerY = Frame4.left-outset,Frame4.top+Frame4.height+outset
            cornerEffect4.centerX,cornerEffect4.centerY = Frame4.left+Frame4.width+outset,Frame4.top+Frame4.height+outset
            cornerEffect1.opacity,cornerEffect2.opacity,cornerEffect3.opacity,cornerEffect4.opacity = 100,100,100,100
        tr = 75
        if (tB1.contains(m.centerX,m.centerY) and tB1.opacity != 0):
            app.tb1sel = True
        else:
            app.tb1sel = False
        
        if (tB2.contains(m.centerX,m.centerY) and tB2.opacity != 0):
            app.tb2sel = True
        else:
            app.tb2sel = False
        
        if (tB3.contains(m.centerX,m.centerY) and tB3.opacity != 0):
            app.tb3sel = True
        else:
            app.tb3sel = False
        
        if (tB4.contains(m.centerX,m.centerY) and tB4.opacity != 0):
            app.tb4sel = True
        else:
            app.tb4sel = False
        
        if (tB5.contains(m.centerX,m.centerY) and tB4.opacity != 0):
            app.tb5sel = True
        else:
            app.tb5sel = False
        
        if (tB6.contains(m.centerX,m.centerY) and tB6.opacity != 0):
            app.tb6sel = True
        else:
            app.tb6sel = False
        
        if lButton1.contains(m.centerX,m.centerY) and lButton1.opacity != 0:
            app.lb1 = True
        else:
            app.lb1 = False
        
        if lButton2.contains(m.centerX,m.centerY) and lButton2.opacity != 0:
            app.lb2 = True
        else:
            app.lb2 = False
        
        if sfxButton.contains(m.centerX,m.centerY) and sfxButton.opacity != 0:
            app.ssfx = True
        else:
            app.ssfx = False
        
        if ldmButton.contains(m.centerX,m.centerY) and ldmButton.opacity != 0:
            app.sldm = True
        else:
            app.sldm = False
        if mmButton.contains(m.centerX,m.centerY) and mmButton.opacity !=0:
            app.smm = True
        else:
            app.smm = False
        if mmbbb.contains(m.centerX,m.centerY) and mmbbb.opacity !=0:
            app.smmbbb = True
        else:
            app.smmbbb = False
        if d1.contains(m.centerX,m.centerY) and d1.opacity != 0:
            app.d1 = True
        else:
            app.d1 = False
        
        if d2.contains(m.centerX,m.centerY) and d2.opacity != 0:
            app.d2 = True
        else:
            app.d2 = False
        
        if d3.contains(m.centerX,m.centerY) and d3.opacity != 0:
            app.d3 = True
        else:
            app.d3 = False
        
        if Frame1.contains(m.centerX,m.centerY) and Frame1.opacity != 0:
            app.f1 = True
            minimenuDrag.opacity = tr
            minimenuDrag.left,minimenuDrag.top = m.centerX,m.centerY
        else:
            app.f1 = False
            minimenuDrag.opacity = 0
        
        if Frame2.contains(m.centerX,m.centerY) and Frame2.opacity != 0:
            app.f2 = True
            minimenuChargLas.opacity = tr
            minimenuChargLas.left,minimenuChargLas.top = m.centerX,m.centerY-minimenuChargLas.height
        else:
            app.f2 = False
            minimenuChargLas.opacity = 0
        
        if Frame3.contains(m.centerX,m.centerY) and Frame3.opacity != 0:
            app.f3 = True
            minimenuHeat.opacity = tr
            minimenuHeat.left,minimenuHeat.top = m.centerX-minimenuHeat.width,m.centerY
        else:
            app.f3 = False
            minimenuHeat.opacity = 0
        
        if Frame4.contains(m.centerX,m.centerY) and Frame4.opacity != 0:
            app.f4 = True
            minimenuPockVac.opacity = tr
            minimenuPockVac.left,minimenuPockVac.top = m.centerX-minimenuPockVac.width,m.centerY-minimenuPockVac.height
        else:
            app.f4 = False
            minimenuPockVac.opacity = 0

        bgStars.opacity = 0
        if app.count > 6:
            app.rotateflag = not app.rotateflag
            app.count=0
        if not app.rotateflag:
            mainMenuLabel.rotateAngle+=0.2
            mainMenuLabel2.rotateAngle+=0.2
            dLabel.rotateAngle+=0.2
            lL1.rotateAngle+=0.2
            lL2.rotateAngle+=0.2
            lL3.rotateAngle+=0.2
            cLabel.rotateAngle+=0.2
            sLabel.rotateAngle+=0.2
            pwlabel.rotateAngle+=0.2
            shopL.rotateAngle+=0.2
        else:
            mainMenuLabel.rotateAngle-=0.2
            mainMenuLabel2.rotateAngle-=0.2
            dLabel.rotateAngle-=0.2
            lL1.rotateAngle-=0.2
            lL2.rotateAngle-=0.2
            lL3.rotateAngle-=0.2
            cLabel.rotateAngle-=0.2
            sLabel.rotateAngle-=0.2
            pwlabel.rotateAngle-=0.2
            shopL.rotateAngle-=0.2
        app.count+=0.1
        for i in menuStars:
            if not app.in_menu:
                break
            i.centerX-=1
            if i.centerX < 0:
                i.centerX=400
                i.centerY=randrange(0, 400)
        for i in astModel:
            if not app.in_menu:
                break
            i.centerX-=2.3
            i.rotateAngle+=90
            if i.centerX < -50:
                i.centerX = 430
                i.centerY = randrange(40, 360)
        for i in rapidTrailModel:
            if not app.in_menu:
                break
            i.centerX-=0.65
            i.time-=1
            if i.opacity > 1:
                i.opacity-=1
                i.radius-=0.2
            
            if i.opacity < 2:
                i.opacity = 50
            if i.time < 0:
                rapidTrailModel.remove(i)
        for i in rapdModel:
            if not app.in_menu:
                break
            i.centerX-=5.29               #5.29
            i.rotateAngle+=90
            if i.centerX < -50:
                i.centerX = 430
                i.centerY = randrange(40, 360)
            t = Circle(i.centerX, i.centerY, 15, fill='grey', opacity=50)
            t.time=15
            rapidTrailModel.add(t)
        if app.dif:
            mainMenuLabel.opacity=0
            mainMenuLabel2.opacity=0
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=0
            tB2.opacity=0
            tB3.opacity=0
            tB4.opacity=0
            tB5.opacity=0
            tB6.opacity=0
            dLabel.opacity=100
            d1.opacity=100
            d2.opacity=100
            d3.opacity=100
            if app.mmtog:
                mmBackButtonB.opacity=100
                mmBackButtonB.centerX = 200
                mmBackButtonB.centerY = 325
                mainMenuLabel4.opacity=0
            if app.d1:
                if not d1frame.width >= ogd1[2]+offset*2:
                    d1frame.width += speed
                if not d1frame.height >= ogd1[3]+offset*2:
                    d1frame.height += speed
                if not d1frame.left <= ogd1[0]-offset:
                    d1frame.left -= speed
                if not d1frame.top <= ogd1[1]-offset:
                    d1frame.top -= speed
            else:
                if not d1frame.width <= ogd1[2]:
                    d1frame.width -= speed
                if not d1frame.height <= ogd1[3]:
                    d1frame.height -= speed
                if not d1frame.left >= ogd1[0]:
                    d1frame.left += speed
                if not d1frame.top >= ogd1[1]:
                    d1frame.top += speed
            
            if app.d2:
                if not d2frame.width >= ogd2[2]+offset*2:
                    d2frame.width += speed
                if not d2frame.height >= ogd2[3]+offset*2:
                    d2frame.height += speed
                if not d2frame.left <= ogd2[0]-offset:
                    d2frame.left -= speed
                if not d2frame.top <= ogd2[1]-offset:
                    d2frame.top -= speed
            else:
                if not d2frame.width <= ogd2[2]:
                    d2frame.width -= speed
                if not d2frame.height <= ogd2[3]:
                    d2frame.height -= speed
                if not d2frame.left >= ogd2[0]:
                    d2frame.left += speed
                if not d2frame.top >= ogd2[1]:
                    d2frame.top += speed
            
            if app.d3:
                if not d3frame.width >= ogd3[2]+offset*2:
                    d3frame.width += speed
                if not d3frame.height >= ogd3[3]+offset*2:
                    d3frame.height += speed
                if not d3frame.left <= ogd3[0]-offset:
                    d3frame.left -= speed
                if not d3frame.top <= ogd3[1]-offset:
                    d3frame.top -= speed
            else:
                if not d3frame.width <= ogd3[2]:
                    d3frame.width -= speed
                if not d3frame.height <= ogd3[3]:
                    d3frame.height -= speed
                if not d3frame.left >= ogd3[0]:
                    d3frame.left += speed
                if not d3frame.top >= ogd3[1]:
                    d3frame.top += speed
            
        
        if app.led:
            mainMenuLabel.opacity=0
            mainMenuLabel2.opacity=0
            mainMenuLabel4.opacity=0
            mainMenuLabel3.opacity=0
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=0
            tB2.opacity=0
            tB3.opacity=0
            tB4.opacity=0
            tB5.opacity=0
            tB6.opacity=0
            lL1.opacity=100
            lL2.opacity=100
            lL3.opacity=100
            leds.opacity = 100
            lButton2.opacity,lBoardAT.opacity,lBoardAt2.opacity = 100,100,100
            lButton1.opacity = 100
            
            targets = {0:e,1:n,2:h}
            target_x = targets[app.ledstep]
            
            if leds.centerX < target_x:
                leds.dx += 1
            elif leds.centerX > target_x:
                leds.dx -= 1
            else:
                leds.dx = 0
            
            leds.centerX += leds.dx
            
            if abs(leds.centerX - target_x) <= abs(leds.dx):
                leds.centerX = target_x
                leds.dx = 0
            if app.mmtog:
                lL1.centerY = 25
                lL2.centerY = 25
                lL3.centerY = 25
                mmBackButtonB.opacity=100
                mmBackButtonB.centerX = 200
                mmBackButtonB.centerY = 60
            else:
                lL1.centerY = 50
                lL2.centerY = 50
                lL3.centerY = 50
                
            # print(f"step: {app.ledstep} | pos: {leds.centerX} | target: {target_x} | dx: {leds.dx}")
        if app.cred:
            mainMenuLabel.opacity=0
            mainMenuLabel2.opacity=0
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=0
            tB2.opacity=0
            tB3.opacity=0
            tB4.opacity=0
            tB5.opacity=0
            tB6.opacity=0
            cLabel.opacity=100
            Credits1.opacity=100
            Credits2.opacity=100
            Credits3.opacity=100
            Credits4.opacity=100
            if app.mmtog:
                mmBackButtonB.opacity=100
                mmBackButtonB.centerX = 200
                mmBackButtonB.centerY = 325
        if app.set:
            mainMenuLabel.opacity=0
            mainMenuLabel2.opacity=0
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=0
            tB2.opacity=0
            tB3.opacity=0
            tB4.opacity=0
            tB5.opacity=0
            tB6.opacity=0
            sfx.opacity=100
            sLabel.opacity = 100
            ldm.opacity=100
            mm.opacity=100
            if app.mmtog:
                mmBackButtonB.opacity = 100
                mmBackButtonB.centerX = 300
                mmBackButtonB.centerY = 350
                mainMenuLabel4.opacity=0
            else:
                mmBackButtonB.opacity = 0
                mainMenuLabel4.opacity=100
            keybds.opacity=100
        if app.sho:
            if InsufficientFunds.opacity != 0:
                app.curnoti -= 1
                if app.curnoti < 0:
                    InsufficientFunds.opacity = 0
                    app.curnoti = buyupnoti
            if Purchased.opacity != 0:
                app.curnoti -= 1
                if app.curnoti < 0:
                    Purchased.opacity = 0
                    app.curnoti = buyupnoti
            mainMenuLabel.opacity=0
            mainMenuLabel2.opacity=0
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=0
            tB2.opacity=0
            tB3.opacity=0
            tB4.opacity=0
            tB5.opacity=0
            tB6.opacity=0
            powerUpMenu.opacity = 100
            astModelDeco.opacity = 100
            lasModels.opacity = 100
            superChargedlasModels.opacity = 100
            heatWaveModel.opacity = 100
            heatWaveModel2.opacity=45
            pocketVaccumModel.opacity = 100
            pocketVaccumModel2.opacity = 100
            pocketVaccumModel3.opacity = 100
            pocketVaccumModel.opacity=70
            pocketVaccumModel2.centerX = 298
            pocketVaccumModel2.centerY = 315
            pocketVaccumModel2.rotateAngle= -20
            pocketVaccumModel3.centerX = 334
            pocketVaccumModel3.centerY = 315
            pocketVaccumModel3.rotateAngle= 15
            moonRocksCount.centerX = 200
            moonRocksCount.centerY = 128
            mRLabel.centerY = 124
            mRLabel.centerX = 201
            mRAmount.centerY = 140
            mRAmount.centerX = 201
            mRAmount.value = app.moonrocks
            starShipModel.rotateAngle=-20
            starShipModel.centerX=55
            starShipModel.centerY = 140
            starShipModel.opacity=100
            powerupsLabel.opacity=100
            upgradesLabel.opacity=100
            shelf1.opacity = 100
            shelf2.opacity = 100
            shelf3.opacity = 100
            shelf4.opacity = 100
            shelf5.opacity = 100
            shelf6.opacity = 100
            moonRocksCount.opacity = 100
            mRLabel.opacity = 100
            mRAmount.opacity = 100
            Frame1.opacity = 100
            Frame2.opacity = 100
            Frame3.opacity = 100
            Frame4.opacity = 100
            flag.opacity = 100
            pwlabel.opacity = 100
            shopL.opacity = 100
            if app.mmtog:
                mainMenuLabel4.opacity=0
                mmBackButtonB.opacity=100
                mmBackButtonB.centerX = 85
                mmBackButtonB.centerY = 50

        if app.form:
            mainMenuLabel.opacity=0
            mainMenuLabel2.opacity=0
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=0
            tB2.opacity=0
            tB3.opacity=0
            tB4.opacity=0
            tB5.opacity=0
            tB6.opacity=0
            formLab.opacity = 100
            if app.mmtog:
                mmBackButtonB.opacity=100
                mmBackButtonB.centerX = 200
                mmBackButtonB.centerY = 325
        
        if not app.cred and not app.dif and not app.led and not app.set and not app.sho and not app.form:
            mainMenuLabel.opacity=100
            mainMenuLabel2.opacity=100
            mainMenuLabel3.opacity=100
            mainMenuLabel4.opacity = 100
            astModel.opacity=100
            rapdModel.opacity=100
            rapidTrailModel.opacity=20
            tB1.opacity=100
            tB2.opacity=100
            tB3.opacity=100
            tB4.opacity=100
            tB5.opacity=100
            tB6.opacity=100
            dLabel.opacity=0
            d1.opacity=0
            d2.opacity=0
            d3.opacity=0
            lL1.opacity = 0
            lL2.opacity = 0
            lL3.opacity = 0
            leds.opacity = 0
            lButton2.opacity,lBoardAT.opacity,lBoardAt2.opacity = 0,0,0
            lButton1.opacity = 0
            cLabel.opacity=0
            Credits1.opacity=0
            Credits2.opacity=0
            sLabel.opacity=0
            sfx.opacity=0
            ldm.opacity = 0
            mm.opacity = 0
            keybds.opacity=0
            Credits3.opacity = 0
            Credits4.opacity = 0
            formLab.opacity = 0
            powerUpMenu.opacity = 0
            Purchased.opacity = 0
            InsufficientFunds.opacity = 0
            astModelDeco.opacity = 0
            lasModels.opacity = 0
            superChargedlasModels.opacity = 0
            heatWaveModel.opacity = 0
            heatWaveModel2.opacity=0
            pocketVaccumModel.opacity = 0
            pocketVaccumModel2.opacity = 0
            pocketVaccumModel3.opacity = 0
            starShipModel.opacity = 0
            upgradesLabel.opacity = 0
            powerupsLabel.opacity = 0
            shelf1.opacity = 0
            shelf2.opacity = 0
            shelf3.opacity = 0
            shelf4.opacity = 0
            shelf5.opacity = 0
            shelf6.opacity = 0
            moonRocksCount.opacity = 0
            mRLabel.opacity = 0
            mRAmount.opacity = 0
            Frame1.opacity = 0
            Frame2.opacity = 0
            Frame3.opacity = 0
            Frame4.opacity = 0
            flag.opacity = 0
            pwlabel.opacity = 0
            shopL.opacity = 0
            mmBackButtonB.opacity=0
            if app.mmtog:
                mainMenuLabel4.opacity=0
            if app.tb1sel:
                if not tb1frame.width >= ogtb1[2]+offset*2:
                    tb1frame.width += speed
                if not tb1frame.height >= ogtb1[3]+offset*2:
                    tb1frame.height += speed
                if not tb1frame.left <= ogtb1[0]-offset:
                    tb1frame.left -= speed
                if not tb1frame.top <= ogtb1[1]-offset:
                    tb1frame.top -= speed
                tb1frame.border = gradient('lime', 'chartreuse', 'green')
            else:
                if not tb1frame.width <= ogtb1[2]:
                    tb1frame.width -= speed
                if not tb1frame.height <= ogtb1[3]:
                    tb1frame.height -= speed
                if not tb1frame.left >= ogtb1[0]:
                    tb1frame.left += speed
                if not tb1frame.top >= ogtb1[1]:
                    tb1frame.top += speed
                tb1frame.border = ogtb1[4]
            
            if app.tb2sel:
                if not tb2frame.width >= ogtb2[2]+offset*2:
                    tb2frame.width += speed
                if not tb2frame.height >= ogtb2[3]+offset*2:
                    tb2frame.height += speed
                if not tb2frame.left <= ogtb2[0]-offset:
                    tb2frame.left -= speed
                if not tb2frame.top <= ogtb2[1]-offset:
                    tb2frame.top -= speed
                tb2frame.border = gradient('blue', 'midnightBlue')
            else:
                if not tb2frame.width <= ogtb2[2]:
                    tb2frame.width -= speed
                if not tb2frame.height <= ogtb2[3]:
                    tb2frame.height -= speed
                if not tb2frame.left >= ogtb2[0]:
                    tb2frame.left += speed
                if not tb2frame.top >= ogtb2[1]:
                    tb2frame.top += speed
                tb2frame.border = ogtb2[4]
            
            if app.tb3sel:
                if not tb3frame.width >= ogtb3[2]+offset*2:
                    tb3frame.width += speed
                if not tb3frame.height >= ogtb3[3]+offset*2:
                    tb3frame.height += speed
                if not tb3frame.left <= ogtb3[0]-offset:
                    tb3frame.left -= speed
                if not tb3frame.top <= ogtb3[1]-offset:
                    tb3frame.top -= speed
                tb3frame.border = color
            else:
                if not tb3frame.width <= ogtb3[2]:
                    tb3frame.width -= speed
                if not tb3frame.height <= ogtb3[3]:
                    tb3frame.height -= speed
                if not tb3frame.left >= ogtb3[0]:
                    tb3frame.left += speed
                if not tb3frame.top >= ogtb3[1]:
                    tb3frame.top += speed
                tb3frame.border = ogtb3[4]
            
            if app.tb4sel:
                if not tb4frame.width >= ogtb4[2]+offset*2:
                    tb4frame.width += speed
                if not tb4frame.height >= ogtb4[3]+offset*2:
                    tb4frame.height += speed
                if not tb4frame.left <= ogtb4[0]-offset:
                    tb4frame.left -= speed
                if not tb4frame.top <= ogtb4[1]-offset:
                    tb4frame.top -= speed
                tb4frame.border = gradient('gold', 'yellow')
            else:
                if not tb4frame.width <= ogtb4[2]:
                    tb4frame.width -= speed
                if not tb4frame.height <= ogtb4[3]:
                    tb4frame.height -= speed
                if not tb4frame.left >= ogtb4[0]:
                    tb4frame.left += speed
                if not tb4frame.top >= ogtb4[1]:
                    tb4frame.top += speed
                tb4frame.border = ogtb4[4]
            
            if app.tb5sel:
                if not tb5frame.width >= ogtb5[2]+offset*2:
                    tb5frame.width += speed
                if not tb5frame.height >= ogtb5[3]+offset*2:
                    tb5frame.height += speed
                if not tb5frame.left <= ogtb5[0]-offset:
                    tb5frame.left -= speed
                if not tb5frame.top <= ogtb5[1]-offset:
                    tb5frame.top -= speed
                tb5frame.border = gradient('orange','darkOrange','orange')
            else:
                if not tb5frame.width <= ogtb5[2]:
                    tb5frame.width -= speed
                if not tb5frame.height <= ogtb5[3]:
                    tb5frame.height -= speed
                if not tb5frame.left >= ogtb5[0]:
                    tb5frame.left += speed
                if not tb5frame.top >= ogtb5[1]:
                    tb5frame.top += speed
                tb5frame.border = ogtb5[4]
            
            if app.tb6sel:
                if not tb6frame.width >= ogtb6[2]+offset*2:
                    tb6frame.width += speed
                if not tb6frame.height >= ogtb6[3]+offset*2:
                    tb6frame.height += speed
                if not tb6frame.left <= ogtb6[0]-offset:
                    tb6frame.left -= speed
                if not tb6frame.top <= ogtb6[1]-offset:
                    tb6frame.top -= speed
                tb6frame.border = color
            else:
                if not tb6frame.width <= ogtb6[2]:
                    tb6frame.width -= speed
                if not tb6frame.height <= ogtb6[3]:
                    tb6frame.height -= speed
                if not tb6frame.left >= ogtb6[0]:
                    tb6frame.left += speed
                if not tb6frame.top >= ogtb6[1]:
                    tb6frame.top += speed
                tb6frame.border = ogtb6[4]
        if not app.lost:
            youLoseScreen.visible=False
            youLoseScreen.toBack()
            youLoseLabel2.toBack()
            youLoseLabel3.toBack()
            youLoseLabel2.opacity=0
            youLoseLabel3.opacity=0
            mmLoseLabelB.opacity=0
            bgStars.toBack()
            mmLoseLabelB.toBack()
            currencyEarned.toBack()
            currencyEarned.opacity=0
            currencyEarnedAmt.toBack()
            currencyEarnedAmt.opacity=0
    elif not app.lost:
        wipwarn.opacity = 0
        mainMenuLabel.opacity=0
        mainMenuLabel2.opacity=0
        astModel.opacity=0
        rapdModel.opacity=0
        rapidTrailModel.opacity=0
        tB1.opacity=0
        tB2.opacity=0
        tB3.opacity=0
        tB4.opacity=0
        dLabel.opacity=0
        d1.opacity=0
        d2.opacity=0
        d3.opacity=0
        lL1.opacity = 0
        lL2.opacity = 0
        lL3.opacity = 0
        leds.opacity = 0
        lButton2.opacity,lBoardAT.opacity,lBoardAt2.opacity = 0,0,0
        lButton1.opacity = 0
        cLabel.opacity=0
        Credits1.opacity=0
        Credits2.opacity=0
        Credits3.opacity=0
        Credits4.opacity=0
        sLabel.opacity=0
        sfx.opacity=0
        ldm.opacity = 0
        mm.opacity=0
        keybds.opacity=0
        formLab.opacity = 0
        powerUpMenu.opacity = 0
        Purchased.opacity = 0
        InsufficientFunds.opacity = 0
        astModelDeco.opacity = 0
        lasModels.opacity = 0
        superChargedlasModels.opacity = 0
        heatWaveModel.opacity = 0
        
        pocketVaccumModel.opacity = 0
        pocketVaccumModel2.opacity = 0
        pocketVaccumModel3.opacity = 0
        starShipModel.opacity = 0
        upgradesLabel.opacity = 0
        powerupsLabel.opacity = 0
        shelf1.opacity = 0
        shelf2.opacity = 0
        shelf3.opacity = 0
        shelf4.opacity = 0
        shelf5.opacity = 0
        shelf6.opacity = 0
        moonRocksCount.opacity = 0
        mRLabel.opacity = 0
        mRAmount.opacity = 0
        Frame1.opacity = 0
        Frame2.opacity = 0
        Frame3.opacity = 0
        Frame4.opacity = 0
        flag.opacity = 0
        pwlabel.opacity = 0
        shopL.opacity = 0
        mainMenuLabel.opacity = 0
        mainMenuLabel2.opacity = 0
        mainMenuLabel3.opacity = 0
        mainMenuLabel4.opacity = 0
        menuBackground.opacity = 0
        menuStars.opacity = 0
        #alienShipP1.opacity=100
        #alienShipP2.opacity=100
        #alienShipP3.opacity=100
        #alienShipP4.opacity=100
        #laserGun.opacity=100
        #alienShipP2.toBack()
        #laserGun.rotateAngle+=2
        
        menuBackground.opacity = 0
        
        starship.opacity = 100
        bgStars.opacity = 100
        
        if not app.lost:
            youLoseScreen.visible=False
            youLoseScreen.toBack()
            youLoseLabel2.toBack()
            youLoseLabel3.toBack()
            youLoseLabel2.opacity=0
            youLoseLabel3.opacity=0
            mmLoseLabelB.opacity=0
            bgStars.toBack()
            mmLoseLabelB.toBack()
            playerhealthModel.opacity = 100
            playerhealthBorder.opacity = 100
            healthbar.opacity = 100
            
            score.opacity=100
            ingamemenu.visible=True
            if pows[app.selit] == 'heatwave':
                hwicon.visible = True
                pvicon.visible = False
                equiped.value = "["+pows[app.selit]+"]"
                equiped.centerX = 120
                equiped.centerY = 372.5
                amount.value = "["+str(app.heat)+"]"
                cost.value = 'Cost: [20]'
            if pows[app.selit] == 'pocket vaccum':
                hwicon.visible = False
                pvicon.visible = True
                equiped.value = "["+pows[app.selit]+"]"
                equiped.centerX = 135
                equiped.centerY = 372.5
                amount.value = "["+str(app.poctvacc)+"]"
                cost.value = 'Cost: [30]'
            if app.heatcd and pows[app.selit] == 'heatwave':
                app.heatcooldown -= 1
                cdtimer.value = app.heatcooldown//app.stepsPerSecond
                if app.heatcooldown <= 0:
                    app.heatcd = False
            else:
                app.heatcooldown = heatcdsec*app.stepsPerSecond
            
            if app.pctcd and pows[app.selit] == 'pocket vaccum':
                app.pctcooldown -= 1
                cdtimer.value = app.pctcooldown//app.stepsPerSecond
                if app.pctcooldown <= 0:
                    app.pctcd = False
            else:
                app.pctcooldown = pctcdsec*app.stepsPerSecond
        else:
            app.heatcd = False
            app.pctcd = False
            
        
        starship.rotateAngle = angleTo(starship.centerX,starship.centerY,m.centerX,m.centerY)-90
        if abs(starship.dy) < 0.1:
            starship.dy = 0
        if app.keybinds[5] in keey:
            if starship.dy > -5:
                starship.dy -= 1
        elif app.keybinds[6] in keey:
            if starship.dy < 5:
                starship.dy += 1
        else:
            if starship.dy < 0:
                starship.dy += 0.2
            elif starship.dy > 0:
                starship.dy -= 0.2
        if starship.centerY > 482:
            starship.centerY = -32
        if starship.centerY < -32:
            starship.centerY = 482
        
        starship.centerY += starship.dy
        
        playerhealthModel.centerX,playerhealthModel.centerY = starship.centerX,starship.centerY-50
        hbw = playerhealthModel.width
        healthbar.left,healthbar.top = playerhealthModel.left,playerhealthModel.top
        playerhealthBorder.left,playerhealthBorder.top = playerhealthModel.left-3,playerhealthModel.top-3
        
        if app.plr_health != 0:
            healthbar.width = hbw*(app.plr_health/app.player_health)
        
        for i in explosions:
            i.time -= 1
            i.opacity -= 2
            i.rotateAngle += 1
            i.centerX+=app.asteroid_speed
            for ii in i:
                ii.radius += 1
            if i.time < 0 or i.opacity < 2:
                explosions.remove(i)
        
        if app.wait > app.waittime and not app.in_menu:
            #asteroids
            ast = Star(app.spawnX, randrange(40, 360), 30, 13, fill=gradient('tan', 'grey'), roundness=95)
            asteroids.add(ast)
            ast.width = randrange(30, 100)
            ast.length = randrange(30, 100)
            
            #comets
            chancec = randrange(1,app.comet_chance)
            numc = randrange(1,app.comet_chance)
            if chancec == numc:
                comt = Star(app.spawnX, randrange(40, 360), 20, 13, fill=gradient('lightCyan','lightCyan','lightSteelBlue', 'grey'), roundness=95)
                comt.dx = 0
                comt.dy = 0
                comets.add(comt)
            #rapid
            chancer = randrange(1,app.rapid_chance)
            numr = randrange(1,app.rapid_chance)
            if chancer == numr:
                rapd = Star(app.spawnX, randrange(40, 360), 20, 13, fill=gradient('tan','grey'), roundness=95)
                rapd.dx = 0
                rapd.dy = 0
                rapid.add(rapd)
            
            #star
            chances = randrange(1,app.star_chance)
            nums = randrange(1,app.star_chance)
            if chances == nums:
                star = Star(app.spawnX, randrange(40, 360), 20, randrange(5,7), fill=gradient('gold','yellow'), roundness=95)
                star.dx = 0
                star.dy = 0
                shootingstar.add(star)
                
                
            #bh
            chanceb = randrange(1,app.bh_chance)
            numb = randrange(1,app.bh_chance)
            if chanceb == numb:
                bhcir = Circle(app.spawnX, randrange(40,360), 39.34, fill=gradient('black', 'black', 'grey'), border=gradient('yellow', 'gold', 'orange', start='center'), borderWidth=4)
                blackhole.add(bhcir)
            #asp
            chancea = randrange(1,app.alien_spaceship_chance)
            numa = randrange(1,app.alien_spaceship_chance)
            if chancea == numa:
                alienShip = Group(
                    Oval(200, 172, 120, 30, fill=gradient('royalBlue', 'navy'), border='lightGrey'),
                    Circle(200, 160, 29, fill=None, border='white'),
                    Line(182, 142, 189, 138, fill='white'),
                    Line(187, 135, 169, 112, fill='white'),
                    Line(213, 135, 231, 112, fill='white'),
                    Circle(169, 112, 5, fill='gold'),
                    Circle(231, 112, 5, fill='gold'),
                    Oval(200, 172, 120, 30, fill=gradient('royalBlue', 'navy'), border='lightGrey'),
                    Oval(158, 171, 10, 5, fill='gold', rotateAngle = 15),
                    Oval(171, 176, 10, 5, fill='gold', rotateAngle = 14),
                    Oval(184, 176, 10, 5, fill='gold', rotateAngle = 5),
                    Oval(200, 176, 10, 5, fill='gold', rotateAngle = 0),
                    Oval(216, 176, 10, 5, fill='gold', rotateAngle = -5),
                    Oval(231, 176, 10, 5, fill='gold', rotateAngle = -14),
                    Oval(242, 171, 10, 5, fill='gold', rotateAngle = -15),
                    Polygon(163, 184, 173, 196, 231, 196, 237, 184, fill='dimGray', border='white'),
                    )       
                
                aspm = Group(alienShip)
                aspm.centerX = app.spawnX
                aspm.centerY = randrange(40,360)
                aspm.shoot = 20
                # aspm.beam = Group(Polygon(192, 194, 179, 800, 221, 800, 208, 194, fill=gradient('chartreuse', 'lime', 'lightGreen', start='top')),Circle(200,-500,0.1))
                alienSP.add(aspm)
                # alienbeam.append([aspm.beam,aspm])
            #asteroid wall
            asteroid_n = 8
            if randrange(1,app.asteroid_wall_chance)==randrange(1,app.asteroid_wall_chance):
                for i in range(asteroid_n):
                    ast = Star(randrange(450,500), i*(400/(asteroid_n-1)), 30, 13, fill=gradient('tan', 'grey'), roundness=95)
                    ast.width = randrange(30, 100)
                    ast.length = randrange(30, 100)
                    asteroids.add(ast)
            #boss
            if score.value//app.boss_min_points == score.value/app.boss_min_points and score.value != 0:
                bossasteroidModel.active = True
            app.wait = 0
            if app.waittime < app.min_spawn_rate:
                app.waittime = app.min_spawn_rate
            else:
                app.waittime -= 1
        for i in asteroids:
            i.centerX+=app.asteroid_speed
            i.rotateAngle+=10
            if i.centerX < -10:
                app.plr_health -= 10
                asteroids.remove(i)
            bhf(asteroids,i)
        
        if app.waite < app.waitelime:
            app.waite += 1
        else:
            app.waite = 0
        for i in comets:
            i.dx = cos(radians(i.rotateAngle))
            i.dy = sin(radians(i.rotateAngle))
            
            if not app.waite < app.waitelime:
                i.rotateAngle = random.choice([-45,45])
            
            if i.centerY > 400:
                i.centerY = 400
            if i.centerY < 0:
                i.centerY = 0
            if i.centerX < -i.radius:
                app.plr_health -= 10
                comets.remove(i)
            
            i.centerX += i.dx*app.asteroid_speed*2
            i.centerY += i.dy*app.asteroid_speed*4
            tr = Circle(i.centerX,i.centerY,15,fill='white',opacity = 50)
            tr.time = 15
            if app.ldmtog:
                tr.time = 2
            comettrail.add(tr)
            bhf(comets,i)
        for i in comettrail:
            i.centerX -= 2
            if i.time < 0:
                comettrail.remove(i)
                
            i.time -= 1
            i.opacity -= 1
            i.radius -= 0.5
        
        for i in rapid:
            i.centerX+=app.asteroid_speed*app.rapid_speed_multiplier
            i.rotateAngle+=20
            if i.centerX < -10:
                app.plr_health -= 5
                rapid.remove(i)
            t = Circle(i.centerX,i.centerY,15,fill='grey',opacity = 50)
            t.time = 15
            if app.ldmtog:
                t.time = 2
            rapidtrail.add(t)
            bhf(rapid,i)
        for i in rapidtrail:
            i.centerX -= 2
            if i.time < 0:
                rapidtrail.remove(i)
            
                
            i.time -= 1
            i.opacity -= 1
            i.radius -= 0.1
        for i in shootingstar:
            i.dx = i.centerX-starship.centerX
            i.dy = i.centerY-starship.centerY
            dist = ((i.dx**2)+(i.dy**2))**0.5
            if dist != 0:
                i.dx /= dist
                i.dy /= dist
            i.centerX += i.dx*app.asteroid_speed*1.5
            i.centerY += i.dy*app.asteroid_speed*1.5
            i.rotateAngle+=20
            t = Star(i.centerX,i.centerY,i.radius,i.points,fill='yellow',opacity = 25,roundness = i.roundness)
            t.time = 15
            if app.ldmtog:
                t.time = 2
            sstrail.add(t)
            bhf(shootingstar,i)
            if i.hitsShape(starship):
                app.plr_health -= 1
        for i in sstrail:
            i.centerX -= 0.65
            i.opacity-=1
            i.radius-=0.1
            if i.time < 0:
                sstrail.remove(i)
            i.time -= 1
        for i in blackhole:
            i.centerX -= 2.3
            if i.centerX < -i.radius:
                blackhole.remove(i)
        for i in alienSP:
            i.shoot -= 1
            if i.shoot < 0:
                i.shoot = 20
                l = Rect(i.centerX,i.centerY,10,20,fill='lime')
                l.time = 60
                l.rotateAngle = angleTo(l.centerX,l.centerY,starship.centerX,starship.centerY)
                l.dx = cos(radians(l.rotateAngle-90))
                l.dy = sin(radians(l.rotateAngle-90))
                alienlasers.add(l)
            i.centerX -= 2.3
            bhf(alienSP,i)
        for i in alienlasers:
            if not app.ldmtog:
                tr = Rect(500,500,10,10,fill='lime')
                ofc = 10
                cdx = random.choice([-i.dx*ofc,i.dx*ofc])
                cdy = random.choice([-i.dy*ofc,i.dy*ofc])
                tr.centerX,tr.centerY = i.centerX+cdx,i.centerY+cdy
                tr.time = 10
                SPlasertrail.add(tr)
            
            i.time -= 1
            if i.time < 0:
                alienlasers.remove(i)
            i.centerX += i.dx*5
            i.centerY += i.dy*5
            if i.hitsShape(starship):
                app.plr_health -= 10
                alienlasers.remove(i)
            bhf(alienlasers,i)
        for i in SPlasertrail:
            i.time -= 1
            if i.time < 0:
                SPlasertrail.remove(i)
            i.rotateAngle += randrange(5,20)
            sd = 1
            if i.width > sd+1 and i.height > sd+1:
                i.width -= sd
                i.height -= sd
            i.opacity -= 2
        
        for i in heatwaves:
            i.centerX += 1
            if i.centerX > 400+i.width:
                heatwaves.remove(i)
            for a in asteroids:
                if (i.hitsShape(a)):
                    asteroids.remove(a)
                    placeex(a.centerX,a.centerY)
                    score.value+=1
            for c in comets:
                if (i.hitsShape(c)):
                    comets.remove(c)
                    placeex(c.centerX,c.centerY)
                    comtex = Circle(c.centerX,c.centerY,100,fill='white',opacity = 25)
                    comettrail.add(comtex)
                    comtex.time = 10
                    if distance(starship.centerX,starship.centerY,c.centerX,c.centerY) < 100:
                        app.plr_health -= 5
                    score.value+=2
            for r in rapid:
                if i.hitsShape(r):
                    rapid.remove(r)
                    placeex(r.centerX,r.centerY)
                    score.value += 2
            for s in shootingstar:
                if i.hitsShape(s):
                    shootingstar.remove(s)
                    placeex(s.centerX,s.centerY)
                    score.value += 3
        for i in pctvcm:
            i.centerX += i.dx*i.speed
            i.centerY += i.dy*i.speed
            i.rotateAngle += 20
            for a in asteroids:
                if distance(a.centerX,a.centerY,i.centerX,i.centerY) < 150:
                    pull_angle = angleTo(a.centerX, a.centerY, i.centerX, i.centerY)
                    pull_dx = cos(radians(pull_angle))
                    pull_dy = sin(radians(pull_angle))
                    a.centerX += pull_dx*3
                    a.centerY += pull_dy*3
                if a.hitsShape(i):
                    asteroids.remove(a)
            
        
        if bossasteroidModel.active:
            bossasteroidModel.centerX-=0.875
            bossasteroidModel.rotateAngle += 2
        else:
            bossasteroidModel.centerX = 550
            bossasteroidModel.health = 10
        if bossasteroidModel.health < 0:
            bossasteroidModel.active = False
        if bossasteroidModel.centerX < -bossasteroidModel.radius:
            bossasteroidModel.active = False
            app.plr_health = 0
        if starship.hitsShape(asteroids) or starship.hitsShape(bossasteroidModel) or starship.hitsShape(comets) or starship.hitsShape(rapid) or starship.hitsShape(blackhole) or starship.hitsShape(alienSP):
            lose()
        if not app.ldmtog:
            for i in bgStars:
                
                i.centerX -= 1
                if i.centerX < 0:
                    i.centerX = 400
                    i.centerY = randrange(0,400)
        
        for i in lasers:
            #####
            if not app.ldmtog:
                if not app.charged:
                    tr = Rect(500,500,10,10,fill='red')
                    ofc = 10
                    cdx = random.choice([-i.dx*ofc,i.dx*ofc])
                    cdy = random.choice([-i.dy*ofc,i.dy*ofc])
                    tr.centerX,tr.centerY = i.centerX+cdx,i.centerY+cdy
                    tr.time = 10
                    laserstrail.add(tr)
                else:
                    tr = Rect(500,500,10,10,fill=gradient('red','orange'))
                    ofc = 10
                    cdx = random.choice([-i.dx*ofc,i.dx*ofc])
                    cdy = random.choice([-i.dy*ofc,i.dy*ofc])
                    tr.centerX,tr.centerY = i.centerX+cdx,i.centerY+cdy
                    tr.time = 10
                    laserstrail.add(tr)
            #####
            if i.time < 0:
                lasers.remove(i)
            for a in asteroids:
                if (i.hitsShape(a)):
                    if not app.charged: lasers.remove(i)
                    asteroids.remove(a)
                    placeex(a.centerX,a.centerY)
                    score.value+=1
            for c in comets:
                if (i.hitsShape(c)):
                    if not app.charged: lasers.remove(i)
                    comets.remove(c)
                    placeex(c.centerX,c.centerY)
                    comtex = Circle(c.centerX,c.centerY,100,fill='white',opacity = 25)
                    comettrail.add(comtex)
                    comtex.time = 10
                    if distance(starship.centerX,starship.centerY,c.centerX,c.centerY) < 100:
                        app.plr_health -= 5
                    score.value+=2
            for r in rapid:
                if i.hitsShape(r):
                    if not app.charged: lasers.remove(i)
                    rapid.remove(r)
                    placeex(r.centerX,r.centerY)
                    score.value += 2
            for s in shootingstar:
                if i.hitsShape(s):
                    if not app.charged: lasers.remove(i)
                    shootingstar.remove(s)
                    placeex(s.centerX,s.centerY)
                    score.value += 3
                    
            for b in blackhole:
                if i.hitsShape(b):
                    lasers.remove(i)
                    b.radius += 1
            for a in alienSP:
                if i.hitsShape(a):
                    if not app.charged: lasers.remove(i)
                    placeex(a.centerX,a.centerY)
                    alienSP.remove(a)
                    score.value += 1
            if i.hitsShape(bossasteroidModel) and bossasteroidModel.active:
                if not app.charged: lasers.remove(i)
                bossasteroidModel.health -= 1
                score.value += 2
            i.centerX += i.dx*app.laser_speed
            i.centerY += i.dy*app.laser_speed
            i.time -= 1
        for i in laserstrail:
            i.time -= 1
            if i.time < 0:
                laserstrail.remove(i)
            i.rotateAngle += randrange(5,20)
            sd = 1
            if i.width > sd+1 and i.height > sd+1:
                i.width -= sd
                i.height -= sd
            i.opacity -= 2
        if app.plr_health < 0:
            lose()
        app.wait += 1
#===============================================================================================

from cmu_graphics.cmu_graphics import run
run()
