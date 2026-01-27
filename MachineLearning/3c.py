import matplotlib.pyplot as plt

year = [2019, 2020, 2021, 2022]
sales = [300, 100, 110, 150]

plt.plot(year, sales, marker='o')
plt.title("Sales trend over years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("sales.png")
plt.close()
