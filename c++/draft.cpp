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
  int n = 4;
  std::vector<std::thread> threads;

  for (int i = 0; i < n; i++) {
    threads.emplace_back(worker, i);
  }

  for (auto &t : threads)
    t.join();
}
