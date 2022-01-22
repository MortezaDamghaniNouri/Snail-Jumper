import copy
import random
from player import Player


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"




    # This function calculates the average fitness of the input list
    def average_fitness_calculator(self, input_players_list):
        summation = 0
        for i in input_players_list:
            summation += i.fitness
        return summation / len(input_players_list)


    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.
        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # Top-k algorithm is implemented here by using bubble sort
        i = len(players) - 1
        while i > 0:
            j = 0
            while j <= (i - 1):
                if players[j].fitness > players[j + 1].fitness:
                    temp = players[j + 1]
                    players[j + 1] = players[j]
                    players[j] = temp
                j += 1
            i = i - 1

        # Writing statistics on a file for part 5 (bonus part)
        stat_file = open("stat_file.txt", "at")
        stat_file.write(str(players[len(players) - 1].fitness) + " " + str(self.average_fitness_calculator(players)) + " " + str(players[0].fitness) + "\n")
        stat_file.close()





        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)

        # TODO (Additional: Learning curve)
        return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.
        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:

            new_players = []
            i = 0
            while i < len(prev_players):
                parent1 = self.clone_player(prev_players[i])
                parent2 = self.clone_player(prev_players[i + 1])
                child1 = self.clone_player(parent1)
                child2 = self.clone_player(parent2)

                layer_sizes = parent1.nn.layer_sizes
                # Generating child1
                child1_random_number = random.uniform(0, 1)     # The probability of happening cross over for child1 is controlled by this random number
                if child1_random_number <= 0.8:
                    j = int(layer_sizes[0] / 2)
                    while j < layer_sizes[0]:
                        child1.nn.weights1[j] = parent2.nn.weights1[j]
                        j += 1

                    j = int(layer_sizes[1] / 2)
                    while j < layer_sizes[1]:
                        child1.nn.biases1[0][j] = parent2.nn.biases1[0][j]
                        child1.nn.weights2[j] = parent2.nn.weights2[j]
                        j += 1

                    j = int(layer_sizes[2] / 2)
                    while j < layer_sizes[2]:
                        child1.nn.biases2[0][j] = parent2.nn.biases2[0][j]
                        j += 1


                # Generating child2
                child2_random_number = random.uniform(0, 1)  # The probability of happening cross over for child2 is controlled by this random number
                if child2_random_number <= 0.8:
                    j = 0
                    while j < (layer_sizes[0] / 2):
                        child2.nn.weights1[j] = parent1.nn.weights1[j]
                        j += 1

                    j = 0
                    while j < (layer_sizes[1] / 2):
                        child2.nn.biases1[0][j] = parent1.nn.biases1[0][j]
                        child2.nn.weights2[j] = parent1.nn.weights2[j]
                        j += 1

                    j = 0
                    while j < (layer_sizes[2] / 2):
                        child2.nn.biases2[0][j] = parent1.nn.biases2[0][j]
                        j += 1

                new_players.append(child1)
                new_players.append(child2)
                # if i % 2 == 0:
                    #   print("parent1 weights1: " + str(parent1.nn.weights1))
                    #   print("parent2 weights1: " + str(parent2.nn.weights1))
                    #   print("child1 weights1: " + str(child1.nn.weights1))
                    #   print("child2 weights1: " + str(child2.nn.weights1))
                    #   print("====")
                    #   print("parent1 biases2: " + str(parent1.nn.biases2))
                    #   print("parent2 biases2: " + str(parent2.nn.biases2))
                    #   print("child1 biases2: " + str(child1.nn.biases2))
                    #   print("child2 biases2: " + str(child2.nn.biases2))
                    #   print("=======================================")



                i += 2
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
