from abc import ABC, abstractmethod


class Socket(ABC):
    @abstractmethod
    def voltage(self):
        pass

    
    
    
    
class EuropeanSocket(ABC):
    def voltage(self):
        return 230

class AmericanSocket(ABC):
    def voltage(self):
        return 120

class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        if isinstance(self.socket, EuropeanSocket):
            return self.socket.voltage() / 2
        return self.socket.voltage()

# Usage
euro_socket = EuropeanSocket()
adapter = SocketAdapter(euro_socket)
print(adapter.voltage())  # Output: 115.0
