import socket
import datetime
import time

from package import NTPPacket

class NTPClient:
    
    # Time difference between 1970 and 1900, seconds
    FORMAT_DIFF = (datetime.date(1970, 1, 1) - datetime.date(1900, 1, 1)).days * 24 * 3600


    def __init__(self, ntp_server, server_port, waiting_time=5):
        self.server = ntp_server
        self.port = server_port
        self.WAITING_TIME = waiting_time


    def get_time(self):
        cur_time = time.time() + self.FORMAT_DIFF
        request = NTPPacket(version_number=2, mode=3, transmit=cur_time)

        response = NTPPacket()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(self.WAITING_TIME)
            sock.sendto(request.pack(), (self.server, self.port))

            raw_response = sock.recv(48)
            time_of_arrival = time.time() + self.FORMAT_DIFF
            response.unpack(raw_response)

        delta = self.calculate_delta(response.originate, response.transmit, response.receive,
                                     time_of_arrival)

        return datetime.datetime.fromtimestamp(time.time() + delta).strftime("%c")


    @staticmethod
    def calculate_delta(original, transmitted, received, arrived):
        transmission_time = ((arrived - original) - (transmitted - received)) / 2
        total_delta = received - original - transmission_time
        return total_delta