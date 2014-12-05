LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SRC_FILES :=  \
    hello.c

LOCAL_MODULE := hello

LOCAL_SHARED_LIBRARIES:= libcutils libutils

#include $(BUILD_SHARED_LIBRARY)
include $(BUILD_EXECUTABLE)

