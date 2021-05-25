import pygame as pyg
from pygame.locals import *
import sys
import time


board=[[None]*3,[None]*3,[None]*3]
XO='x'
winner=None
draw=None
width=300
height=300
line_color=(0,0,0)
white=(255,255,255)
pyg.init()

screen = pyg.display.set_mode((width, height + 100))
pyg.display.set_caption("TIC TAC TOE Using PYGAME")
#print(pygame.display.Info())
initaiting_window = pyg.image.load("C:\\Users\\Azhar\\Desktop\\Maria\\PY-HUB-WORKSHOP-main\\modiications")
initaiting_window = pyg.transform.scale(initaiting_window, ((width, height + 100)))
ximg = pyg.image.load("C:\\Users\\Azhar\\Desktop\\Maria\\PY-HUB-WORKSHOP-main\\modifications")
oimg = pyg.image.load("C:\\Users\\Azhar\\Desktop\\Maria\\PY-HUB-WORKSHOP-main\\modifications")
ximg = pyg.transform.scale(ximg, (60, 60))
oimg = pyg.transform.scale(oimg, (60, 60))

def game_initiating_window():
    screen.blit(initaiting_window, (0, 0))
    pyg.display.update()
    time.sleep(3)
    screen.fill(white)
    pyg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 5)
    pyg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 5)
    pyg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 5)
    pyg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 5)
    pyg.display.update()
    #time.sleep(10)
    draw_status()

def draw_status():
    global draw,winner
    if winner is None:
        message=XO.upper()+"'s turn"
    else:
        message=winner.upper()+"  Won the game!"
    if draw:
        message="Game Draw!"

    font = pyg.font.Font(None, 30)

    text = font.render(message, 1, (255, 255, 255))

    screen.fill((0, 0, 0), (0, 300, 300, 100))
    text_rect = text.get_rect(center=(width / 2, 350))
    screen.blit(text, text_rect)
    pyg.display.update()
    time.sleep(1)


def win():
    global winner,draw,board
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != None)):
            winner = board[row][0]
            pyg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6),
                         4)
            break

    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pyg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height),5)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pyg.draw.line(screen, (250, 70, 70), (20,20), (300, 300), 4)

    elif (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pyg.draw.line(screen, (250, 70, 70), (20,280),(280,20), 4)

    elif (all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()

def drawXO(row,col):
    global XO
    if(row==1):
        posy=25
    if(row==2):
        posy=height/3+25
    if(row==3):
        posy=height/3*2+25
    if(col==1):
        posx=25
    if(col==2):
        posx=width/3+25
    if(col==3):
        posx=width/3*2+25
    board[row-1][col-1]=XO
    if(XO=='x'):
        screen.blit(ximg,(posx,posy))
        XO='o'
    else:
        screen.blit(oimg,(posx,posy))
        XO='x'
    pyg.display.update()



def user_interface():
    x,y=pyg.mouse.get_pos()
    if x<width/3:
        col=1
    if (x<width/3*2 and x>width/3):
        col=2
    if (x<width and x>width/3*2):
        col=3
    if x>width:
        col=None
    if y<height/3:
        row=1
    if (y<height/3*2 and y>height/3):
        row=2
    if (y<height and y>height/3*2):
        row=3
    if y>height:
        row=None
    print("x=",x," y=",y)
    print("row=",row," col=",col )
    if(row and col and (board[row-1][col-1] is None)):
        global XO
        drawXO(row,col)
        win()
def reset_game():
    global board,XO,draw,winner
    board=[[None]*3,[None]*3,[None]*3]
    X0='x'
    winner=None
    draw=False
    time.sleep(3)
    game_initiater()



game_initiater()
while(True):
    for event in pyg.event.get():
        #print(event.type)
        if event.type== QUIT:
            pyg.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            user_interface()
            if(winner or draw):
                reset_game()

    pyg.display.update()
 

