import os
import pygame
import time

# Load/Save Game
import pickle


# Game Settings
    # Game Setup
pygame.init()

    # Game Size Screen
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

    # Game Title
pygame.display.set_caption("Shards of Moonstones")

    # Game Clock
clock = pygame.time.Clock()

    #Ressources
font = pygame.font.SysFont(None, 25)

black = (0,0,0)
green = (0,180,80)
red = (200,0,0)
Text_ui_Color = black

bright_green = (96,255,96)
bright_red = (255,96,96)
game_ui_color = (245,218,168)
text_action_color = black #Temporary

sky_color = (153,217,234)
ground_color = (34,177,76)

    # Game Files
Title_Screen_Background = pygame.image.load("Data\Background\Title_Screen_Background.png")
Game_ui_Screen = pygame.image.load("Data\Game_ui\Game_ui_Cutscene.png")



# Game Core
def Game_Save():
    with open("savefile", "wb") as f:
        pickle.dump(PlayerIG, f)

def Game_Load():
    if os.path.exists("savefile") == True:
        with open("savefile", "rb") as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
        Main_Menu()
    else:
        Title_Screen()

def Quit_Game():
    pygame.quit()
    quit()



    
def Title_Screen():
    gameDisplay.blit(Title_Screen_Background, (0,0))
    Text_Display("Shards of Moostones", display_width/2, display_height*0.25, Text_Title_Screen)
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Button        # 200/400/600      - Box Width / 2     # Height            - Box Height /2      800/8 = 100      600 / 12 = 50
        Button("Start", display_width*0.25 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Game_Intro)
        Button("Load",  display_width*0.50 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Game_Load)
        Button("Exit",  display_width*0.75 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Quit_Game)

        pygame.display.update()

 
def Game_Intro():
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
# Setup
        gameDisplay.blit(Game_ui_Screen, (0,0))
        Game_Text_Event()
        pygame.display.update()
        global PlayerIG

    # Game Intro 1 :
        # Player Name
        if GameStateIG.Text_Order == 1:
            GameStateIG.Text_Line_Right[1] = "What is your name?"
            GameStateIG.Text_Line_Right[2] = "->"
            GameStateIG.Event[1] == True

        if GameStateIG.Text_Order == 3 and GameStateIG.Text_Line[0] != "":
            PlayerIG = Player(GameStateIG.Text_Line[0])
            game_intro_2()
        
        # Game_Event[1]
        if GameStateIG.Text_Order == 3 and GameStateIG.Text_Line[0] == "" or GameStateIG.Game_Event[1] == True:
            GameStateIG.Text_Line[2] = "That doesn't seem like a real name!"
            GameStateIG.Text_Line[3] = "->"
            GameStateIG.Game_Event[1] = True

            if GameStateIG.Text_Order == 4 or GameStateIG.Game_Event[2] == True:
                GameStateIG.Text_Line[3] = "Please, tell me your name!"
                GameStateIG.Text_Line[4] = "->"
                GameStateIG.Game_Event[2] = True

                if GameStateIG.Text_Order == 5 and GameStateIG.Text_Line[0] == "":
                    GameStateIG.Text_Order = 4

                # Player Name - Game_Event[1]
                elif GameStateIG.Text_Order == 5 and GameStateIG.Text_Line[0] != "":
                    PlayerIG = Player(GameStateIG.Text_Line[0])
                    game_intro_2()















    # Game Tools Development
    
# Main Tools
class GameState:
    def __init__(self, name):
        self.Text_Line_Left     = ["", "1", "2", "4", "5", "6", "7", "8"]
        self.Text_Line_Right    = ["", "1", "3", "4", "5", "6", "7", "8"]
        self.Text_Order         = 1

        GameStateIG.Event = [False,False,False,False,False,False]

GameStateIG = GameState("GameState")

        
def Text_Display(msg, x, y, Text_Type):
    textSurf, textRect = Text_Type(msg, font)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)

    
def Button(msg,x,y,w,h,ic,ac,Text_Type,action=None):
    # msg : Message / ic : Inactive Color / ac : Active Color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button Box - Active Color
    if x < mouse[0] < x+w and y < mouse[1] < y+h :
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        # Action
        if click[0] ==1 and action !=None:
            action()

    # Button Box - Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))


    textSurf, textRect = Text_Type(msg, font)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def Game_Text_Event():
# Left
    # Character Name
    Text_ui(GameStateIG.Text_Line_Left[1], 10, 450)

    # Text
    Text_ui(GameStateIG.Text_Line_Left[2], 10, 470)
    Text_ui(GameStateIG.Text_Line_Left[3], 10, 490)
    Text_ui(GameStateIG.Text_Line_Left[4], 10, 510)
    Text_ui(GameStateIG.Text_Line_Left[5], 10, 530)
    Text_ui(GameStateIG.Text_Line_Left[6], 10, 550)
    Text_ui(GameStateIG.Text_Line_Left[7], 10, 570)


# Right
    # Character Name
    Text_ui(GameStateIG.Text_Line_Right[1], 460, 450)

    # Text
    Text_ui(GameStateIG.Text_Line_Right[2], 460, 470)
    Text_ui(GameStateIG.Text_Line_Right[3], 460, 490)
    Text_ui(GameStateIG.Text_Line_Right[4], 460, 510)
    Text_ui(GameStateIG.Text_Line_Right[5], 460, 530)
    Text_ui(GameStateIG.Text_Line_Right[6], 460, 550)
    Text_ui(GameStateIG.Text_Line_Right[7], 460, 570)
    




# Secondary Tools
def Text_Title_Screen(msg, font):
    font = pygame.font.SysFont(None, 75)
    textSurface = font.render(msg, True, (210,100,240))
    return textSurface, textSurface.get_rect()
    
def Text_Title_Selection(msg, font):
    font = pygame.font.SysFont(None, 30)
    textSurface = font.render(msg, True, (black))
    return textSurface, textSurface.get_rect()

def Text_ui(msg, x, y):
    font = pygame.font.SysFont("comicsansms", 20)
    Text_Line = font.render(msg, True, Text_ui_Color)
    gameDisplay.blit(Text_Line,  (x,y))
        
Title_Screen()
