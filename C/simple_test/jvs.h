#ifndef __UTIL_JVS_H__
#define __UTIL_JVS_H__

// jsnprintf(), like snprintf(), will help put escape to avoid json syntax
// error into output string buffer
//
// [in] out: result buffer
// [in] n:   sizeof result buffer, will return <= 0 if failed
// [in] format and ..., use it as printf()
//
// for example:
//
// void test()
// {
//     const size_t BUFFERSIZE = 512;
//     char buf[BUFFERSIZE];
//     const char test[] = "everything \"is\" ok";

//     int res = jsnprintf(buf, BUFFERSIZE-1,
//         "{'string': %s, 'integer': %d, 'boolean': %b}", test, 3, 1);
//     if (res > 0) {
//         printf("JSON result: %s\n", buf);
//     } else {
//         printf("Fail\n");
//     }
// }
//
//
int jsnprintf(char *out, size_t n, const char *format, ...)

#endif  // __UTIL_JVS_H__
