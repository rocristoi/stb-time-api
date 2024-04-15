
/* Include Libraries, download them! */
#include "DigitLedDisplay.h"
#include "ESP8266WiFi.h"
#include <ESP8266HTTPClient.h>
#include <WiFiClientSecureBearSSL.h>
#include <ArduinoJson.h>


/* ESP Pin to Display Pin
   D7 to DIN,
   D5 to CS,
   D6 to CLK */
DigitLedDisplay ld = DigitLedDisplay(D7, D5, D6);

const char* ssid = "starOnGithub"; // Write here your router's SSID
const char* password = "starOnGithub"; // Write here your router's passward

WiFiClient wifiClient;

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);

  // while wifi not connected yet, print '.'
  // then after it connected, get out of the loop
  while (WiFi.status() != WL_CONNECTED) {
     delay(500);
  }
  /* Set the brightness min:1, max:15 */
  ld.setBright(10);

  /* Set the digit count */
  ld.setDigitLimit(8);
  Serial.println("");
  Serial.println("WiFi connected");
  // Print the IP address
  Serial.println(WiFi.localIP());

}

void loop() {


  /* Prints data to the display */
  ld.printDigit(getTime("1"), 2);
  ld.printDigit(getTime("2"), 6);
  //ld.printDigit(getTime("3"), 7);
  delay(60000);
  ld.clear();
  

}

int getTime(String numar) {
  int timp = 0;
   if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status

    HTTPClient http; 
 
    http.begin(wifiClient, "http://yourip:5000/api/time/" + numar);  //change to API address
    int httpCode = http.GET();                                
 
    if (httpCode > 0) {
 
      String payload = http.getString();  
      if(payload == "m")
       {
        return 20;
       } else {
        timp = payload.toInt();
       }
      

    }
 
    http.end();   //Close connection
 
  }
  return timp;
  delay(30000);    //Send a request every 30 seconds

}
