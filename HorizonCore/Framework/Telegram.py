import datetime
import hashlib

from HorizonCore.Framework.ComparableMixin import ComparableMixin


class Telegram(ComparableMixin):
    """
    These telegrams will be stored in a priority queue. Therefore the >
    operator needs to be overloaded so that the PQ can sort the telegrams
    by time priority. Note how the times must be smaller than
    SmallestDelay apart before two Telegrams are considered unique.
    """
    SmallestDelay = datetime.timedelta(milliseconds=500)

    def __init__(self, dispatchTime, senderId, receiverId, message, extraInfo):
        self._dispatchTime = dispatchTime
        self._senderId = senderId
        self._receiverId = receiverId
        self._message = message
        self._extraInfo = extraInfo

    @property
    def DispatchTime(self):
        """
        Messages can be dispatched immediately or delayed for a specified amount
        of time. If a delay is necessary this field is stamped with the time 
        the message should be dispatched.
        """
        return self._dispatchTime

    @DispatchTime.setter
    def DispatchTime(self, value):
        self._dispatchTime = value

    @property
    def SenderId(self):
        """The entity that sent this telegram"""
        return self._senderId

    @property
    def ReceiverId(self):
        """The entity that is to receive this telegram"""
        return self._receiverId

    @property
    def Message(self):
        """The message itself. These are all enumerated in the file MessageTypes"""
        return self._message

    @property
    def ExtraInfo(self):
        """Any additional information that may accompany the message"""
        return self._extraInfo

    def __repr__(self):
        return "Time: {}  Sender: {}   Receiver: {}   Msg: {}".format(
            self.DispatchTime, self.SenderId, self.ReceiverId, self.Message)

    def __eq__(self, other):
        return abs(self.DispatchTime - other.DispatchTime) < self.SmallestDelay and \
            self.SenderId == other.SenderId and \
            self.ReceiverId == other.ReceiverId and \
            self.Message == other.Message

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        hashObject = hashlib.md5(self.__repr__().encode())
        return int(hashObject.hexdigest(), 16)

    def _compareKey(self):
        return self._dispatchTime
