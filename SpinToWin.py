import csv
import random

class SpinToWin:
    def __init__(self)-> None:
        self.rewards = dict()
        self.num_items = int()

    def loadWheel(self, item_file: str)-> None:
        """
        Load wheel with CSV file
        @param item_file: CSV file containing rewards and weights
        """
        total_weight = int()
        weights = list()

        with open(item_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                reward, weight = row[0], row[1]

                try:
                    weight = float(weight)
                except ValueError:
                    raise ValueError("Weight must be number")

                self.rewards[reward] = weight

        self.num_items = len(self.rewards)

    def spin(self)-> str:
        return "".join(random.choices(list(self.rewards.keys()), list(self.rewards.values()), k=1))

    def addReward(self, reward: str, weight: str)-> str:
        """
        Add reward to wheel
        @param reward: Name of reward to add
        @param weight: Weight of new reward
        """
        if (reward in self.rewards):
            return f"Error: {reward} already exists"

        try:
            weight = float(weight)
            self.rewards[reward] = weight
        except ValueError:
            return f"Error: {weight} is not a valid weigt"

        return "Success"

    def getRewards(self)-> dict:
        """List rewards"""
        return self.rewards

    def updateReward(self, reward: str, new_weight: str)-> str:
        """
        Update current reward
        @param reward: Name of reward to update
        @param new_weight: New weight for specified reward
        """
        if (reward not in self.rewards):
            return f"Error: {reward} not in rewards"

        try:
            new_weight = float(new_weight)
            self.rewards[reward] = new_weight
        except ValueError:
            return f"Error: {new_weight} is not a valid weight"

        return "Success"

    def deleteReward(self, reward: str)-> str:
        """
        Delete reward from rewards
        @param reward: Name of the reward to delete
        """

        if (reward not in self.rewards):
            return f"Error: {reward} not in rewards"

        self.rewards.pop(reward)

        return f"Removed {reward}"