#include <Balboa32U4.h>
#include "Balboa.h"

#define BAUDRATE 115200

#define ASCII_LINE_FEED 10
#define ASCII_W         87

int inputByte = 0;
Balboa::Balboa balboa;

void setup () {
    Serial.begin(BAUDRATE);

    balboa.connect();
    
    balboa.balance();
}

void loop () {
    if ( Serial.available() > 0 ) {
        inputByte = Serial.read();

        switch (inputByte) {
            case ASCII_W:
                System.println("Move forward.");

                break;

            default:
                break;
        }
    }
}