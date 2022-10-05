class WingsMixin:

    def fly(self):
        print(f"{self.name} uses wings to fly")


class TwoWingsMixin(WingsMixin):
    pass


class ManyWingsMixin(WingsMixin):
    pass


class FeatheredWingsMixin(TwoWingsMixin):
    pass


class WebbedWingsMixin(TwoWingsMixin):
    pass
