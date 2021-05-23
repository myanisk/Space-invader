import params

def menu():
    while True:
        vt100.move(uart,0, 0)
        uart.write("*********************************************MENU***********************************************************")
        vt100.move(uart,0, 2)
        uart.write("*******************************************1.EASY***********************************************************")
        vt100.move(uart,0, 6)
        uart.write("*******************************************2.NORMAL*********************************************************")
        vt100.move(uart,0, 10)
        uart.write("*******************************************3.HARD***********************************************************")
        vt100.move(uart,0, 14)
        uart.write("************************************************************************************************************")
      
        choice = 3
        string error;
        switch (choice) {
            case 1:  space_inv_easy();
                     break;
            case 2:  space_inv_normal();
                     break;
            case 3:  space_inv_hard();
                     break;
            default: error = "ERROR";
                     break;
        }
        System.out.println(error);
}
