import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# import oled_control
from oled_display.oled_control import OLEDController,time

oled = OLEDController()

class OledDisplayNode(Node):
    def __init__(self):
        super().__init__('oled_display_node')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)
        self.subscription  # Prevent unused variable warning
        self.current_state = None

    def cmd_vel_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        if angular_z > 0:
            new_state = 'left'
        elif angular_z < 0:
            new_state = 'right'
        elif linear_x > 0:
            new_state = 'up'
        elif linear_x < 0:
            new_state = 'down'
        else:
            new_state = 'stop'

        if new_state != self.current_state:
            self.current_state = new_state
            self.update_display()
    
    def update_display(self):
        if self.current_state == 'left':
            # self.get_logger().info('Turning left')
            oled.lefteye()
        elif self.current_state == 'right':
            # self.get_logger().info('Turning right')
            oled.righteye()
        elif self.current_state == 'up':
            # self.get_logger().info('Moving forward')
            oled.normal()
        elif self.current_state == 'down':
            # self.get_logger().info('Moving backward')
            oled.downeye()
        elif self.current_state == 'stop':
            # self.get_logger().info('Stopping')
            oled.display_text('Huydeptrai')

def main(args=None):
    rclpy.init(args=args)
    oled_display_node = OledDisplayNode()
    while rclpy.ok():
        rclpy.spin_once(oled_display_node)
        time.sleep(0.01)
    oled_display_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
