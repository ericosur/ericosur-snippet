// demo.cpp
#include <iostream>
#define STRIP_FLAG_HELP 1
#include <gflags/gflags.h>

using namespace std;

DEFINE_string(inipath, "../conf/setup.ini", "program configure file");
//DEFINE_string(i, "../conf/setup.ini", "program configure file");
DEFINE_int32(port, 9090, "program listen port");
//DEFINE_int32(p, 9090, "program listen port");
DEFINE_bool(daemon, true, "run daemon mode");
DEFINE_bool(d, true, "run daemon mode");
DEFINE_string(name, "noname", "specified app name");
//DEFINE_string(n, "noname", "specified app name");

// void SetUsageMessage()
// {

// }

int main(int argc, char** argv)
{
  gflags::ParseCommandLineFlags(&argc, &argv, true);

  cout << "initpath: " << FLAGS_inipath << endl;
  cout << "port: " << FLAGS_port << endl;
  cout << "daemon: " << (FLAGS_daemon ? "true" : "false") << endl;
  cout << "daemon: " << (FLAGS_d ? "true" : "false") << endl;
  cout << "name: " << FLAGS_name << endl;
  cout << "good luck and good bye!" << endl;

  gflags::ShutDownCommandLineFlags();
  return 0;
}
