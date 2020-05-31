import struct 

class NTPPacket:
    _FORMAT = "!B B b b 11I"

    def __init__(self, version_number=2, mode=3, transmit=0):
        # Necessary of enter leap second (2 bits)
        self.leap_indicator = 0
        # Version of protocol (3 bits)
        self.version_number = version_number
        # Mode of sender (3 bits)
        self.mode = mode
        # The level of "layering" reading time (1 byte)
        self.stratum = 0
        # Interval between requests (1 byte)
        self.pool = 0
        # Precision (log2) (1 byte)
        self.precision = 0
        # Interval for the clock reach NTP server (4 bytes)
        self.root_delay = 0
        # Scatter the clock NTP-server (4 bytes)
        self.root_dispersion = 0
        # Indicator of clocks (4 bytes)
        self.ref_id = 0
        # Last update time on server (8 bytes)
        self.reference = 0
        # Time of sending packet from local machine (8 bytes)
        self.originate = 0
        # Time of receipt on server (8 bytes)
        self.receive = 0
        # Time of sending answer from server (8 bytes)
        self.transmit = transmit

    @staticmethod
    def get_fraction(number, precision):
        return int((number - int(number)) * 2 ** precision)

    # Pack message to send and receive
    def pack(self):
        package = struct.pack(NTPPacket._FORMAT,
                (self.leap_indicator << 6) + 
                    (self.version_number << 3) + self.mode,
                self.stratum,
                self.pool,
                self.precision,
                int(self.root_delay) + get_fraction(self.root_delay, 16),
                int(self.root_dispersion) + 
                    get_fraction(self.root_dispersion, 16),
                self.ref_id,
                int(self.reference),
                get_fraction(self.reference, 32),
                int(self.originate),
                get_fraction(self.originate, 32),
                int(self.receive),
                get_fraction(self.receive, 32),
                int(self.transmit),
                get_fraction(self.transmit, 32))

        return package

