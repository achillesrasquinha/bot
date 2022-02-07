#include <Wire.h>
#include <LSM6.h>
#include <Balboa32U4.h>

#include "Util.h"
#include "Logger.h"

#define DELAY 1

#define LED_CONNECTED 0b001

namespace Balboa {
    class Balboa {
        public:
            LSM6 imu;
            Balboa32U4Buzzer buzzer;
            Balboa32U4Motors motors;

            Balboa();

            void connect () {
                init_imu();

                setLED(LED_CONNECTED);
            }

            void setLED (int bits) {
                // TODO
            }

            void init_imu () {
                Wire.begin();

                if ( !imu.init() ) {
                    while (true) {
                        Serial.println("Failed to detect and initialize IMU.");
                        sdelay(DELAY);
                    }
                } else {
                    imu.enableDefault();
                    imu.writeReg(LSM6::CTRL2_G, 0b1011000); // 208 Hz, 1000 deg/s

                    sdelay(DELAY);
                }
            }
            
            void balance () {
                
            }

            // The current gryoscope reading.
            void gyro () {
                imu.read();
                
            }
    };

    Balboa::Balboa () {

    }
}