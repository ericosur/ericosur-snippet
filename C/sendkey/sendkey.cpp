// sendkey.c
// a sample program that uses Windows API to search
// **Microsoft PowerPoint** in background, and set it
// to foreground for receiving key focus.
//
// also demo send keyevent PGUP/PGDN to powerpoint
//

#include <windows.h>

// for printf()
#include <stdio.h>
// for strstr()
#include <string.h>

BOOL g_foundPPT = 0;

void shoot_key(WORD vk)
{
    // This structure will be used to create the
    // keyboard input event
    INPUT ip;

    // Set up a generic keyboard event
    ip.type = INPUT_KEYBOARD;
    ip.ki.wScan = 0; // hardware scan code for key
    ip.ki.time = 0;
    ip.ki.dwExtraInfo = 0;

    // Press the key
    ip.ki.wVk = vk;     // the virutal key
    ip.ki.dwFlags = 0;  // 0 for key press
    SendInput(1, &ip, sizeof(INPUT));

    // no need to sleep/pause here

    // Release the key
    ip.ki.dwFlags = KEYEVENTF_KEYUP; // KEYEVENTF_KEYUP for key release
    // windows api from WINUSER
    SendInput(1, &ip, sizeof(INPUT));
}

/*
   send Page Down key
*/
void send_pgdn()
{
    shoot_key(VK_NEXT);
}

/*
   send Page Up key
*/
void send_pgup()
{
    shoot_key(VK_PRIOR);
}

BOOL OnWindowEnum(HWND hwnd, LPARAM lparam)
{
//#define TARGET_TITLE	"Microsoft PowerPoint"
#define TARGET_TITLE	"Total Commander"

    const size_t TITLE_SIZE = 512;
	char title[TITLE_SIZE] = { 0 };

	(void)lparam;

    GetWindowText(hwnd, title, TITLE_SIZE);
    if (strstr(title, TARGET_TITLE) != NULL) {
        // found hwnd will goes to foreground and get keyboard focus
        BOOL ret = SetForegroundWindow(hwnd);
        printf("got %s, %p\n", title, hwnd);
        if (ret) {
            printf("set foreground...\n");
            g_foundPPT = 1;
        }
    }

    return TRUE;
}

/*
    search **Microsoft PowerPoint** and set it foreground to get keyboard

    NOTE: if there are more than one powerpoint, the last found will be
    lifted
*/
void activate_powerpoint()
{
    EnumWindows(OnWindowEnum, 0);
}

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

    return 0;
}
