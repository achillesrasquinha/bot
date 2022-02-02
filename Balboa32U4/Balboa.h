#include <Wire.h>
#include <Balboa32U4.h>
#include "Logger.h"

namespace Balboa {
    class Balboa {
        public:
            void connect () {
                
            }

            void balance () {
                Wire.begin();

                if ( !imu.init() ) {
                    Serial.println("Failed to detect and initialize IMU.");
                } else {
                    imu.enableDefault();
                }
            }
    };
}