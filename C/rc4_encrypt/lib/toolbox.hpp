// \file toolbox.hpp
#ifndef __TOOL_BOX_HPP__
#define __TOOL_BOX_HPP__

#include <stdio.h>

/// a magic string at the beginning of header
#define MY_MAGIC_NUMBER	"RasmusMagicHead\0"
/// md5sum length = 16 bytes
#define MY_MD5_DIGEST_LENGTH		16
#define MY_MAGIC_NUMBER_LENGTH  	16
#define MY_LOCAL_RESERVED_LENGTH	MY_MD5_DIGEST_LENGTH
#define MY_LARGE_PRESERVED_LENGTH	128

typedef unsigned char byte;

/** \struct Header ToolBox.hpp
*/
typedef struct Header
{
	/// usu. MY_MAGIC_NUMBER

	byte	MagicNumber[MY_MAGIC_NUMBER_LENGTH];	/// usu. MY_MAGIC_NUMBER
	int 	HeaderSize;			/// the header size including the file name string
	int 	FileNameLength;		/// the length of file name
	int 	Reserved1;			/// reserved
	size_t	FileSize;			/// the file size
	byte	reserved2[16];		/// reserved
	byte	header_md5[MY_MD5_DIGEST_LENGTH];		/// header_md5
	byte	file_md5[MY_MD5_DIGEST_LENGTH];		/// the MD5 of file
	char*	FileName;			/// the name of file
} Header_struct;


/** \param fptr [in] file pointer
	\param md5_hash [out] byte buffer of hash digest
	\param total_read [out] bytes already read
	\brief Calculate MD5 digest form a file pointer
*/
int CalculateFileMD5(FILE *fptr, byte *md5_hash, size_t& total_read);


/** \param buffer [in] byte buffer to calculate MD5
	\param buffer_size [in] buffer size in bytes
	\param md5_hash [out] byte buffer of hash digest
	\brief Calculate MD5 digest form a give buffer
*/
int CalculateBufferMD5(byte* buffer, size_t buffer_size, byte *md5_hash);

/** \param fptr [in] file pointer
	\param sha1_hash [out] byte buffer of hash digest
	\param total_read [out] bytes already read
	\brief calculate SHA1 digest from a file pointer
*/
int CalculateFileSHA1(FILE *fptr, byte *sha1_hash, size_t& total_read);

/** \param hash [in] byte buffer of hash digest
	\param len	[in] length of hash buffer
	\brief print a blob as continuos string
*/
void PrintHashValue(const byte *hash, const int len);

/** \param in [in] byte buffer for encoding
	\param cipher [out] byte buffer already encrypted
	\param len [in] size of both in and out
	\brief perform RC4 on input buffer
*/
void PerformRC4(const byte* in, byte* cipher, size_t len);

/** \param record_header_size [in] the size of header recorded in the header section

	calculate the actural header size because of
	the actual size would be the 16-aligning
*/
int GetActualHeaderSize(int record_header_size);

/** \param in [in] input file stream
	\param out [in] output file stream
	\brief encrypt an input file pointer by RC4
*/
void EncryptFileByRC4(FILE *in, FILE *out);

/** \param in [in] the header struct
	\param out [out] the calculate md5
	\brief calculate the md5 for header
*/
void VerifyHeaderMD5(const Header& header, byte* recorded_md5);

/** \param in [in] the header struct
	\brief check the magic header
*/
bool verify_magic(const Header_struct& header);

#endif	// __TOOL_BOX_HPP__
