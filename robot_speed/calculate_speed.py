#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

WHEEL_RADIUS = 12.5 / 100

class SpeedCalulator(Node):
    def __init__(self):
        super().__init__("speed_calculate_node")
        self.sub = self.create_subscription(Float32,"rpm",self.calculate_speed_callback,10)
        self.pub = self.create_publisher(Float32,"speed",10)

    def calculate_speed_callback(self,rpm_msg):
        speed = (rpm_msg.data * WHEEL_RADIUS * 2 * 3.14159) / 60
        speed_msg = Float32()
        speed_msg.data = float(speed)
        self.pub.publish(speed_msg)
        print(f"Robot running at speed of {speed}")

def main(args=None):
    rclpy.init()
    speed_cal_node = SpeedCalulator()
    print("waiting for publisher to publish rpm data")
    try:
        rclpy.spin(speed_cal_node)
    except KeyboardInterrupt:
        print('Terminating Speed calc Node...')
        speed_cal_node.destroy_node()

if __name__=='__main__':
    main()