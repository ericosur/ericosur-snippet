#include "nndef.h"
#define NAME "tx"

int sock;

int send_request(int val)
{
	char str[32];
	int sz_n;

	if (val < 0) {
		sprintf(str, "exec");
	} else {
		sprintf(str, "%d", val);	
	}
	sz_n = strlen(str) + 1;
	
	printf("tx sends: %s\n", str);
	return nn_send(sock, str, sz_n, 0);
}

int recv_answer()
{
	char *buf = NULL;
	int result = nn_recv(sock, &buf, NN_MSG, 0);
	if (result > 0) {
		printf("tx recv: %s\n", buf);
		nn_freemsg(buf);
	}
	return result;
}

int init(const char *url)
{
    sock = nn_socket(AF_SP, NN_PAIR);
    assert(sock >= 0);
    assert(nn_bind(sock, url) >= 0);
    return 0;
//    send_recv(sock, NODE0);
//    return nn_shutdown(sock, 0);
}

int main()
{
	int i;
	int r;
    
	unsigned int seed = (unsigned int)time(NULL);
	srand(seed); 

	init(URL);
	for (i = 0; i < MAX_VAL; i++) {
		r = rand() % 100;
		if ( r % 11 == 0 ) {
			break;
		}
		//printf("%d\n", r);
		send_request(r);
	}
	send_request(-1);
	printf("enter recv loop...\n");
	while (1) {
		if (recv_answer())
			break;
	}
	nn_shutdown(sock, 0);
	return 0;
}
