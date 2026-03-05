#include <chrono>
#include <iostream>
#include <thread>
#include <vector>

void worker(int id) {
  while (true) {
    std::cout << "Worker " << id << " running\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
  }
}

int main() {
  std::cout << "Hi";
  return 0;
}
