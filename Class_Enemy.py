import params


class Enemy():
    def __init__(self,x,y,dir):
        self.x = x
        self.y = y
        self.dir = dir
        vt100.move(uart, (self.x)-4, self.y)
        uart.write("0X0")
    def movement(self):
        if (self.x>=MAX_WIDTH):
            self.dir = -1
            self.x = self.x + self.dir
            vt100.move(uart,self.x, self.y)
            uart.write("	")
            self.y = self.y + 2
            vt100.move(uart,self.x, self.y)
            uart.write("0X0")
            if (self.y >= 5):
            vt100.move(uart,MAX_HEIGHT/2, MAX_WIDTH/2)
            uart.write("GAME OVER")
        elif (self.x <=5):
            self.dir = +1
            self.x = self.x + self.dir
            vt100.move(uart,self.x, self.y)
            uart.write("	")
            self.y = self.y + 2
            vt100.move(uart,self.x, self.y)
            uart.write("0X0")
            if (self.y >= 5):
            vt100.move(uart,MAX_HEIGHT/2, MAX_WIDTH/2)
            uart.write("GAME OVER")
        else:
            self.x = self.x + self.dir
            vt100.move(uart,self.x, self.y)
            uart.write("0X0")


def initShip(ship):
    for i in range(5):
        ship[i] = Enemy(i*9 + 7*(i+1), 4, 1)


def enemy():
    ship = [0,0,0,0,0]
    initShip(ship)
    
    while true:
        for i in range(5):
            ship[i].movement()
            pyb.delay(20)


