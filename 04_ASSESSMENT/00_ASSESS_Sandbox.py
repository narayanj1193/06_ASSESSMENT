import threading
import matplotlib.pyplot as plt
import random
import warnings
# Function to display the random graph
def display_graph():
    # Generate random graph data
    x = range(10)
    y = [random.randint(0, 10) for _ in x]

    # Display the graph
    plt.plot(x, y)
    plt.show()

# Function to check for user input
def check_user_input():
    while True:
        user_input = input("Would you like to display the graph? (yes/no): ")
        if user_input.lower() == "yes":
            # Display the graph
            display_graph()
            break
        elif user_input.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

warnings.filterwarnings("ignore", category=UserWarning)
# Create and start the input thread
input_thread = threading.Thread(target=check_user_input)
input_thread.start()

# Wait for the input thread to complete before exiting the program
input_thread.join()
