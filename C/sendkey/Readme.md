Readme
======

## ShowWindow

winapi ShowWindow()

https://stackoverflow.com/questions/29837268/how-can-i-restore-a-winapi-window-if-its-minimized

https://stackoverflow.com/posts/29837548/revisions

```c++
void show(HWND hwnd)
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
    case SW_SHOWMAXIMIZED:
        ShowWindow(hwnd, SW_SHOWMAXIMIZED);
        break;
    case SW_SHOWMINIMIZED:
        ShowWindow(hwnd, SW_RESTORE);
        break;
    default:
        ShowWindow(hwnd, SW_NORMAL);
        break;
    }

    SetForegroundWindow(hwnd);
}

int WINAPI WinMain(HINSTANCE hinst, HINSTANCE, LPSTR cmdline, int nshow)
{
    const wchar_t *classname = L"Chrome_WidgetWin_1";

    HWND hwnd = NULL;
    for (;;)
    {
        hwnd = FindWindowEx(0, hwnd, classname, 0);
        if (!hwnd) break;

        //skip Chrome's invisible winodw
        if (IsWindowVisible(hwnd))
        {
            wchar_t buf[260];
            GetWindowText(hwnd, buf, 260);
            OutputDebugString(buf);
            OutputDebugString(L"\n");

            show(hwnd);
            break;
        }
    }

    return 0;
}
```