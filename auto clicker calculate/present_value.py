class hand:
    power = 1
    likelyhood = 0.4975

class uppgrades(hand):
    level = 0
    price = None
    effekt = None
    present_value = None

    def __init__(self, level, price, effekt) -> None:
        self.level = level
        self.price = price
        self.effekt = effekt
        self.power = hand.power + effekt*level

    def find_present_value(self, time):
        production_ps = self.power*self.likelyhood/2
        time_until_uppgrade = self.price/production_ps
        self.present_value = production_ps*time + time/time_until_uppgrade*self.effekt - time/time_until_uppgrade*self.price

stronger_arms = uppgrades(11, 58, 1)
greater_coin = uppgrades(0, 125, 5)

stronger_arms.find_present_value(10)
greater_coin.find_present_value(10)

print(stronger_arms.present_value, stronger_arms.power)
print(greater_coin.present_value, greater_coin.power)