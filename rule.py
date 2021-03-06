class Rule:

    def __init__(
            self,
            src, 
            dst, 
            trans_proto, 
            app_proto, 
            expiration,
            delay):
        self.src = src
        self.dst = dst
        self.trans_proto = trans_proto
        self.app_proto = app_proto
        self.expiration = expiration
        self.delay = delay

    def __str__(self):
        return  "src:" + self.src + \
                " dst:" + self.dst + \
                " trans_proto:" + self.trans_proto + \
                " app_proto:" + self.app_proto + \
                " expiration:" + self.expiration + "s" + \
                " delay:" + str(self.delay) + "s"
