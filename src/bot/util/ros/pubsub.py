import rospy
from std_msgs.msg import (
    String
)

from bpyutils.util.string import get_random_str

MESSAGE_TYPES = {
    "string": {
        "type": String
    }
}

DEFAULT = {
    "rate":  10, # Hz
    "mtype": "string",
    "queue_size": 10
}

class PubSubNode:
    def __init__(self, name = None, rate = DEFAULT["rate"], mtype = DEFAULT["mtype"], 
        topic = None, *args, **kwargs):
        self._name  = name  or get_random_str()
        self._rate  = rate
        self._topic = topic or get_random_str()

        self._mtype = mtype

        anonymous   = kwargs.get("anonymous", True)

        rospy.init_node(name, anonymous = anonymous)

        rospy.loginfo("Initialized Node: %s." % name)

    def run(self):
        raise NotImplementedError("Please write your own run method.")

    @property
    def topic(self):
        return getattr(self, "_topic", None)

    @property
    def rate(self):
        rate = self._rate

        if not rate:
            rate = DEFAULT["rate"]

        rate = rospy.Rate(rate)

        return rate

    @property
    def message_type(self):
        mtype  = self._mtype
        config = MESSAGE_TYPES.get(mtype, "string")
        
        return config

class SubscriberNode(PubSubNode):
    def __init__(self, *args, **kwargs):
        self._super = super(SubscriberNode, self)
        self._super.__init__(*args, **kwargs)

        self._subscriber = rospy.Subscriber(self.topic, self.message_type["type"])

    def run(self):
        rospy.spin()

class PublisherNode(PubSubNode):
    def __init__(self, *args, **kwargs):
        queue_size  = kwargs.get("queue_size", DEFAULT["queue_size"])

        self._super = super(PublisherNode, self)
        self._super.__init__(*args, **kwargs)

        self._publisher  = rospy.Publisher(self.topic, self.message_type["type"],
            queue_size = queue_size)