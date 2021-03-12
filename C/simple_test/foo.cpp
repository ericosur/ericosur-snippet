// thread example
#include <iostream>       // std::cout
#include <thread>         // std::thread

int wtf()
{
  int p;
  for (int x=0; x < 2147483647; ++x) {
    p = x * x % 640617;
  }
  return p;
}

void foo()
{
  const int loop = 100000;
  double s = 0.0;
  for (int i=0; i<loop; i++) {
    s = 1048576.0 * (double)i + 65535.999999 * 1.5 * i / 3.141592653589 * (double)wtf();
  }
  std::cout << "foo(): " << s << std::endl << std::flush;
}

void bar(int x)
{
  // do stuff...
  const int loop = 1000000;
  double s = 0.0;
  for (int i=0; i<loop; i++) {
    s = 1048576.0 * i + 1.815 * i / 3.141592653589 * 1.41424142 * 2.8182818284;
  }
  std::cout << "bar(): " << s << std::endl << std::flush;
}

int main()
{
  std::thread first (foo);     // spawn new thread that calls foo()
  std::thread second (bar,0);  // spawn new thread that calls bar(0)

  std::cout << "main, foo and bar now execute concurrently...\n";

  // synchronize threads:
  first.join();                // pauses until first finishes
  second.join();               // pauses until second finishes

  std::cout << "foo and bar completed.\n";

  return 0;
}
