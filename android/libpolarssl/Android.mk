LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

include $(LOCAL_PATH)/polarssl/srcfiles.mk

LOCAL_SRC_FILES += \
	$(POLAR_SOURCES) 

LOCAL_C_INCLUDES += $(LOCAL_PATH)/polarssl/include

LOCAL_CFLAGS += -D_FILE_OFFSET_BITS=64 -Wall -W -Wdeclaration-after-statement
#LOCAL_SHARED_LIBRARIES := libcutils
LOCAL_MODULE_TAGS := optional

LOCAL_MODULE := libpolarssl

include $(BUILD_STATIC_LIBRARY)

