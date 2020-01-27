from graphics import *
from carromPiece import *
from player import *
#Constants
LEFT = 1
WIDTH = 900
HEIGHT = 900
RUNNING = True
QUEEN = 0
BLACK = 1
WHITE = 2
CENTERL = 377
CENTERR = 384
LEFTTOP = 50
numPIECE = 9
sizePiece = 250
sizeStriker = 60
POINTSB = 10
POINTSW = 20
POINTSQ = 50
TEXTCOLOR = [0,0,255]
BLACKCOLOR = [0,0,0]

def text_objects(fontSize, txtColor, backColor, rotAngle, x ,y, txt):
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(txt, True, txtColor, backColor)
    text = pygame.transform.rotate(text, rotAngle)
    textRect = text.get_rect()
    textRect.center = (x, y)
    return text, textRect

def blackPiecePos():
    i = 0
    k = 500
    j = 45
    q = 0
    z = 1
    d = 0
    while i < numPIECE:
        xCoord = 0
        yCoord = 0
        pieces = pygame.sprite.RenderUpdates()
        if(0 <= i < 3):
            if(i%2 == 0):
                z = -1
            xCoord = CENTERR + q*(z)
            yCoord = CENTERL + j
            q = 34
            j = 70
            z = 1
        if (3 <= i < 5):
            xCoord = CENTERR +40 + d
            yCoord = CENTERL - j
            j -= 70
            d += 40
        if (i==5):
            xCoord = CENTERR + 35
            yCoord = CENTERL - 25
        if (i == 6):
            q+=45
            xCoord = CENTERR - q
            yCoord = CENTERL + 10
        if (i == 7):
            xCoord = CENTERR - 43
            yCoord = CENTERL - 70
        if (i == 8):
            xCoord = CENTERR - 40
            yCoord = CENTERL - 25
        pieces.add(CarromPiece(xCoord, yCoord, 0, BLACK, POINTSB))
        i += 1
        k += 20
    return 0
def whitePiecePos():
    i = 0
    k = 0
    l = 0
    j = 27
    m = 0
    z = 0
    while i < numPIECE:
        xCoord = CENTERR
        yCoord = CENTERL
        if 0 <= i < 2:
            xCoord = CENTERR + 40 + k
            yCoord = CENTERL + 20 + k
            k += 30
        if 2 <= i < 4:
            xCoord = CENTERR - l - 40
            yCoord = CENTERL + l + 20
            l += 30
        if 4 <= i < 6:
            xCoord = CENTERR
            yCoord = CENTERL - 65 - j
            j -= 45
        # CENTERL = 452
        # CENTERR = 423
        if 6 <= i < 9:
            q = 1
            zeroX = 1
            zeroY = 1
            if (i % 7 == 0):
                q = -1
            if (i % 8 == 0):
                zeroX = 0
                zeroY = 130
            xCoord = CENTERR + (+78) * q * zeroX
            yCoord = CENTERL + (-40) + zeroY
        pieces = pygame.sprite.RenderUpdates()
        pieces.add(CarromPiece(xCoord, yCoord, 0, WHITE, POINTSW))
        i += 1
    return 0
#function will give menu
def start():
    screen = pygame.display.set_mode((WIDTH + 100, HEIGHT + 100))
    pygame.display.set_caption('Carrom by Sneha')
    screen.fill([0, 0, 0])
    return screen

#function will give instructions and ask for either type game 1 or type game 2
def instructions():
    return 0

def resizePicture(picName,sizeW, sizeH):
    imageFile = picName
    im1 = Image.open(imageFile)
    im2 = im1.resize((sizeW, sizeH))
    im2.save(picName)

def main():
    #Initialize
    pygame.init()
    screen = start()
    pygame.display.flip()
    #re-shape Board Image
    resizePicture("Board.png", WIDTH, HEIGHT)
    resizePicture("queenImage.png", sizePiece, sizePiece)
    resizePicture("blackPieceImage.png", sizePiece, sizePiece)
    resizePicture("whitepiece.png", sizePiece, sizePiece)
    resizePicture("striker1.png", sizeStriker, sizeStriker)

    #Text Message
    [text, textRect] = text_objects(32, TEXTCOLOR, BLACKCOLOR, 270, 975, 875, 'Player 1')
    [text2, textRect2] = text_objects(32, [255,20,147], BLACKCOLOR, 90, 20, 115, 'Player 2')
    [text3, textRect3] = text_objects(32, [128, 0, 128], BLACKCOLOR, 0, 120, 975, 'Player 3')
    [text4, textRect4] = text_objects(32, [255,255,255], BLACKCOLOR, 0, 885, 25, 'Player 4')

    #Display Board
    background_image = pygame.image.load("Board.png").convert_alpha()
    screen.blit(background_image, [LEFTTOP, LEFTTOP])
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    #Create Queen Piece
    pieces = pygame.sprite.RenderUpdates()
    pieces.add(CarromPiece(CENTERR,CENTERL,0,QUEEN, POINTSQ))

    #Create White PieceS
    whitePiecePos()

    #Create Black PieceS
    blackPiecePos()

    #Create Player / Striker
    player1 = Player("striker1.png")
    player1.rect.x = 753
    player1.rect.y = 475
    player_list = pygame.sprite.RenderUpdates()
    player_list.add(player1)
    player_list.draw(screen)
    pygame.display.flip()

    #event Loop
    piece_selected = pygame.sprite.GroupSingle()

    #Clock of Game
    clock = pygame.time.Clock()
    #Game Loop
    while RUNNING:
        pieces.clear(screen, background_image)
        #pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            break
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print ("You pressed the left mouse button at (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            print ("You released the left mouse button at (%d, %d)" % event.pos)
    pygame.quit()
    exit()

if __name__ == '__main__': main()