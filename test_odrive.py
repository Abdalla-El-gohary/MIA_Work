import odrive
import time 
from odrive.enums import *
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension


inp_pos=Float32MultiArray
inp_pos=[0,0,0,0]  #for input position

curr_pos=Float32MultiArray
curr_pos=[0,0,0,0] #for current position



def callback(data):  #fun of subscriber
    rospy.loginfo(rospy.get_caller_id() + "  speeds are %f",data.data)
    inp_pos[0]=data.data[0]
    inp_pos[1]=data.data[1]
    inp_pos[2]=data.data[2]
    inp_pos[3]=data.data[3]








if __name__ == '__main__':
    rospy.init_node("odrive",anonymous=True)
    pub=rospy.Publisher("topic",Float32MultiArray,queue_size=10)
    sub=rospy.Subscriber("speeds",Float32MultiArray,callback)
    rate = rospy.Rate(10) # 10hz

    odrv0 = odrive.find_any()
    odrv1 = odrive.find_any()  #for the other odriver

    odrv0.axis0.encoder.config.cpr = 400000 #set the cpr value of the encoder
    odrv0.axis1.encoder.config.cpr = 400000 #set the cpr value of the encoder
    odrv1.axis0.encoder.config.cpr = 400000 #set the cpr value of the encoder
    odrv1.axis1.encoder.config.cpr = 400000 #set the cpr value of the encoder


    odrv0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE  #Start the calibratrion sequence
    odrv0.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE  #Start the calibratrion sequence
    odrv1.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE  #Start the calibratrion sequence
    odrv1.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE  #Start the calibratrion sequence


    while odrv0.axis0.current_state != AXIS_STATE_IDLE:  
        time.sleep(0.1)
    while odrv0.axis1.current_state != AXIS_STATE_IDLE:  
        time.sleep(0.1)
    while odrv1.axis0.current_state != AXIS_STATE_IDLE:  
        time.sleep(0.1)
    while odrv1.axis1.current_state != AXIS_STATE_IDLE:  
        time.sleep(0.1)


    odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL  #set the state to closed loop
    odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL  #set the state to closed loop
    odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL  #set the state to closed loop
    odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL  #set the state to closed loop


    while not rospy.is_shutdown():
        odrv0.axis0.controller.input_pos = inp_pos[0]  #units are in turns
        odrv0.axis1.controller.input_pos = inp_pos[1]  #units are in turns
        odrv1.axis0.controller.input_pos = inp_pos[2]  #units are in turns
        odrv1.axis1.controller.input_pos = inp_pos[3]  #units are in turns

        curr_pos[0] = odrv0.axis0.encoder.pos_estimate
        curr_pos[1] = odrv0.axis1.encoder.pos_estimate
        curr_pos[2] = odrv1.axis0.encoder.pos_estimate
        curr_pos[3] = odrv1.axis1.encoder.pos_estimate

        pub.publish(curr_pos)

        rospy.spin()
        rate.sleep()

