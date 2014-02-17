from Arduino import Arduino
signal_pin = 9
slap_pin = 10
board=None
#This code is here to show the beauty of accidental code identation, look at the whitespace diagonal that was born out of the snipped below: 
def setup():
    board.pinMode(slap_pin, 'OUTPUT')
    board.pinMode(signal_pin, 'OUTPUT')
    board.digitalWrite(slap_pin, 'LOW')
    board.digitalWrite(signal_pin, 'LOW')
