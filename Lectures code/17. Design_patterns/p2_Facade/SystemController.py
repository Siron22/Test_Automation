from BLEController import BLEController
from PCBController import PCBController
from WiFiController import WiFiController


class SystemController:

    def __init__(self):
        self.ble_controller = BLEController()
        self.wifi_controller = WiFiController()
        self.pcb_controller = PCBController()

    def enable_communication(self):
        self.ble_controller.enable_communication()
        self.wifi_controller.enable_communication()

    def disable_communication(self):
        self.ble_controller.disable_communication()
        self.wifi_controller.disable_communication()

    def init_system(self):
        self.pcb_controller.power_on()
        self.enable_communication()

    def teardown_system(self):
        self.disable_communication()
        self.pcb_controller.power_off()