#include <assert.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <time.h>
#include <nanomsg/nn.h>
#include <nanomsg/pubsub.h>

#define IPCURL      "ipc:///tmp/pubsub.ipc"
#define MAX_REPEAT  100
#define PREFIX      "clock-"
// 1000 ==> 1ms
#define USLEEP_LEN  (100*1000)

void make_string(char *str, int max_size, int opt)
{
    memset(str, 0, max_size);
    // sprintf(str, "%s/%d/%s",
    //     PREFIX, opt,
    //     (opt%2 ? "Digital" : "Analog") );
    sprintf(str, "%s%s",
        PREFIX,
        (opt%2 ? "Digital" : "Analog") );
}

void send_data(int sock)
{
    int cnt = 0;
    const int MYSTR_MAX = 128;
    char data[MYSTR_MAX];
    while(cnt < MAX_REPEAT) {
        make_string(data, MYSTR_MAX, cnt);
        int sz_d = strlen(data) + 1; // '\0' too
        printf("SERVER: send_data: %s\n", data);
        int bytes = nn_send(sock, data, sz_d, 0);
        assert(bytes == sz_d);
        usleep(USLEEP_LEN);
        cnt ++;
    }
    printf("total %d published\n", cnt);
}

int bind_server(const char *url)
{
    int sock = nn_socket(AF_SP, NN_PUB);
    assert(sock >= 0);
    assert(nn_bind(sock, url) >= 0);
    return sock;
}

int main(const int argc, const char **argv)
{
    int sock = 0;

    sock = bind_server(IPCURL);
    printf("sock: %d\n", sock);
    usleep(2500);
    send_data(sock);
    usleep(1000);
    nn_shutdown(sock, 0);

    return 1;
}
