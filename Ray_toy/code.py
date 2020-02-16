
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_circuitplayground import cp
from color_names import *
from random import randint

# define color list
COLOR_INDEX = [ 
                RED,
                MAROON,
                ORANGE,
                YELLOW,
                OLIVE,
                GREEN,
                AQUA,
                TEAL,
                BLUE,
                NAVY,
                PURPLE,
                PINK,
                WHITE,
                ]

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = AQUA

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)
        
# Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(200, 200, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0xAA0088 # Purple
# inner_sprite = displayio.TileGrid(inner_bitmap,
#                                   pixel_shader=inner_palette,
#                                   x=20, y=20)
# splash.append(inner_sprite)

# Draw a label
# text_group = displayio.Group(max_size=10, scale=2, x=35, y=120)
# text = "Merry Chirstmas!"
# text_area = label.Label(terminalio.FONT, text=text, color=BLACK)
# text_group.append(text_area) # Subgroup for text scaling
# splash.append(text_group)

# def hexprep(INT_Value_To_Convert):
#     var = hex(int(INT_Value_To_Convert)).split('0x')
#     if (len(var[1]) < 2):
#         var[0] = '0'
#         return str(var[0] + var[1])
#     return(var[1])

while True:
    if not cp.switch:
        print("Slide switch off!")
        cp.pixels.fill((0, 0, 0))
        color_palette[0] = AQUA
        continue
    else:
        # R = 0
        # G = 0
        # B = 0
        x, y, z = cp.acceleration
        # print((x, y, z))
        # cp.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))

        inner_bitmap = displayio.Bitmap(30, 30, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = RED # Purple
        inner_sprite = displayio.TileGrid(inner_bitmap,
                                          pixel_shader=inner_palette,
                                          x=int((x)+120), y=int((y)+120))
        splash.append(inner_sprite)
        if(len(splash) > 2):
            splash.pop(1)
        # color_bitmap[int(abs(x)+120),int(abs(y)+120)] = 1
        cp.detect_taps = 1
        if(cp.tapped):
            color_palette[0] = COLOR_INDEX[randint(0,len(COLOR_INDEX)-1)]
            # cp.pixels.fill(color_palette[0])

     #    pixel_color_hex = hexprep((R + abs(int(x)))*2.5) + hexprep((G + abs(int(x)))*2.5) + hexprep((B + abs(int(x)))*2.5)
     #    print(pixel_color_hex)
     #    # print(hex(pixel_color_hex))
        # inner_palette[0] = int(pixel_color_hex,16)
