import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
     global node
     node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cb, 10)

rclpy.spin(node)

