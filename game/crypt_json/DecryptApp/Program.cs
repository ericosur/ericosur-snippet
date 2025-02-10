// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");

// Program.cs
using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length != 3)
        {
            Console.WriteLine("Usage: DecryptApp -c|-d <inputFile> <outputFile>");
            Console.WriteLine("  -c: encrypt the input file");
            Console.WriteLine("  -d: decrypt the input file");
            return;
        }

        string option = args[0];
        string inputFile = args[1];
        string outputFile = args[2];

        try
        {
            if (option == "-c")
            {
                // Read the plaintext content from the input file
                string plaintextContent = File.ReadAllText(inputFile);

                // Encrypt the content
                string encryptedContent = Crypt.Encrypt(plaintextContent);

                // Write the encrypted content to the output file
                File.WriteAllText(outputFile, encryptedContent);

                Console.WriteLine("Encryption successful. Encrypted content written to " + outputFile);
            }
            else if (option == "-d")
            {
                // Read the encrypted content from the input file
                string encryptedContent = File.ReadAllText(inputFile);

                // Decrypt the content
                string decryptedContent = Crypt.Decrypt(encryptedContent);

                // Write the decrypted content to the output file
                File.WriteAllText(outputFile, decryptedContent);

                Console.WriteLine("Decryption successful. Decrypted content written to " + outputFile);
            }
            else
            {
                Console.WriteLine("Invalid option. Use -c to encrypt or -d to decrypt.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }
}
