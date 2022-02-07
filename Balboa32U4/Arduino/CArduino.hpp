#include <Arduino.h>
#include "Util/Array.h"

#define BAUDRATE 115200

namespace Arduino {
    class Arduino {
        public:
            void connect (int8_t *inputs, int8_t *outputs) {
                Serial.begin(BAUDRATE);
                
                setup(inputs, outputs);

                Serial.println("Connected.");
            }

            void setup (int8_t *inputs, int8_t *outputs) {
                int8_t inp_len = (int8_t) len((int) inputs);
                int8_t out_len = (int8_t) len((int) outputs);
                
                for ( int8_t i = 0 ; i < inp_len ; ++i ) {
                  int8_t pin = inputs[i];
                  pinMode(pin, INPUT_PULLUP);
                }

                for ( int8_t i = 0 ; i < out_len ; ++i ) {
                  int8_t pin = outputs[i];
                  pinMode(pin, OUTPUT);
                }
            }

            int8_t* read (int8_t *inputs, int8_t *outputs) {
                int8_t inp_len = (int8_t) len((int) inputs);
                
                int8_t states [inp_len];
                
                for ( int8_t i = 0 ; i < inp_len ; ++i ) {
                  int8_t inp_pin = inputs[i];
                  int8_t out_pin = outputs[i];
                  
                  states[i] = digitalRead(inp_pin);

                  if ( states[i] == LOW ) {
                    digitalWrite(out_pin, HIGH);
                  } else {
                    digitalWrite(out_pin, LOW);
                  }

                  char *state_str = states[i] == 0 ? "ON" : "OFF";
              
                  Serial.print(inp_pin);
                  Serial.print(" (button): (state) ");
                  Serial.print(state_str);
                  Serial.print("\n");
                }

                return states;
            }
    };
}
