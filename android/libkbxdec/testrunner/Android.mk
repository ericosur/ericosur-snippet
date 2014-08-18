LOCAL_PATH:= $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SRC_FILES:= runner.c
LOCAL_STATIC_LIBRARIES := libkbxdec
LOCAL_SHARED_LIBRARIES := libcutils libcrypto
LOCAL_MODULE_TAGS := optional
LOCAL_CFLAGS := -DDEBUG_PRINT
LOCAL_LDLIBS := -lkbxdec

LOCAL_MODULE := kbxdec

include $(BUILD_EXECUTABLE)
