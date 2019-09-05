// sendkey.c
// a sample program that uses Windows API to search
// **Microsoft PowerPoint** in background, and set it
// to foreground for receiving key focus.
//
// also demo send keyevent PGUP/PGDN to powerpoint
//

#include "sendkey.h"

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

// send Page Down key
void send_pgdn()
{
    shoot_key(VK_NEXT);
}

// send Page Up key
void send_pgup()
{
    shoot_key(VK_PRIOR);
}

// send down arrow key
void send_down()
{
    shoot_key(VK_DOWN);
}

// send up arrow key
void send_up()
{
    shoot_key(VK_UP);
}

BOOL OnWindowEnum(HWND hwnd, LPARAM lparam)
{
// interface of this callback function is fixed, so TARGET_TITLE is hardcoded
//#define TARGET_TITLE	"PowerPoint "
#define TARGET_TITLE	"Total Commander"

    const size_t TITLE_SIZE = 512;
	char title[TITLE_SIZE] = { 0 };

	(void)lparam;  // make compiler happy

    GetWindowText(hwnd, title, TITLE_SIZE);
    if (strstr(title, TARGET_TITLE) != NULL) {
        // found hwnd will goes to foreground and get keyboard focus

		show_window(hwnd);
		g_foundPPT = 1;
		//BOOL ret = SetForegroundWindow(hwnd);
        //printf("got %s, %p\n", title, hwnd);
        //if (ret) {
        //    printf("set foreground...\n");
        //    g_foundPPT = 1;
        //}
    } else {
        if (strlen(title) > 3 && strstr(title, "IME") == NULL) {
            printf("title:%s\n", title);
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

void show_window(HWND hwnd)
{
    //ShowWindow(hwnd, SW_NORMAL);
    //SetForegroundWindow(hwnd);
    //We can just call ShowWindow & SetForegroundWindow to bring hwnd to front.
    //But that would also take maximized window out of maximized state.
    //Using GetWindowPlacement preserves maximized state
    WINDOWPLACEMENT place;
    memset(&place, 0, sizeof(WINDOWPLACEMENT));
    place.length = sizeof(WINDOWPLACEMENT);
    GetWindowPlacement(hwnd, &place);

    switch (place.showCmd)
    {
    //case SW_SHOWMAXIMIZED:
        //ShowWindow(hwnd, SW_SHOWMAXIMIZED);
        //break;
    case SW_SHOWMINIMIZED:
        ShowWindow(hwnd, SW_RESTORE);
        break;
    default:
        //ShowWindow(hwnd, SW_NORMAL);
        break;
    }

    SetForegroundWindow(hwnd);
}

// const wchar_t *classname = L"Total Commander";
int find_window(LPCSTR classname)
{
    HWND hwnd = NULL;
    for (;;) {
        hwnd = FindWindowEx(0, hwnd, (LPCSTR)classname, 0);
		if (!hwnd) {
			printf("find_window: not found!\n");
			break;
		}

		printf("hwnd: %p\n", hwnd);
        //skip invisible winodw
        if (IsWindowVisible(hwnd)) {
            char buf[260];
            GetWindowText(hwnd, (LPSTR)buf, 260);
            //OutputDebugString(buf);
            //OutputDebugString("\n");
			printf("%s\n", buf);

            //show(hwnd);
            break;
        }
    }

    return 0;
}
