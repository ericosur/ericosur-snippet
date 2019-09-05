#ifndef __UTIL_SENDKEY_H__
#define __UTIL_SENDKEY_H__

#include <windows.h>

extern BOOL g_foundPPT;

void activate_powerpoint();
void send_pgup();
void send_pgdn();
void send_up();
void send_down();

void show_window(HWND hwnd);
int find_window(LPCSTR classname);

#endif  // __UTIL_SENDKEY_H__
