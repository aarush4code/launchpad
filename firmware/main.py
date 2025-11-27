# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.RGB import RGB, AnimationsModes
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GPIO3, board.GPIO4, board.GPIO2, board.GPIO1, board.GPIO6,board.GPIO26, board.GPIO27]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


rgb = RGB(
    pixel_pin=board.GPIO6,
    num_pixel=6,
    hue_default=0,
    animation_mode=AnimationsModes.STATIC,
    sat_default=0,
)
keyboard.extensions.append(rgb)
 
# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.ENTER,KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)), 
    KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),KC.MEDIA_PLAY_PAUSE, 
    KC.VOLU, KC.VOLD]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()