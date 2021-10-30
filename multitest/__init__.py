from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS
from struct import unpack
from time import sleep

class MultiTest:
    def __init__(self, com_port, device_number):
        self.port = None
        self.com_port = com_port
        self.number = device_number
    
    def _start(self):
        self.port = Serial(
            self.com_port,
            baudrate=9600,
            parity=PARITY_NONE,
            stopbits=STOPBITS_ONE,
            bytesize=EIGHTBITS
        )
    
    def _stop(self):
        self.port.close()
        sleep (0.1)
    
    def get_pX(self):
        self._start()
        request = [0x00, self.number, 0x04, 0x00, 0x10, 0x10, 0x30]
        request.append(sum(request) % 256)
        self.port.write(bytes(request))
        response = [int(i) for i in self.port.read(13)]
        self._stop()
        if len(response) == 13:
            return True, round(unpack('f', bytes(response[7:11]))[0], 3)
        return False, 0

    def get_E(self):
        self._start()
        request = [0x00, self.number, 0x04, 0x00, 0x10, 0x10, 0x10]
        request.append(sum(request) % 256)
        self.port.write(bytes(request))
        response = [int(i) for i in self.port.read(13)]
        self._stop()
        if len(response) == 13:
            return True, round(unpack('f', bytes(response[7:11]))[0], 1)
        return False, 0

    def get_T(self):
        self._start()
        request = [0x00, self.number, 0x04, 0x00, 0x10, 0x1A, 0x20]
        request.append(sum(request) % 256)
        self.port.write(bytes(request))
        response = [int(i) for i in self.port.read(13)]
        self._stop()
        if len(response) == 13:
            return True, round(unpack('f', bytes(response[7:11]))[0], 1)
        return False, 0
