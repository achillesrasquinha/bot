#include <Balboa32U4.h>

#include "Balboa.hpp"

#define BAUDRATE 115200

#define ASCII_LINE_FEED 10
#define ASCII_W         87

#define INITIAL_BALANCE_SETUP_SPEED        100
#define INITIAL_BALANCE_SETUP_SPEED_FACTOR 4

int inputByte = 0;
balboa::Balboa b;

void setup () {
    Serial.begin(BAUDRATE);

    b.connect();

    // move backward
    for ( u16t i = 1 ; i <= INITIAL_BALANCE_SETUP_SPEED ; ++i ) {
      b.set_speed(-INITIAL_BALANCE_SETUP_SPEED_FACTOR * i, -INITIAL_BALANCE_SETUP_SPEED_FACTOR * i);
      delay(10);
    }

    // move forward
    for ( u16t i = 1 ; i <= INITIAL_BALANCE_SETUP_SPEED ; ++i ) {
      b.set_speed(INITIAL_BALANCE_SETUP_SPEED_FACTOR * i, INITIAL_BALANCE_SETUP_SPEED_FACTOR * i);
      delay(10);
    }

    sdelay(1);

    b.set_speed(0, 0);
}

void loop () {
    if ( Serial.available() > 0 ) {
        inputByte = Serial.read();

        switch (inputByte) {
            case ASCII_W:
                Serial.println("Move forward.");

                break;

            default:
                break;
        }
    }
        
    b.balance();

    b.gyro();
}
