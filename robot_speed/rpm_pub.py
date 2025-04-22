#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from std_msgs.msg import Float32
import random



class rpmPublisher(Node):
    def __init__(self):
        super().__init__("rpm_publisher_node")
        self.pub = self.create_publisher(Float32,"rpm",10)
        self.timer = self.create_timer(0.5,self.publish_rpm)

    def publish_rpm(self):
        RPM = random.randint(5,30)
        msg = Float32()
        msg.data = float(RPM)
        self.pub.publish(msg)


def main(args=None):
    rclpy.init()
    rpm_pub_node = rpmPublisher()
    print("rpm publisher node Running...")

    try:
        rclpy.spin(rpm_pub_node)
    except KeyboardInterrupt:
        print("Terminating Node...")
        rpm_pub_node.destroy_node()



if __name__=="__main__":
    main()