import os

num_prob = 0
num_solution = 0
for root, dirs, files in os.walk("./Archives"):
    # file = (root, dirs, files)
    if len(root.split("/")) == 3:
        # if current directory is month
        num_prob += len(dirs)

    if len(root.split("/")) == 4:
        # if current directory is problem
        solutions = list(filter(lambda x: not x.endswith(".md"), files))
        num_solution += len(solutions)
    
print(num_prob, num_solution)