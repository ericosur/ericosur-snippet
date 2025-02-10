// Crypt.cs
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

public class Crypt
{
	public static string Encrypt(string text)
	{
		ICryptoTransform cryptoTransform = new RijndaelManaged
		{
			BlockSize = 128,
			KeySize = 128,
			Padding = PaddingMode.Zeros,
			Mode = CipherMode.CBC,
			Key = Encoding.UTF8.GetBytes(AesKey),
			IV = Encoding.UTF8.GetBytes(AesIV)
		}.CreateEncryptor();
		MemoryStream memoryStream = new MemoryStream();
		CryptoStream cryptoStream = new CryptoStream(memoryStream, cryptoTransform, CryptoStreamMode.Write);
		byte[] bytes = Encoding.UTF8.GetBytes(text);
		cryptoStream.Write(bytes, 0, bytes.Length);
		cryptoStream.FlushFinalBlock();
		byte[] array = memoryStream.ToArray();
		return Convert.ToBase64String(array);
	}

	public static string Decrypt(string cryptText)
	{
		ICryptoTransform cryptoTransform = new RijndaelManaged
		{
			BlockSize = 128,
			KeySize = 128,
			Padding = PaddingMode.Zeros,
			Mode = CipherMode.CBC,
			Key = Encoding.UTF8.GetBytes(AesKey),
			IV = Encoding.UTF8.GetBytes(AesIV)
		}.CreateDecryptor();
		string text;
		try
		{
			byte[] array = Convert.FromBase64String(cryptText);
			byte[] array2 = new byte[array.Length];
			MemoryStream memoryStream = new MemoryStream(array);
			CryptoStream cryptoStream = new CryptoStream(memoryStream, cryptoTransform, CryptoStreamMode.Read);
			cryptoStream.Read(array2, 0, array2.Length);
			text = Encoding.UTF8.GetString(array2);
		}
		catch
		{
			text = "SaveDataCrash";
		}
		return text;
	}

	private const string AesIV = "jCddaOybW3zEh0Kl";

	private const string AesKey = "giVJrbHRlWBDIggF";
}
