# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE=(127,0,127)

# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)
pygame.display.set_caption("Ocean View SOS game!")

# Loop until the user clicks the close button.
done = False
flag = None
clock = pygame.time.Clock()


# print text function
def printText(msg, color='BLACK', pos=(50, 50)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos

    screen.blit(textSurface, textRect)

texty = ""
chktexty = 0

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    #clock.tick(10000)

    # Main Event Loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.KEYDOWN:  # If user release what he pressed.
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
            if buttons[0] == 'backspace':
                if len(texty) >= 1:
                    texty = texty[0:len(texty)-1]
                continue
            elif len(buttons[0]) > 1:
                continue
            flag = True
        elif event.type == pygame.KEYUP:  # If user press any key.
            flag = False
        elif event.type == pygame.QUIT:  # If user clicked close.
            done = True

            # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
    printText('Please enter the \'frog\'', 'PURPLE', (50, 25))
    printText(texty, 'RED', (50, 130))

    # Print red text if user pressed any key.
    if flag == True:
        if len(texty) >= 4:
            texty = ""
        printText('you just key down!!', 'RED')
        printText('--> you pressed any key.', 'RED', (50, 70))
        for i in buttons:
            printText('Pressed Key : ' + i, 'RED', (50, 90))
            if chktexty == 0: texty += i
            chktexty=1

    if len(texty) == 4:
        if texty =='frog':
            printText('What the hells going on?', 'BLACK', (50, 155))
        else:
            printText('Not Frog!', 'BLACK', (50, 155))

    # Print blue text if user released any key.
    if flag == False:
        chktexty = 0
        printText('you just key up!!', 'BLUE')
        printText('--> released what you pressed.', 'BLUE', (50, 70))

    # Print default text if user do nothing.
    else:
        printText('Please press any key.')

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

#출처: https: // kkamikoon.tistory.com / 132[컴퓨터를 다루다]