import argparse

from client import NTPClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser("python main.py", description="Simple NTP client.")
    parser.add_argument("-a", "--address", help="NTP server address", type=str, default="pool.ntp.org")
    parser.add_argument("-p", "--port", help="NTP server port", type=int, default=123)
    parser.add_argument("-w", "--wait", help="Server response waiting time (in seconds)", type=int, default=123)

    args = parser.parse_args()

    client_ = NTPClient(args.address, args.port, args.wait)
    print("\nTIME: {0}\n \nRESPONSE_INFO:\n{1}".format(client_.get_time()[0], client_.get_time()[1]))