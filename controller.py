import pyfirmata

comport = 'COM9'
board = pyfirmata.Arduino(comport)

led_pins = [
    board.get_pin('d:8:o'),
    board.get_pin('d:9:o'),
    board.get_pin('d:10:o'),
    board.get_pin('d:11:o'),
    board.get_pin('d:12:o'),
    board.get_pin('d:7:o'),   
    board.get_pin('d:6:o'), 
    board.get_pin('d:5:o'), 
    board.get_pin('d:4:o'), 
    board.get_pin('d:3:o'),  
]

def led(fingerUp):
    for i in range(10):
        led_pins[i].write(fingerUp[i])
