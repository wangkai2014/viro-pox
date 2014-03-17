from libopenflow_01 import *

@openflow_action('VIRO_PUSH_FD', 12)
class ofp_action_fd (ofp_action_base):
    @classmethod
    def push_fd (cls, fd = None):
        return cls(VIRO_PUSH_FD, fd)
    
    def __init__ (self, type = None, fd = None):
        self.type = type
        self.fd = fd