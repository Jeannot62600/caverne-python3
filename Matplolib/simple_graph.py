import matplotlib.pyplot as plt

x = [i/10 for i in range(100)]
y = [j**2 for j in x]

plt.plot(x,y)

plt.xlabel('Label X')
plt.ylabel('Label Y')
plt.title("This is a simple graph of square")
plt.grid(True)
plt.savefig("simple_graph.png")
plt.show()
