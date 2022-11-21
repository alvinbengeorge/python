# proximity sensor arduino pyfirmata
import pyfirmata

arduinoBoard = pyfirmata.Board('COM3')

iterator = pyfirmata.util.Iterator(arduinoBoard)
iterator.start()

component = arduinoBoard.get_pin('')