/* rosserial Subscriber Example */

#include <ros.h>
#include <std_msgs/Bool.h>

ros::NodeHandle  nh;

void messageCb( const std_msgs::Bool& msg){
  String ms= msg.data
  Serial.println(ms)
  digitalWrite(13, ms);   // set the pin state to the message data
}

ros::Subscriber<std_msgs::Bool> sub("/turtlebot_cmdVel", &messageCb );

void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
