class Wing:

    def flap(self):
        print(f"wing flaps")


class FeatheredWing(Wing):

    def flap(self):
        print("feathered", end=" ")
        super().flap()


class WebbedWing(Wing):

    def flap(self):
        print("webbed", end=" ")
        super().flap()
