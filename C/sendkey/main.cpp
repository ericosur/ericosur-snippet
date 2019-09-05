#include "sendkey.h"
#include <windows.h>
#include <stdio.h>

#if 0
int main()
{
	activate_powerpoint();


    return 0;
}

#else
int main()
{
    const int PAUSE_SMALL = 250;

    // find and set one copy of powerpoint to foreground to receive key event
    activate_powerpoint();

    if (!g_foundPPT) {
        printf("cannot find any PowerPoint, exit...\n");
        return 0;
    }

    // Pause for a moment
    Sleep(PAUSE_SMALL);

    // NOTE: if call send_pg??() continuously and quickly
    // some keyevent will be dropped
    printf("shoot PGDN!\n");
    send_pgdn();
    Sleep(PAUSE_SMALL); // make a little pause
    printf("shoot PGDN!\n");
    send_pgdn();
    Sleep(PAUSE_SMALL); // make a little pause
    printf("shoot PGUP!\n");
    send_pgup();

    send_down();
    Sleep(PAUSE_SMALL); // make a little pause
    send_down();
    Sleep(PAUSE_SMALL); // make a little pause
    send_down();

    return 0;
}
#endif
