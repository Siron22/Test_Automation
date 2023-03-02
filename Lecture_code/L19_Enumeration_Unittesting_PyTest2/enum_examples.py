status_codes = {
    'ok': 200,
    'not_found': 404
}

import enum

#@enum.unique
#class StatusCodes(enum.IntEnum):
class StatusCodes(enum.Enum):

    OK = 200
    NOT_FOUND = 404
    SUCCESSFUL = 200

def connect(is_connected):
    if is_connected:
        return StatusCodes.OK
    else:
        return StatusCodes.NOT_FOUND

if connect(True) == StatusCodes.OK:
    print("Connected")


print(StatusCodes.OK.name)
print(StatusCodes.OK.value)
print(StatusCodes.SUCCESSFUL.value)

print(StatusCodes.OK < StatusCodes.NOT_FOUND)