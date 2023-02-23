# bug with checking parameter for None using if parameter:
# use is not None if you need 0 value

def publish(data, area=None):
    if area is not None:
        kwargs['area'] = area
    lib.publish(data, **kwargs)

publish(data, area=0)

# lesson is located at
# https://github.com/AlexLitvino/hl_pyauto_17oct22_web
