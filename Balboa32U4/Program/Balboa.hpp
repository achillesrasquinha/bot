#ifndef BALBOA_HPP
#define BALBOA_HPP

#include <Wire.h>
#include <LSM6.h>
#include <Balboa32U4.h>

#include "Constant.hpp"
#include "Util.hpp"
#include "Logger.hpp"

#define DELAY 1

#define LED_CONNECTED 0b010

namespace balboa {
    class Balboa {
        public:
            LSM6 imu;
            Balboa32U4Buzzer buzzer;
            Balboa32U4Motors motors;

            Balboa();

            void connect () {
                Serial.println("Attempting to connect Balboa...");
                
                init_imu();

                setLED(LED_CONNECTED);
            }

            void setLED (u8t bits) {
                u8t bit = bits & 1;
                
                ledRed(bit);
            }

            void init_imu () {
                Wire.begin();

                if ( !imu.init() ) {
                    while (true) {
                        Serial.println("Failed to detect and initialize IMU.");
                        sdelay(DELAY);
                    }
                }
                
                imu.enableDefault();
                imu.writeReg(LSM6::CTRL2_G, 0b1011000); // 208 Hz, 1000 deg/s

                // Wait for IMU to stabilize...
                sdelay(DELAY);
                
                Serial.println("IMU enabled.");
            }
            
            void balance () {
                // Serial.println("Attempting to balance the Balboa...");
            }

            // The current gryoscope reading.
            void gyro () {
                imu.read();
            }

            void set_speed (u8t left, u8t right) {
                Serial.print("Setting motor speed: (");
                Serial.print(left); Serial.print(","); Serial.print(right); Serial.println(")");

                motors.setSpeeds(left, right);
            }
    };

    Balboa::Balboa () {

    }
}

#endif
