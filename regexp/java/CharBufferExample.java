// example from http://java.sun.com/developer/technicalArticles/releases/1.4regex/

/*
 * Prints out the comments found in a .java file.
 */
import java.util.regex.*;
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.nio.channels.*;

public class CharBufferExample {
    public static void main(String[] args) throws Exception {
        // Create a pattern to match comments
        Pattern p =
			Pattern.compile("//.*$", Pattern.MULTILINE);
			//Pattern.compile("/\\*[^*]*\\*+([^/*][^*]*\\*+)*/|([^/\"']*(\"[^\"\\\\]*(\\\\[\\d\\D][^\"\\\\]*)*\"[^/\"']*|'[^'\\\\]*(\\\\[\\d\\D][^'\\\\]*)*'[^/\"']*|/+[^*/][^/\"']*)*)", Pattern.MULTILINE);
        // Get a Channel for the source file
        File f = new File("Replacement.java");
        FileInputStream fis = new FileInputStream(f);
        FileChannel fc = fis.getChannel();

        // Get a CharBuffer from the source file
        ByteBuffer bb =
            //fc.map(FileChannel.MAP_RO, 0, (int)fc.size());
            fc.map(FileChannel.MapMode.READ_ONLY, 0, (int)fc.size());
        Charset cs = Charset.forName("8859_1");
        CharsetDecoder cd = cs.newDecoder();
        CharBuffer cb = cd.decode(bb);

        // Run some matches
        Matcher m = p.matcher(cb);
        while (m.find())
            System.out.println("Found comment: "+m.group());
    }
}
