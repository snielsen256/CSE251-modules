"""
Course: CSE 251
Lesson Week: 09
File: team1.py

Purpose: team activity - Dining philosophers problem

Problem statement

Five silent philosophers sit at a round table with bowls of spaghetti. Forks
are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can
only eat spaghetti when they have both left and right forks. Each fork can be
held by only one philosopher and so a philosopher can use the fork only if it
is not being used by another philosopher. After an individual philosopher
finishes eating, they need to put down both forks so that the forks become
available to others. A philosopher can only take the fork on their right or
the one on their left as they become available and they cannot start eating
before getting both forks.  When a philosopher is finished eating, they think 
for a little while.

Eating is not limited by the remaining amounts of spaghetti or stomach space;
an infinite supply and an infinite demand are assumed.

The problem is how to design a discipline of behavior (a concurrent algorithm)
such that no philosopher will starve

Instructions:

        **************************************************
        ** DO NOT search for a solution on the Internet **
        ** your goal is not to copy a solution, but to  **
        ** work out this problem.                       **
        **************************************************

- You have Locks and Semaphores that you can use.
- Remember that lock.acquire() has an argument called timeout.
- philosophers need to eat for 1 to 3 seconds when they get both forks.  
  When the number of philosophers has eaten MAX_MEALS times, stop the philosophers
  from trying to eat and any philosophers eating will put down their forks when finished.
- philosophers need to think for 1 to 3 seconds when they are finished eating.  
- You want as many philosophers to eat and think concurrently.
- Design your program to handle N philosophers and N forks after you get it working for 5.
- Use threads for this problem.
- When you get your program working, how to you prove that no philosopher will starve?
  (Just looking at output from print() statements is not enough)
- Are the philosophers each eating and thinking the same amount?
- Using lists for philosophers and forks will help you in this program.
  for example: philosophers[i] needs forks[i] and forks[i+1] to eat (the % operator helps)
"""

import time
import threading

PHILOSOPHERS = 5
MAX_MEALS_EATEN = PHILOSOPHERS * 5

def do_philosophy(self_index, meals, lock1, lock2):
    """
    The function called by the philosopher threads.
    """

    for i in range(5):
        #determine who eats
        #for i in range

        lock1.acquire(timeout = 1)
        lock2.acquire(timeout = 1)
        eat(meals)
        lock1.release()
        lock2.release()
        think()

def eat(meals):
    meals.acquire()

def think():
    pass

def main():
    # create the meals
    meals = threading.Semaphore(MAX_MEALS_EATEN)
    # create the forks
    fork_list = []
    for _ in range(0, PHILOSOPHERS):
        fork_list.append(threading.Lock())

    # create PHILOSOPHERS philosophers
    philo_list = []
    for i in range(0, PHILOSOPHERS):
        
        #determine the forks
        fork_index_1 = i
        fork_index_2 = i + 1

        if fork_index_2 == PHILOSOPHERS:
          fork_index_2 = 0

        # add philosopher to list
        philo_list.append(threading.Thread(target=do_philosophy, args=(i+1, meals, fork_list[fork_index_1], fork_list[fork_index_2])))

    # TODO - Start them eating and thinking
    for i in range(0, len(philo_list)):
        philo_list[i].start()
    
    for i in range(0, len(philo_list)):
        philo_list[i].join()

    # TODO - Display how many times each philosopher ate
    print("finished")


if __name__ == '__main__':
    main()
