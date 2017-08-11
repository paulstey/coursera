
// change to C++ io
// change to one line comments
// change defines of constants to const
// change array to vector<>
// inline any short function


#include <iostream>
#include <vector>

const int N = 40;

void sum(int& p, int n, std::vector<int> d) {
  p = 0;

  for (int i = 0; i < n; ++i) {
    p += d[i];
  }
}


int main() {
  int accum = 0;
  std::vector<int> data(N);

  for (int i = 0; i < N; ++i) {
    data[i] = i;
  }
  sum(accum, N, data);

  std::cout << "sum is: " << accum  << std::endl;

  return 0;
}
