#include <iostream>
#include <thread>

void printFromThread() {
    std::cout << "Hello from thread" << std::endl;
}

int main() {
    // Create a thread that runs the function printFromThread
    std::thread t(printFromThread);

    // Print from the main thread
    std::cout << "Hello from Main" << std::endl;

    // Wait for the thread to complete
    t.join();

    return 0;
}