#include <iostream>
#include "date/date.h"

using namespace std;
using namespace std::chrono;
using namespace date;

int main()
{
    auto today = floor<days>(system_clock::now());
    cout << today << '\n';
}
