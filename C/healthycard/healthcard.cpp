//
// a small demo program to read some fields from °·«O¥d
//

#include <stdio.h>
#include <winscard.h>
#include <stdlib.h>
#include <string.h>
#ifndef _WIN32
#include <unistd.h>
#endif

#define LPCSTR	LPCTSTR

void my_get_readers(SCARDCONTEXT hContext, char *pCardReaderName);

struct APDURec
{
	BYTE bCLA;
	BYTE bINS;
	BYTE bP1;
	BYTE bP2;
	BYTE bP3;
	BYTE Data[255];
	bool IsSend;
	BYTE le;
};

void test();
void apdu_hc_SELECT();
void apdu_hc_getrecode();
LONG send_command(SCARDHANDLE hCardHandle, APDURec apdu_command,
				  SCARD_IO_REQUEST sendprotocol, SCARD_IO_REQUEST recprotocol);
void hello(int line);
void pcsc_stringify_error(LONG rv);
void dump_recv_buffer(BYTE* buffer, DWORD len);

struct APDURec apdu;
BYTE RecvBuff[1024];
DWORD g_recvbuff_len = 0;

int main()
{
	test();

	return 0;
}

void test()
{
	// establish context for smart card reader
    SCARDCONTEXT hSC;
	LONG lReturn;
    const int BUFFER_SIZE = 1024;

    lReturn = SCardEstablishContext(SCARD_SCOPE_USER, 0, 0, &hSC);
    if (lReturn != SCARD_S_SUCCESS)
    {
        printf("SCardEstablishContext() failed\n");
		return;
    }
    else
    {
        printf("SCardEstablishContext() ok\n");
    }

	// get card reader names
	char pCardReaderName[256];
	my_get_readers(hSC, pCardReaderName);

	// connect to smart card
	SCARDHANDLE     hCardHandle;
	DWORD           dwAP;

	lReturn = SCardConnect( hSC,
#if _WIN32
	                        (LPCTSTR)pCardReaderName,
#else
							(LPCSTR)pCardReaderName,
#endif
	                        SCARD_SHARE_SHARED,
	                        SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1,
	                        &hCardHandle,
	                        &dwAP );
	if ( SCARD_S_SUCCESS != lReturn )
	{
	    printf("Failed SCardConnect\n");
	    exit(1);  // Or other appropriate action.
	}

	// Use the connection; here we will merely display the
	// active protocol.
	switch ( dwAP )
	{
	    case SCARD_PROTOCOL_T0:
	        printf("Active protocol T0\n");
	        break;

	    case SCARD_PROTOCOL_T1:
	        printf("Active protocol T1\n");
	        break;
#if _WIN32
	    case SCARD_PROTOCOL_UNDEFINED:
#else
	   	case 0:
#endif
	    default:
	        printf("Active protocol unnegotiated or unknown\n");
	        break;
	}

	// send request to smart card
	SCARD_IO_REQUEST SendRequest;
	SCARD_IO_REQUEST RecvRequest;

	SendRequest.dwProtocol = SCARD_PROTOCOL_T1;
	SendRequest.cbPciLength = sizeof(SendRequest);

	RecvRequest.dwProtocol = SCARD_PROTOCOL_T1;
	RecvRequest.cbPciLength = sizeof(RecvRequest);

	apdu_hc_SELECT();
	memset(RecvBuff, 0, 1024);
	lReturn = send_command(hCardHandle, apdu, SendRequest, RecvRequest);

	if ( (lReturn == 0) && (RecvBuff[0] == 144) && (RecvBuff[1] == 0) )
	{
		printf("===> next stage...\n");
		apdu_hc_getrecode();
		lReturn = send_command(hCardHandle, apdu, SendRequest, RecvRequest);
		if ( (lReturn == 0) && (RecvBuff[57] == 144) && (RecvBuff[58] == 0) )
		{
			dump_recv_buffer(RecvBuff, g_recvbuff_len);

			const int RES_SIZE = 40;
			char sResult[RES_SIZE];
			DWORD ptr = 0;

			memset(sResult, 0, RES_SIZE);
			memcpy(sResult, RecvBuff, 12);
			printf("@@@@@ %s\n", sResult);

			ptr += 12;
			memset(sResult, 0, RES_SIZE);
			memcpy(sResult, RecvBuff + ptr, 20);
			printf("@@@@@ %s\n", sResult);

			ptr += 20;
			memset(sResult, 0, RES_SIZE);
			memcpy(sResult, RecvBuff + ptr, 10);
			printf("@@@@@ %s\n", sResult);

			ptr += 10;
			memset(sResult, 0, RES_SIZE);
			memcpy(sResult, RecvBuff + ptr, 7);
			printf("@@@@@ %s\n", sResult);

			ptr += 7;
			memset(sResult, 0, RES_SIZE);
			memcpy(sResult, RecvBuff + ptr, 1);
			printf("@@@@@ %s\n", sResult);

			ptr += 1;
			memset(sResult, 0, RES_SIZE);
			memcpy(sResult, RecvBuff + ptr, 7);
			printf("@@@@@ %s\n", sResult);
		}
	}
	else
	{
		printf("cannot process\n");
	}

	// disconnect smart card
	lReturn = SCardDisconnect(hCardHandle, SCARD_RESET_CARD);
}


void apdu_hc_SELECT()
{
	apdu.bCLA = 0x00;
	apdu.bINS = 0xA4;
	apdu.bP1 = 0x04;
	apdu.bP2 = 0x00;
	apdu.bP3 = 0x10;

	apdu.Data[0] = 0xD1;
	apdu.Data[1] = 0x58;
	apdu.Data[2] = 0x00;
	apdu.Data[3] = 0x00;
	apdu.Data[4] = 0x01;
	apdu.Data[5] = 0x00;
	apdu.Data[6] = 0x00;
	apdu.Data[7] = 0x00;
	apdu.Data[8] = 0x00;
	apdu.Data[9] = 0x00;
	apdu.Data[10] = 0x00;
	apdu.Data[11] = 0x00;
	apdu.Data[12] = 0x00;
	apdu.Data[13] = 0x00;
	apdu.Data[14] = 0x11;
	apdu.Data[15] = 0x00;
	//apdu.Data[16] = 0x00;
	apdu.IsSend = true;
	apdu.le = 0;
}

void apdu_hc_getrecode()
{
	apdu.bCLA = 0x00;
	apdu.bINS = 0xCA;
	apdu.bP1 = 0x11;
	apdu.bP2 = 0x00;
	apdu.bP3 = 0x02;
	apdu.Data[0] = 0x00;
	apdu.Data[1] = 0x00;
	apdu.IsSend = true;
	apdu.le = 57;
}

LONG send_command(SCARDHANDLE hCardHandle, APDURec apdu_command,
				  SCARD_IO_REQUEST sendprotocol, SCARD_IO_REQUEST recprotocol)
{
	BYTE SendBuff[260];
	DWORD SendBuffLen;
	DWORD RecvBuffLen;
	DWORD lReturn;

	memset(SendBuff, 0, 260);
	memset(RecvBuff, 0, 1024);

	SendBuff[0] = apdu.bCLA;
	SendBuff[1] = apdu.bINS;
	SendBuff[2] = apdu.bP1;
	SendBuff[3] = apdu.bP2;
	SendBuff[4] = apdu.bP3;

	if (apdu.IsSend)
	{
		memcpy(SendBuff+5, apdu.Data, apdu.bP3);
		SendBuffLen = 5 + apdu.bP3;
		RecvBuffLen = 2 + apdu.le;
	}
	else
	{
		SendBuffLen = 5;
		RecvBuffLen = 2 + apdu.bP3;
	}

	//  Transmit the request.
	//  lReturn is of type LONG.
	//  hCardHandle was set by a previous call to SCardConnect.
	//  pbSend points to the buffer of bytes to send.
	//  dwSend is the DWORD value for the number of bytes to send.
	//  pbRecv points to the buffer for returned bytes.
	//  dwRecv is the DWORD value for the number of returned bytes.
	lReturn = SCardTransmit(hCardHandle,
							&sendprotocol,
							SendBuff,
							SendBuffLen,
							NULL,
							RecvBuff,
							&RecvBuffLen );
	g_recvbuff_len = RecvBuffLen;
	if ( SCARD_S_SUCCESS != lReturn )
	{
		printf("SCardTransmit() failed\n");
	}
	else
	{
		printf("SCardTransmit() ok\n");
	}

	return lReturn;
}

void hello(int line)
{
	printf("at line %d ==> ", line);
}

void my_get_readers(SCARDCONTEXT hContext, char *pCardReaderName)
{
#ifdef _WIN32
	LPCTSTR mszGroups;
#else
	LPCSTR mszGroups;
#endif
	LPSTR mszReaders;
	DWORD dwReaders = 0;
	LONG rv;
	int iList[16];

	mszGroups = 0;
	rv = SCardListReaders( hContext, mszGroups, 0, &dwReaders );

	if ( rv != SCARD_S_SUCCESS ) {
		pcsc_stringify_error(rv);
		printf("control: Error listing readers\n");
		exit(41);
	}
	mszReaders = (char *)malloc(sizeof(char)*dwReaders);
	rv = SCardListReaders( hContext, mszGroups, mszReaders, &dwReaders );

	if ( rv != SCARD_S_SUCCESS )
	{
//		printf("PCSC ERROR: %s\n", pcsc_stringify_error(rv));
		printf("control: Error listing readers\n");
		exit(43);
	}
	/* Have to understand the multi-string here */
	int p = 0;
	for (DWORD i=0; i < dwReaders - 1; i++ )
	{
		++p;
		printf("Reader %02d: %s\n", p, &mszReaders[i]);
		strcpy(pCardReaderName, &mszReaders[i]);
		iList[p] = i;
		while ( mszReaders[++i] != 0 );
	}
}

void pcsc_stringify_error(LONG rv)
{
	switch (rv)
	{
	case SCARD_E_NO_READERS_AVAILABLE:
		printf("group contains no readers\n");
		break;
	default:
		printf("rv = 0x%08x\n", rv);
		break;
	}
}

void dump_recv_buffer(BYTE* buffer, DWORD len)
{
	const char fname[] = "hc.dat";
	FILE *out = NULL;
	DWORD wl = 0;

	if ( (out = fopen(fname, "wb")) == NULL )
	{
		printf("cannot output dump file\n");
		exit(83);
	}

	wl = fwrite(buffer, 1, len, out);
	printf("write len = %d\n", wl);
	fclose(out);
}
