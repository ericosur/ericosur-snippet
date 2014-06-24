LOCAL_PATH:= $(call my-dir)

include $(CLEAR_VARS)
LOCAL_C_INCLUDES += $(LOCAL_PATH)/../../../external/openssl/include
LOCAL_SRC_FILES:= keybox_decrypt.cpp
LOCAL_SHARED_LIBRARIES := libcutils libcrypto
LOCAL_MODULE_TAGS := optional

BUILD_AS_EXE := false

ifeq ($(BUILD_AS_EXE), true)

LOCAL_CFLAGS := -DDEBUG_PRINT
LOCAL_SRC_FILES += runner.c
LOCAL_MODULE := kbxdec
include $(BUILD_EXECUTABLE)

else

LOCAL_CFLAGS := -DKBXLIBRARY
LOCAL_MODULE:= libkbxdec
include $(BUILD_STATIC_LIBRARY)

endif
