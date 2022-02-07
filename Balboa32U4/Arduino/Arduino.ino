#include "CArduino.hpp"
#include "Util/Time.h"
#include "Constant.h"

Arduino::Arduino uno;

int8_t inputs  [] = {2};
int8_t outputs [] = {13};

int8_t inp_len = (int8_t) len((int) inputs);
int8_t out_len = (int8_t) len((int) outputs);

void setup () {
    uno.connect(inputs, outputs);
}

void loop () {
    while (true) {
      if ( Serial.available() > 0 ) {
        uno.read(inputs, outputs);
      }
    }
    
    
//    sdelay(DELAY);

//    for ( int8_t i = 0 ; i < inp_len ; ++i ) {
//      int8_t input = inputs[i];
//      int8_t state = *(states + i);
//
//      char *state_str = state == 0 ? "OFF" : "ON";
//
//      Serial.print(input);
//      Serial.print(" (button): (state) ");
//      Serial.print(state_str);
//      Serial.print("\n");
//
//      sdelay(DELAY);
//    }
}
