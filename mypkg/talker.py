import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0
def cb():
    global n
    msg = Person()         
    msg.name = "YunosukeKameoka"  #msgファイルに書いた「name」
    msg.age = 20            #msgファイルに書いた「age」
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
