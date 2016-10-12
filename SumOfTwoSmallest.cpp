#include <vector>
using namespace std;

long sumTwoSmallestNumbers(std::vector<int> numbers) {
  long small1, small2 = 999999999999999;
    for (int i = 0; i < numbers.size(); i++) {
    long cur = numbers[i];
    if (cur < small1) {
      small2 = small1;
      small1 = cur;
    } else if (cur < small2) {
      small2 = cur;
    }
  }
  return small1 + small2;
}
