#ifndef __FLOCK_H__
#define __FLOCK_H__

/**
    \file flock.h
    \brief header file for flock()
**/
#include <stdio.h>

FILE *util_file_lock_wait(const char *fname);
int util_file_unlock_wait(FILE  *lockf);
int util_file_lock(const char *name);
int util_test_file_lock(const char *name);

#endif  // __FLOCK_H__
