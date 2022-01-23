import matplotlib.pyplot as plt

generations_stat_file = open("generations_stat_file.txt", "rt")
lines = []
while True:
    line = generations_stat_file.readline()
    if line == "":
        break
    lines.append(line)

number_of_generations = len(lines)
stats = []
i = 0
while i < len(lines):
    stats.append(lines[i].split(" "))
    i += 1

minimums = []
averages = []
maximums = []

i = 0
while i < len(stats):
    maximums.append(int(stats[i][0]))
    averages.append(float(stats[i][1]))
    minimums.append(int(stats[i][2].rstrip("\n")))
    i += 1



print(maximums)
print(averages)
print(minimums)

generations_stat_file.close()

x = []
i = 1
while i <= number_of_generations:
    x.append(i)
    i += 1



plt.plot(x, maximums, label="Maximum")
plt.plot(x, averages, label="Average")
plt.plot(x, minimums, label="Minimum")
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.legend()
plt.show()







