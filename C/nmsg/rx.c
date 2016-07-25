/// file rx.c

#include "nndef.h"

#define NAME "rx"

int sock;
int cnt = 0;
int arr[MAX_VAL] = {0};
int sum = 0;

int sumup()
{
	int i;

	for (i = 0; i < cnt; i++) {
		sum += arr[i];
	}
	return sum;
}

int recv_request()
{
	char *buf = NULL;
	int result = 0;
	int rbyte = nn_recv(sock, &buf, NN_MSG, 0);
	if (rbyte > 0) {
		printf("rx received: %s\n", buf);
		if (strcmp(buf, "exec") == 0) {

			result = -1;
		} else {
			arr[cnt++] = atoi(buf);
		}
		nn_freemsg(buf);
	}
	return result;
}

int send_val(int val)
{
	char str[32];
	int sz_n;

	sprintf(str, "%d", val);	
	sz_n = strlen(str) + 1;
	
	printf("rx send_val() sends: %s\n", str);
	return nn_send(sock, str, sz_n, 0);
}

int init()
{
	int sock = nn_socket(AF_SP, NN_PAIR);
	assert(sock >= 0);
	assert(nn_connect(sock, URL) >= 0);
	return 0;
}

int main()
{
	init();
	while (1) {
		if (recv_request() == -1)
			break;
		usleep(1000);
	}
	sumup();
	nn_shutdown(sock, 0);
	printf("rx: sum: %d\n", sum);
	return 0;
}
