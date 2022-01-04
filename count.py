import os
import platform

num_prob = 0
num_solution = 0
for root, dirs, files in os.walk("./Problems"):
    
    if len(root.split("/")) == 3:
        # if current directory is month
        num_prob += len(dirs)

    if len(root.split("/")) == 4:
        # if current directory is problem
        solutions = list(filter(lambda x: not x.endswith(".md"), files))
        num_solution += len(solutions)

print(num_prob, num_solution)
