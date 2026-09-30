#include <stdio.h>
#include <opencv2/core.hpp>

int main()
{
    printf("opencv version: %d.%d.%d",
           CV_VERSION_MAJOR, CV_VERSION_MINOR, CV_VERSION_REVISION);
#ifdef CV_VERSION_STATUS
    printf("%s", CV_VERSION_STATUS);
#endif
    printf("\n");

    return 0;
}
