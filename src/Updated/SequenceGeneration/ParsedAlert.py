from datetime import datetime

from src.Updated.MicroAttackStage import MicroAttackStage


class ParsedAlert(object):
    def __init__(self, time_delta_seconds: float, src_ip: str, src_port: int, dest_ip: str,
                 dest_port: int, signature: str, category: str, host: str, timestamp: datetime,
                 mcat: MicroAttackStage):
        """
        Represents a basic parsed alert.
        :param time_delta_seconds: Number of seconds since the last alert
        :param src_ip:
        :param src_port:
        :param dest_ip:
        :param dest_port:
        :param signature: label given by Suricata
        :param category:
        :param host: host name given to the source (different from IP)
        :param timestamp:
        :param mcat: mapping from signature to Micro Attack Stage
        """
        self.time_delta_seconds = time_delta_seconds
        self.src_ip = src_ip
        self.src_port = src_port
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.signature = signature
        self.category = category
        self.host = host
        self.timestamp = timestamp
        self.mcat = mcat

    def __str__(self):
        return f"ParsedAlert: {self.src_ip}:{self.src_port} -> {self.dest_ip}:{self.dest_port}, {self.mcat}, {self.timestamp}"

# Reference: in the base, alerts are represented as a tuple:
# (DIFF, srcip, srcport, dstip, dstport, sig, cat, host, dt, mcat)
#  0     1      2        3      4        5    6    7     8   9
