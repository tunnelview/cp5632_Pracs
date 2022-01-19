from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness * self.price_per_km


    def get_fare(self):
        return self.flagfall + super().get_fare()

    def __str__(self):
            return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                        self.flagfall)
        #return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
          # I made a mistake keeping two brackets        #self.flagfall)
