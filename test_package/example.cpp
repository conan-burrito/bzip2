#include <bzlib.h>
#include <iostream>

int main() {
   std::cout << BZ2_bzlibVersion() << std::endl;
   return 0;
}
