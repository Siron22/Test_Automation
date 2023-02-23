from SystemController import SystemController

system_controller = SystemController()

system_controller.init_system()

system_controller.disable_communication()
print("Test without communication")
system_controller.enable_communication()
print("Test with communication")
system_controller.teardown_system()
