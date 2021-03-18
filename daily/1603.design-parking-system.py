class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big_cap = big
        self.big_num = 0
        self.medium_cap = medium
        self.medium_num = 0
        self.small_cap = small
        self.small_num = 0


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big_num == self.big_cap:
                return False
            else:
                self.big_num += 1
        if carType == 2:
            if self.medium_num == self.medium_cap:
                return False
            else:
                self.medium_num += 1
        if carType == 3:
            if self.small_num == self.small_cap:
                return False
            else:
                self.small_num += 1
        return True