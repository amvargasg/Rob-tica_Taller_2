//www.elegoo.com
//2016.09.12

//define logic control output pin/
int in1=9;
int in2=8;
int in3=7;
int in4=6;
//define channel enable output pins/
int ENA=10;
int ENB=5;
//define forward function/
void _mBack()
{ 
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB,HIGH);
  digitalWrite(in1,LOW);//digital output
  digitalWrite(in2,HIGH);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  Serial.println("Back");
}
//define back function/
void _mForward()
{
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB,HIGH);
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  Serial.println("Forward");
}
//define left function/
void _mright()
{
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB,HIGH);
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  Serial.println("Right");
}
//define right function/
void _mleft()
{
  digitalWrite(ENA,HIGH);
  digitalWrite(ENB,HIGH);
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  Serial.println("Left");
}
//define stop function/
void _mStop()
{
  digitalWrite(ENA,LOW);
  digitalWrite(ENB,LOW);
  Serial.println("Stop!");
} 
//put your setup code here, to run once/
void setup() {
 Serial.begin(115200); //Open the serial port and set the baud rate to 9600
//Set the defined pins to the output/
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
}
//put your main code here, to run repeatedly/
void loop() {
  if (Serial.available()>0){
    String data = Serial.readStringUntil('.');
    Serial.print("");
    Serial.println(data);
    Serial.println(data == "w");
    Serial.println(data.equals("w"));
    if (data.equals("w")) {
      Serial.print("adelante");
      _mForward();
      //delay(1000);
      }
    else if (data == "s") {
      Serial.print("atras");
      _mBack();
      //delay(1000);
      }
    else if(data == "d") {
      Serial.print("derecha");
      _mright();
      //delay(1000);
      }
    else if(data == "a") {
      Serial.print("izquierda");
      _mleft();
      //delay(1000);
      }
    else if(data == "n"){
      Serial.print("ningun if");
      _mStop();
      }  
    }
  

}
