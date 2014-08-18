// example from http://java.sun.com/developer/technicalArticles/releases/1.4regex/

/* This class removes control characters from a named
*  file.
*/
import java.util.regex.*;
import java.io.*;

public class Control {
    public static void main(String[] args)
                                 throws Exception {

        //Create a file object with the file name
        //in the argument:
        File fin = new File("fileName1");
        File fout = new File("fileName2");
        //Open and input and output stream
        FileInputStream fis =
                          new FileInputStream(fin);
        FileOutputStream fos =
                        new FileOutputStream(fout);

        BufferedReader in = new BufferedReader(
                       new InputStreamReader(fis));
        BufferedWriter out = new BufferedWriter(
                      new OutputStreamWriter(fos));

	// The pattern matches control characters
        Pattern p = Pattern.compile("{cntrl}");
        Matcher m = p.matcher("");
        String aLine = null;
        while((aLine = in.readLine()) != null) {
            m.reset(aLine);
            //Replaces control characters with an empty
            //string.
            String result = m.replaceAll("");
            out.write(result);
            out.newLine();
        }
        in.close();
        out.close();
    }
}
