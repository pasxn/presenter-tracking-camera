import platform
import serial

class GimbalController:
    def __init__(self):
        self.arch = platform.uname()[-1]
        if  self.arch != 'x86_64':
            scom = serial.Serial ("/dev/ttyS0", 9600)
        else:
            pass

        self.LEFT = -1
        self.MIDDLE = 0
        self.RIGHT = 1
        self.LEFTBOUNDERY = 120
        self.RIGHTBOUNDERY = 520    

    def calculateCommands(self, coordinates):
        if coordinates[0] < self.LEFTBOUNDERY and coordinates[2] > self.RIGHTBOUNDERY:
            return self.MIDDLE
        
        elif coordinates[0] < self.LEFTBOUNDERY:
            return self.LEFT

        elif coordinates[2] > self.RIGHTBOUNDERY:
            return self.RIGHT

        else:
            return self.MIDDLE

    def sendCommands(self, coordinates):
        if  self.arch == 'x86_64':
            try:
                print("Left: {}, Right: {}, Output: {}".format(coordinates[0], coordinates[2], self.calculateCommands(coordinates)))
            except:
                pass
        else:
            pass   