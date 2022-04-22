class GimbalController:
    def __init__(self):
        self.LEFT = -1
        self.MIDDLE = 0
        self.RIGHT = 1
        self.LEFTBOUNDERY = 120
        self.RIGHTBOUNDERY = 520    

    def calculateCommands(self, coordinates):
        if coordinates[0] < self.LEFTBOUNDERY:
            return self.LEFT

        elif coordinates[2] > self.LEFTBOUNDERY:
            return self.RIGHT
        
        else:
            return self.MIDDLE

    def sendCommands(self, coordinates):
        print("Left: {}, Right: {}, Output: {}".format(coordinates[0], coordinates[2], self.calculateCommands(coordinates)))