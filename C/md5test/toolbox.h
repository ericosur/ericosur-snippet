// toolbox.hpp

#ifndef __TOOL_BOX_HPP__
#define __TOOL_BOX_HPP__

#include <stdio.h>
#include <openssl/md5.h>

typedef unsigned char byte;

/** \param buffer [in] byte buffer to calculate MD5
	\param buffer_size [in] buffer size in bytes
	\param md5_hash [out] byte buffer of hash digest
	\brief Calculate MD5 digest form a give buffer
*/
int CalculateBufferMD5(byte* buffer, size_t buffer_size, byte *md5_hash);

#endif	// __TOOL_BOX_HPP__
