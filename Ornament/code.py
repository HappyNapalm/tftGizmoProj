# Circuit Playground digitalio example

# import time
# import board
# import digitalio

# led = digitalio.DigitalInOut(board.D13)
# led.switch_to_output()

# button = digitalio.DigitalInOut(board.BUTTON_A)
# button.switch_to_input(pull=digitalio.Pull.DOWN)

# while True:
#     if button.value:  # button is pushed
#         led.value = True
#     else:
#         led.value = False

#     time.sleep(0.01)

# Circuit Playground NeoPixel
# import time
# import board
# import neopixel

# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# # choose which demos to play
# # 1 means play, 0 means don't!
# color_chase_demo = 1
# flash_demo = 1
# rainbow_demo = 1
# rainbow_cycle_demo = 1


# def wheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if pos < 0 or pos > 255:
#         return (0, 0, 0)
#     if pos < 85:
#         return (255 - pos * 3, pos * 3, 0)
#     if pos < 170:
#         pos -= 85
#         return (0, 255 - pos * 3, pos * 3)
#     pos -= 170
#     return (pos * 3, 0, 255 - pos * 3)


# def color_chase(color, wait):
#     for i in range(10):
#         pixels[i] = color
#         time.sleep(wait)
#         pixels.show()
#     time.sleep(0.5)


# def rainbow_cycle(wait):
#     for j in range(255):
#         for i in range(10):
#             rc_index = (i * 256 // 10) + j * 5
#             pixels[i] = wheel(rc_index & 255)
#         pixels.show()
#         time.sleep(wait)


# def rainbow(wait):
#     for j in range(255):
#         for i in range(len(pixels)):
#             idx = int(i + j)
#             pixels[i] = wheel(idx & 255)
#         pixels.show()
#         time.sleep(wait)


# RED = (255, 0, 0)
# YELLOW = (255, 150, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)
# BLUE = (0, 0, 255)
# PURPLE = (180, 0, 255)
# WHITE = (255, 255, 255)
# OFF = (0, 0, 0)

# while True:
#     if color_chase_demo:
#         color_chase(RED, 0.1)  # Increase the number to slow down the color chase
#         color_chase(YELLOW, 0.1)
#         color_chase(GREEN, 0.1)
#         color_chase(CYAN, 0.1)
#         color_chase(BLUE, 0.1)
#         color_chase(PURPLE, 0.1)
#         color_chase(OFF, 0.1)

#     if flash_demo:
#         pixels.fill(RED)
#         pixels.show()
#         # Increase or decrease to change the speed of the solid color change.
#         time.sleep(1)
#         pixels.fill(GREEN)
#         pixels.show()
#         time.sleep(1)
#         pixels.fill(BLUE)
#         pixels.show()
#         time.sleep(1)
#         pixels.fill(WHITE)
#         pixels.show()
#         time.sleep(1)

#     if rainbow_cycle_demo:
#         rainbow_cycle(0.05)  # Increase the number to slow down the rainbow.

#     if rainbow_demo:
#         rainbow(0.05)  # Increase the number to slow down the rainbow.

"""
This example uses the accelerometer on the Circuit Playground. It prints the values. Try moving
the board to see the values change. If you're using Mu, open the plotter to see the values plotted.
"""
# import time
# from adafruit_circuitplayground import cp

# while True:
#     x, y, z = cp.acceleration
#     print((x, y, z))

#     time.sleep(0.1)

"""If the switch is to the right, it will appear that nothing is happening. Move the switch to the
left to see the NeoPixels light up in colors related to the accelerometer! The Circuit Playground
has an accelerometer in the center that returns (x, y, z) acceleration values. This program uses
those values to light up the NeoPixels based on those acceleration values."""
# from adafruit_circuitplayground import cp

# # Main loop gets x, y and z axis acceleration, prints the values, and turns on
# # red, green and blue, at levels related to the x, y and z values.
# while True:
#     if not cp.switch:
#         # If the switch is to the right, it returns False!
#         print("Slide switch off!")
#         cp.pixels.fill((0, 0, 0))
#         continue
#     else:
#         R = 0
#         G = 0
#         B = 0
#         x, y, z = cp.acceleration
#         print((x, y, z))
#         cp.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))

# """This example plays a different tone for a duration of 1 second for each button pressed."""
# from adafruit_circuitplayground import cp

# while True:
#     if cp.button_a:
#         cp.play_tone(262, 1)
#     if cp.button_b:
#         cp.play_tone(294, 1)

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_circuitplayground import cp

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00 # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(200, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088 # Purple
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette,
                                  x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(max_size=10, scale=2, x=50, y=120)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area) # Subgroup for text scaling
splash.append(text_group)

while True:
    if not cp.switch:
        print("Slide switch off!")
        cp.pixels.fill((0, 0, 0))
        continue
    else:
        R = 0
        G = 0
        B = 0
        x, y, z = cp.acceleration
        # print((x, y, z))
        cp.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))
        pixel_color_hex = (R + abs(int(x))) + (G + abs(int(x)))<<2 + (B + abs(int(x)))<<4
        # print(hex(pixel_color_hex))
        if(pixel_color_hex < 0xffffff):
        	inner_palette[0] = pixel_color_hex
    	else:
    		print("color to big ")
    pass
