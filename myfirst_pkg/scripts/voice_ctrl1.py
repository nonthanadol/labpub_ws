#!/usr/bin/env python3
import speech_recognition as sr 
from gtts import gTTS 
import rospy
from geometry_msgs.msg import Twist 

while True:
    data = recordAudio()
    javis(data)


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source) 

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio, language = "en-US" )
        print("You said: ",data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

    def javis(data):
    	rospy.init_node('javis', anonymous=True)
    	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    	#rate = rospy.Rate(10)
    	velocity = Twist()

    	if "forward" in data:
    	     Velocity.linear.x = 0.15
    	     pub.publish(Velocity)