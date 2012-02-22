/*
 * This program "hook" the original convert.exe(ImageMagick) and log the arguments.
 *
 * 2008/05/22
 * ericosur
 */

// original source file comes from:
//----------------------------------------------------------------------------
// notepad.cpp
// Description : lanceur pour Notepad++, pour remplacer le notepad.exe de Windows
//      Remplacer dans  C:\WINDOWS\
//                      C:\WINDOWS\SYSTEM32\
//                      C:\WINDOWS\SYSTEM32\dllcache\
// Auteur   : Stepho (http://superstepho.free.fr/)
// Creation : 2005-08-22
//----------------------------------------------------------------------------

#include <windows.h>
#include <winreg.h>
#include <stdio.h>

#define LOGPATH			"d:\\_convert.log"
#define CMDBUFFERSIZE	2048
#define REGBUFFERSIZE	1024

int WINAPI WinMain (HINSTANCE hThisInstance,
                    HINSTANCE hPrevInstance,
                    LPSTR lpszArgument,
                    int nFunsterStil)
{
    PROCESS_INFORMATION oProcessInfo;
    STARTUPINFO si;
    char cmd[CMDBUFFERSIZE] = "\"C:\\Program Files\\ImageMagick\\convert.exe\"";

    // locate ImageMagick binary directory from registry
    HKEY hKey;

    if( RegOpenKeyEx( HKEY_LOCAL_MACHINE, "SOFTWARE\\ImageMagick\\current", 0, KEY_QUERY_VALUE, &hKey )
        == ERROR_SUCCESS )
    {
        DWORD   iType;
        unsigned char sData[REGBUFFERSIZE];
        DWORD   iDataSize = REGBUFFERSIZE;

        if( RegQueryValueEx( hKey, "BinPath", NULL, &iType, sData, &iDataSize )
            == ERROR_SUCCESS )
        {
            strcpy(cmd, "\"");
            strcat(cmd, (char*)sData);
            strcat(cmd, "\\convert.exe\"");
        }

        RegCloseKey(hKey);
    }

    // construct the command line
    if( strlen(lpszArgument) )
    {
        strcat(cmd, " ");
        strcat(cmd, lpszArgument);
    }

    // prepare process info for calling CreateProcess()
    memset( &si, 0, sizeof(si) );
    si.cb = sizeof(si);
    memset( &oProcessInfo, 0, sizeof(oProcessInfo) );

// log {
	FILE *fp = NULL;
	if ( (fp = fopen(LOGPATH, "a+t")) == NULL )
		MessageBox(NULL, "open error", "Error", 0);

	fprintf(fp, "cmd: %s\n", cmd);
	fprintf(fp, "arg: %s\n", lpszArgument);
	fclose(fp);
// log }

    //MessageBox(hThisInstance, cmd, "Command", MB_OK);

    // Launch the convert.exe
    CreateProcess( NULL
                 , cmd
                 , NULL
                 , NULL
                 , false
                 , 0
                 , NULL
                 , NULL
                 , &si
                 , &oProcessInfo
                 );

    // on ferme proprement
    CloseHandle( oProcessInfo.hProcess );
    CloseHandle( oProcessInfo.hThread );
}
