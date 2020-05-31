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