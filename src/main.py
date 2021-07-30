
import board

from kmk.boards.macropact import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.rotary_encoder import Encoder
from kmk.ips import IPS, ips_config

keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

def onRotateA(direction):
    if(direction > 0):
        keyboard._state.tap_key(KC.LSFT(KC.RBRC))
    elif(direction < 0):
        keyboard._state.tap_key(KC.LSFT(KC.LBRC))

def rgbv_onRotateA(direction):
    if(direction > 0):
        keyboard.pixels.increase_val()
    elif(direction < 0):
        keyboard.pixels.decrease_val()

def rgbh_onRotateA(direction):
    if(direction > 0):
        keyboard.pixels.increase_hue()
    elif(direction < 0):
        keyboard.pixels.decrease_hue()

def rgbs_onRotateA(direction):
    if(direction > 0):
        keyboard.pixels.increase_sat()
    elif(direction < 0):
        keyboard.pixels.decrease_sat()
        
def onRotateB(direction):
    if(direction > 0):
        keyboard._state.tap_key(KC.RBRC)
    elif(direction < 0):
        keyboard._state.tap_key(KC.LBRC)

def set_default_handler(*args, **kwargs):
    keyboard.encoders[0].onRotate = onRotateA

def set_handler_rgbv(*args, **kwargs):
    keyboard.encoders[0].onRotate = rgbv_onRotateA

def set_handler_rgbh(*args, **kwargs):
    keyboard.encoders[0].onRotate = rgbh_onRotateA

def set_handler_rgbs(*args, **kwargs):
    keyboard.encoders[0].onRotate = rgbs_onRotateA

keyboard.encoders = [Encoder(board.GP0, board.GP1, onRotateA), Encoder(board.GP2, board.GP3, onRotateB)]
keyboard.ips = IPS()

LAYER1 = KC.MO(1)
LAYER1.after_press_handler(lambda *args, **kwargs: keyboard.ips.load_bitmap("L1.bmp"))
LAYER1.after_release_handler(lambda *args, **kwargs: keyboard.ips.load_bitmap("L0.bmp"))

LAYER2 = KC.MO(2)
LAYER2.after_press_handler(lambda *args, **kwargs: keyboard.ips.load_bitmap("L2.bmp"))
LAYER2.after_release_handler(lambda *args, **kwargs: keyboard.ips.load_bitmap("L0.bmp"))



RGBV = make_key(on_press=set_handler_rgbv, on_release=set_default_handler)
RGBH = make_key(on_press=set_handler_rgbh, on_release=set_default_handler)
RGBS = make_key(on_press=set_handler_rgbs, on_release=set_default_handler)


keyboard.keymap = [
    [KC.W,      KC.E,       KC.T,       KC.Y,       KC.NO,
     KC.S,      KC.G,       KC.J,       KC.L,       KC.NO,
     KC.Z,      KC.C,       KC.V,       KC.B,       KC.NO,
     KC.G,      KC.O,       KC.P,       LAYER2,     LAYER1,
     ],
    [KC.F1,         KC.E,           KC.LCMD(KC.J),          KC.LCMD(KC.LSFT(KC.EQUAL)),         KC.NO,
     KC.F6,         KC.G,           KC.LCMD(KC.LSFT(KC.J)), KC.LCMD(KC.MINUS),                  KC.NO,
     KC.Z,          KC.C,           KC.LCMD(KC.T),          KC.LCMD(KC.N0),                     KC.NO,
     KC.LSFT,       KC.LCTL,        KC.LALT,                KC.LCMD,                            KC.TRNS,
     ],
     [RGBV,         KC.NO,            KC.NO,         KC.NO,         KC.NO,
     RGBH,          KC.NO,           KC.NO,         KC.NO,         KC.NO,
     RGBS,          KC.NO,           KC.NO,         KC.NO,         KC.NO,
     KC.RGB_TOG,         KC.NO,           KC.NO,         KC.TRNS,         KC.TRNS,
     ],
]

keyboard.rgb_pixel_pin = board.GP28
keyboard.rgb_config['num_pixels'] = 7
keyboard.rgb_config['sat_default'] = 0
keyboard.rgb_config['val_default'] = 255
keyboard.rgb_config['val_step'] = 5
keyboard.rgb_config['hue_step'] = 5
keyboard.rgb_config['sat_step'] = 5


if __name__ == '__main__':    
    keyboard.ips.load_bitmap("L0.bmp")
    keyboard.go()    
    