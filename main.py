import pygame

pygame.init()

win = pygame.display.set_mode((600,480))

pygame.display.set_caption("First Game")


def slice_spritesheet(sheet_path, sprite_size):
    # Load the sprite sheet
    sprite_sheet = pygame.image.load(sheet_path)

    # Calculate the number of sprites in the sheet
    num_sprites_x = sprite_sheet.get_width() // sprite_size[0]
    num_sprites_y = sprite_sheet.get_height() // sprite_size[1]

    # Slice the sprite sheet into individual sprites
    sprites = []
    for y in range(num_sprites_y):
        for x in range(num_sprites_x):
            rect = pygame.Rect(x * sprite_size[0], y * sprite_size[1], *sprite_size)
            sprite = sprite_sheet.subsurface(rect)
            sprites.append(sprite)

    return sprites

# Load the sprite sheets
right_image = pygame.image.load("Assets/Images/playerRight.png")
left_image = pygame.image.load("Assets/Images/playerLeft.png")
front_image = pygame.image.load("Assets/Images/playerUp.png")
back_image = pygame.image.load("Assets/Images/playerDown.png")
fire_image = pygame.image.load("Assets/Images/fire.png")
fireball_image = pygame.image.load("Assets/Images/fireball.png")
ui_image = pygame.image.load("Assets/Texture/UI Packs/Wood/UI_Shadow_Font_B.png")
# Slice the sprite sheets into individual sprites
walkRight = slice_spritesheet("Assets/Images/playerRight.png", (right_image.get_width() // 4, right_image.get_height()))
walkLeft = slice_spritesheet("Assets/Images/playerLeft.png", (left_image.get_width() // 4, left_image.get_height()))
walkFront = slice_spritesheet("Assets/Images/playerDown.png", (front_image.get_width() // 4, front_image.get_height()))
walkBack = slice_spritesheet("Assets/Images/playerUp.png", (back_image.get_width() // 4, back_image.get_height()))
fire = slice_spritesheet("Assets/Images/fire.png", (fire_image.get_width() // 4, fire_image.get_height()))
fireball = slice_spritesheet("Assets/Images/fireball.png", (fire_image.get_width() // 4, fire_image.get_height()))
ui = slice_spritesheet("Assets/Texture/UI Packs/Wood/UI_Shadow_Font_B.png", (fire_image.get_width() // 4, fire_image.get_height()))

# Background image
bg = pygame.image.load("Assets/tileset/Tiled/Pellet Town.png")
bg = pygame.transform.scale(bg, (2048, 1536))

# Character image
char = walkFront[0]

# Clock object for controlling frame rate
clock = pygame.time.Clock()

# Initial position and size of the character
x = 250
y = 200
width = 64
height = 64

# Initial velocity of the character
vel = 5

# Flags for character movement direction
left = False
right = False
front = False
back = False

# Flag for dashing
dash = False

# Counter for character animation
walkCount = 0

# Flag for fireball
if_fireball = False

# Start time of fireball
fireball_start_time = None

# Set the frame rate
frame_rate = 30

# Set the dash speed
dash_speed = 30

# Set a variable to count the number of frames since the dash started
dash_count = 0

# Adjust the velocity based on the frame rate
vel = 5 * frame_rate / 30

# Set the dash cooldown in frames (5 seconds * 30 frames per second)
dash_cooldown = 30

# Set a variable to count the number of frames since the last dash
dash_timer = dash_cooldown

# Create a font object
font = pygame.font.Font(None, 36)

# Camera offsets for scrolling the background
camera_offset_x = 250
camera_offset_y = 400

# Draw the cooldown timer
text = font.render(f'Dash cooldown: {1 - dash_timer // 30}', True, (255, 255, 255))

# Calculate the position to blit the text
text_width, text_height = text.get_size()
position_x = win.get_width() - text_width - 10  # 10 pixels from the right edge
position_y = win.get_height() - text_height - 10  # 10 pixels from the bottom edge


def redrawGameWindow():
    global walkCount, camera_offset_x, camera_offset_y, dash, if_fireball, fireball
    
    win.blit(bg, (-camera_offset_x, -camera_offset_y))

    if left:
       win.blit(walkLeft[walkCount // 3 % len(walkLeft)], (x,y))
       camera_offset_x -= vel
    elif right:
       win.blit(walkRight[walkCount // 3 % len(walkRight)], (x,y))
       camera_offset_x += vel
    elif front:
       win.blit(walkFront[walkCount // 3 % len(walkFront)], (x,y))
       camera_offset_y += vel
    elif back:
       win.blit(walkBack[walkCount // 3 % len(walkBack)], (x,y))
       camera_offset_y -= vel
    else:
        win.blit(char, (x,y))

    walkCount += 1
    win.blit(ui[0], (position_x, position_y - 100)) 
    win.blit(text, (position_x, position_y))
    

    pygame.display.update()

    # Function to handle user input
def handle_input():
    global vel, dash_count, dash_timer, dash, left, right, front, back, walkCount, if_fireball, position_x, position_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and dash_timer >= dash_cooldown:  # Start the dash
        dash_count = 10  # Dash for 10 frames
        dash_timer = 0  # Reset the dash timer

    if dash_count > 0:  # If currently dashing
        vel = dash_speed
        dash_count -= 1  # Decrease the dash count
        dash = True  # Set the dash flag
    else:  # If not dashing
        vel = 5 * frame_rate / 30

    if dash_timer < dash_cooldown:  # If in cooldown period
        dash_timer += 1  # Increase the dash timer
    # Remove the unused variable "text"
    font.render(f'Dash cooldown: {1 - dash_timer // 30}', True, (255, 255, 255))
    win.blit(text, (position_x, position_y))

    if keys[pygame.K_a]:
        left = True
        right = False
        front = False
        back = False
    elif keys[pygame.K_d]:
        right = True
        left = False
        front = False
        back = False
    elif keys[pygame.K_w]:
        front = False
        back = True
        left = False
        right = False
    elif keys[pygame.K_s]:
        back = False
        front = True
        left = False
        right = False
    else:
        right = False
        left = False
        front = False
        back = False
        walkCount = 0

    if keys[pygame.K_q]:
        if_fireball = True

#mainloop
run = True
while run:
    clock.tick(frame_rate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    handle_input()
    redrawGameWindow()

pygame.quit()
