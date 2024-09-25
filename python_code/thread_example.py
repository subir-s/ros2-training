import threading

def print_from_thread():
    print("Hello from thread")

# Create a new thread that runs the print_from_thread function
thread = threading.Thread(target=print_from_thread)
thread.start()

# Print from the main thread
print("Hello from Main")

# Wait for the thread to complete
thread.join()