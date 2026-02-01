from collections import OrderedDict

class RideSharingSystem:

    def __init__(self):
        self.rider_queue = OrderedDict()
        self.driver_queue = OrderedDict()

    def addRider(self, riderId: int) -> None:
        self.rider_queue[riderId] = None
        

    def addDriver(self, driverId: int) -> None:
        self.driver_queue[driverId] = None
        

    def matchDriverWithRider(self) -> List[int]:
        if len(self.rider_queue) == 0 or len(self.driver_queue) == 0:
            return [-1, -1]

        return [self.driver_queue.popitem(last=False)[0], self.rider_queue.popitem(last=False)[0]]
        

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rider_queue:
            del self.rider_queue[riderId]


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)