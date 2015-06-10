LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := hello
LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES :=  \
    hello.c

LOCAL_C_INCLUDES := external/jpeg
LOCAL_CFLAGS := $(LOCAL_C_INCLUDES:%=-I%)
LOCAL_LDLIBS := -L$(SYSROOT)/usr/lib -lld -ljpeg

LOCAL_SHARED_LIBRARIES:= libcutils libutils libjpeg

#include $(BUILD_SHARED_LIBRARY)
include $(BUILD_EXECUTABLE)

