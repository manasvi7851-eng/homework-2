import matplotlib.pyplot as plt
weeks = ["Week 1","Week 2","Week 3","Week 4","Week 5","Week 6","Week 7"]
savings = [50,100,150,220,280,350,420]
plt.plot(weeks,savings,color="green",marker="o",linestyle="dotted",linewidth=2)
plt.title("My Weekly Savings Progress")
plt.xlabel("Weeks")
plt.ylabel("Savings (£)")
plt.show()
plt.bar(weeks,savings,color="skyblue",edgecolor="black")
plt.title("My Weekly Savings Comparison")
plt.xlabel("Weeks")
plt.ylabel("Savings (£)")
plt.show()
