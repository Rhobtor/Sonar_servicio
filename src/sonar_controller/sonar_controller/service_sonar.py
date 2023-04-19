import rclpy
from rclpy.node import Node
from custom_interfaces.srv import sonar

class HeadServicie(Node):
    def __init__(self):
        super().__init__("sonar_service")
        self.working=False
        self.service=self.create_service(
            sonar,
            "sonar",
            self.sonar_callback
        )
    

    def add_distance_callback(self,request,response):
        self.working = Ping1D()
        self.working.connect_serial("/dev/ttyUSB0", 115200)    #cambiar el usb si es necesario
        if request.value:
            if self.working:
                self.get_logger().info("sonar already working")
                response.success=False
                return response #we are already working
            self.recording=True
            self.camera_recording_thread.start()
        else:
            if not self.recording: #we arent working
                response.success=False
                self.get_logger().info("camera wasnt recording")
                return response
            self.get_logger().info("stop working")
            self.recording=False
        return response

def main(args=None):
    rclpy.init(args=args)
    move_service= HeadServicie()
    rclpy.spin(move_service)
    rclpy.shutdown()
if __name__=="__main__":
    main()