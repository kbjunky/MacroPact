import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11)
    row_pins = (board.GP16, board.GP17, board.GP18, board.GP19)
    diode_orientation = DiodeOrientation.COLUMNS
    coord_mapping = []
    coord_mapping.extend(ic(0, x) for x in range(5))
    coord_mapping.extend(ic(1, x) for x in range(5))
    coord_mapping.extend(ic(2, x) for x in range(5))
    coord_mapping.extend(ic(3, x) for x in range(5))
    
    
    
    


