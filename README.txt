Evan Nelson [email: enelson@gatech.edu], Hyatt Bao [hbao31@gatech.edu]
April 19, 2019
tsp-3510.py [the code executing two ops]
output.txt [the output of the mat requirement]
README.txt: the txt file here explaining everything
tsp-3510.pdf: The pdf explaining our algorithm two-opt
command to run: py tsp-3510.py [input txt file containing nodes and ids] [output txt file containing cost and route of nodes] maximum time constraint
Note: The algorithm needs a minimum of 10 seconds on the time constraint, otherwise it will not function properly due to the way we have implemented the time limit. It will usually yield the best run, but it may be best to run a few times as it has randomness elements in the main method where it randomly shuffles the routes to explore more.