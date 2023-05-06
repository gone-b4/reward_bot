import csv
import random

class SpinToWin:
    def __init__(self)-> None:
        self.rewards = list()
        self.weights = tuple()
        self.num_items = int()

    def loadWheel(self, item_file: str)-> None:
        total_weight = int()
        weights = list()

        with open(item_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                reward, weight = row[0], row[1]

                try:
                    weight = float(weight)
                    total_weight += weight
                except ValueError:
                    raise ValueError("Weight must be number")

                self.rewards.append(reward)
                weights.append(weight)

        if (total_weight != 100):
            raise ValueError("Total weight must equal 100")

        self.weights = tuple(weights)
        self.num_items = len(self.rewards)

    def spin(self)-> list:
        return "".join(random.choices(self.rewards, self.weights, k=1))

    def getRewards(self)-> dict:
        rewards = dict()
        for i in range(self.num_items):
            rewards[self.rewards[i]] = self.weights[i]

        return rewards
