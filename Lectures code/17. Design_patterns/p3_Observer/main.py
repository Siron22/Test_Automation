from sensor import Sensor
from observers import MobileApp, WebPortal, AirConditioner

mobile_app = MobileApp()
web_portal = WebPortal()
air_conditioner = AirConditioner(17, 23)

sensor_ = Sensor()

sensor_.subscribe(mobile_app)
sensor_.subscribe(web_portal)
sensor_.subscribe(air_conditioner)

sensor_.notify_all()
print()
sensor_.notify(mobile_app)
print()
sensor_.unsubscribe(web_portal)
sensor_.notify_all()