from p2pool.bitcoin import networks

PARENT = networks.nets['happyuc']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9338
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9527
BOOTSTRAP_ADDRS = '72.11.140.162 218.253.193.226'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-huc'
VERSION_CHECK = lambda v: None if 100400 <= v else 'HappyUC version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
# SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
