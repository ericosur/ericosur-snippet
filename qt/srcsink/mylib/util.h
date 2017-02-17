/**
 * \file util.h
 */

#ifndef __MYLIB_UTIL_H__
#define __MYLIB_UTIL_H__

#define LOCAL_SHM_KEY    0x0001BABE

int util_shm_write( int key, int shm_size, void *data);
void * util_shm_read( int key, int shm_size);

#endif  // __MYLIB_UTIL_H__
