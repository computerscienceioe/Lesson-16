
import matplotlib.pyplot as plt

# ages = [16,17,18]
# plt.plot(ages)
# plt.show()


# names = ["Mark", "Sarah", "Niamh"]
# ages = [16,17,18]
# plt.plot(names, ages)
# plt.savefig("Plot2.png")
# plt.show()

# names = ["Mark", "Sarah", "Niamh"]
# ages = [16,17,18]
# plt.plot(names, ages)
# plt.title("Title goes on top")
# plt.xlabel("xlabel goes on the x-axis")
# plt.ylabel("ylabel goes on the y-axis")
# plt.savefig("Plot3.png")
# plt.show()

# names = ["Mark", "Sarah", "Niamh"]
# ages = [16,17,18]
# plt.plot(names, ages)
# plt.legend(["Student ages"])
# plt.savefig("Plot4.png")
# plt.show()

# names = ["Mark", "Sarah", "Niamh"]
# ages = [16,17,18]
# plt.plot(names, ages, 'r--')
# plt.savefig("Plot5.png")
# plt.show()

# names = ["Mark", "Sarah", "Niamh"]
# ages = [16,17,18]
# plt.plot(names, ages, 'bs')
# plt.savefig("Plot6.png")
# plt.show()

# names = ["Mark", "Sarah", "Niamh"]
# ages = [16,17,18]
# plt.scatter(names, ages)
# plt.show()

names = ["Mark", "Sarah", "Niamh"]
ages = [16,17,18]
numSiblings = [2,3,1]
plt.plot(names, ages)
plt.plot(names, numSiblings)
plt.legend(["Ages", "Number of siblings"])
plt.show()
