# Description: This file contains all the constants that are used in the game.
 # Set the frame rate
FRAME_RATE = 30

# Set the dash speed
DASH_SPEED = 30

# Set a variable to count the number of frames since the dash started
DASH_COUNT = 0

# Adjust the velocity based on the frame rate
VEL = 5 * FRAME_RATE / 30

# Set the dash cooldown in frames (5 seconds * 30 frames per second)
DASH_COOLDOWN = 30

# Set a variable to count the number of frames since the last dash
DASH_TIMER = DASH_COOLDOWN

