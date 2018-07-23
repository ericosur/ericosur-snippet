// toolbox.hpp

#ifndef __TOOL_BOX_HPP__
#define __TOOL_BOX_HPP__

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

#include <openssl/md5.h>
#include <openssl/sha.h>

namespace toolbox
{

void dump(const uint8_t* buffer, size_t size);

/** \param buffer [in] byte buffer to calculate MD5
	\param buffer_size [in] buffer size in bytes
	\param md5_hash [out] byte buffer of hash digest
	\brief Calculate MD5 digest form a give buffer
*/
int Md5(const uint8_t* buffer, const size_t size, uint8_t *hash);
int Sha(const uint8_t* buffer, const size_t size, uint8_t *hash);
int Sha1(const uint8_t* buffer, const size_t size, uint8_t *hash);
int Sha256(const uint8_t* buffer, const size_t size, uint8_t *hash);

}   // namespace toolbox

#endif	// __TOOL_BOX_HPP__
