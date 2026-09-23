import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3) 
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7)

encoder_handler.pins = ((board.D8, board.D9, None, False),) 

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [
        KC.N7,  KC.N8,  KC.N9,  KC.NO,         
        KC.N4,  KC.N5,  KC.N6,  KC.SLSH,    
        KC.N1,  KC.N2,  KC.N3,  KC.ASTR,   
        KC.N0,  KC.DOT, KC.ENT, KC.MO(1)
    ],
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, 
        KC.HOME, KC.UP,   KC.END,  KC.MINUS,
        KC.LEFT, KC.DOWN, KC.RGHT, KC.PLUS,     
        KC.BSPC, KC.TRNS, KC.TRNS, KC.TRNS 
    ]
]

encoder_handler.map = [
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),),

    ((KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK),)
]

if __name__ == '__main__':
    keyboard.go()
