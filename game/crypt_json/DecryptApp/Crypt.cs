// Crypt.cs
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

// Token: 0x020001BB RID: 443
public class Crypt
{
	// Token: 0x06000950 RID: 2384 RVA: 0x00046720 File Offset: 0x00044B20
	public static string Encrypt(string text)
	{
		ICryptoTransform cryptoTransform = new RijndaelManaged
		{
			BlockSize = 128,
			KeySize = 128,
			Padding = PaddingMode.Zeros,
			Mode = CipherMode.CBC,
			Key = Encoding.UTF8.GetBytes("giVJrbHRlWBDIggF"),
			IV = Encoding.UTF8.GetBytes("jCddaOybW3zEh0Kl")
		}.CreateEncryptor();
		MemoryStream memoryStream = new MemoryStream();
		CryptoStream cryptoStream = new CryptoStream(memoryStream, cryptoTransform, CryptoStreamMode.Write);
		byte[] bytes = Encoding.UTF8.GetBytes(text);
		cryptoStream.Write(bytes, 0, bytes.Length);
		cryptoStream.FlushFinalBlock();
		byte[] array = memoryStream.ToArray();
		return Convert.ToBase64String(array);
	}

	// Token: 0x06000951 RID: 2385 RVA: 0x000467C8 File Offset: 0x00044BC8
	public static string Decrypt(string cryptText)
	{
		ICryptoTransform cryptoTransform = new RijndaelManaged
		{
			BlockSize = 128,
			KeySize = 128,
			Padding = PaddingMode.Zeros,
			Mode = CipherMode.CBC,
			Key = Encoding.UTF8.GetBytes("giVJrbHRlWBDIggF"),
			IV = Encoding.UTF8.GetBytes("jCddaOybW3zEh0Kl")
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

	// Token: 0x0400095F RID: 2399
	private const string AesIV = "jCddaOybW3zEh0Kl";

	// Token: 0x04000960 RID: 2400
	private const string AesKey = "giVJrbHRlWBDIggF";
}
