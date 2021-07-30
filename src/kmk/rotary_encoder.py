#Based on code from https://github.com/adafruit/circuitpython/blob/master/ports/atmel-samd/common-hal/rotaryio/IncrementalEncoder.c#L121

import digitalio
import board


class Encoder:
    prev_state = 0
    q_count = 0
    pad_a = None
    pad_b = None
    onRotate = None

    def __init__(self, pad_a, pad_b, onRotate):
        self.pad_a = pad_a
        self.pad_b = pad_b
        self.onRotate = onRotate

    def read(self):
        t = (0, -1, 1, 'BAD', 1, 0, 'BAD', -1, -1, 'BAD', 0, 1, 'BAD', 1, -1, 0)
        pada = digitalio.DigitalInOut(self.pad_a)
        pada.direction = digitalio.Direction.INPUT
        pada.pull = digitalio.Pull.UP

        padb = digitalio.DigitalInOut(self.pad_b)
        padb.direction = digitalio.Direction.INPUT
        padb.pull = digitalio.Pull.UP

        pav = 1
        pbv = 1
        if(not pada.value):
            pav = 0
        if(not padb.value):
            pbv = 0
         
        self.prev_state = (self.prev_state & 0x3) << 2 | pav << 1 | pbv
        q = t[self.prev_state]
        if(q != 'BAD'):       
            self.q_count += q
            if(self.q_count >= 4):
                self.onRotate(1)
                self.q_count = 0               
            if(self.q_count <= -4):
                self.onRotate(-1)
                self.q_count = 0

        pada.deinit()
        padb.deinit()
