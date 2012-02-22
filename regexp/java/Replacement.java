// example from http://java.sun.com/developer/technicalArticles/releases/1.4regex/

/*
 * This code writes "One dog, two dogs in the yard."
 * to the standard-output stream:
 */
import java.util.regex.*;

public class Replacement {
    public static void main(String[] args)
                         throws Exception {
        // Create a pattern to match cat
        Pattern p = Pattern.compile("cat");
        // Create a matcher with an input string
        Matcher m = p.matcher("one cat," +
                       " two cats in the yard");
        StringBuffer sb = new StringBuffer();
        boolean result = m.find();
        // Loop through and create a new String
        // with the replacements
        while(result) {
            m.appendReplacement(sb, "dog");
            result = m.find();
        }
        // Add the last segment of input to
        // the new String
        m.appendTail(sb);
        System.out.println(sb.toString());
    }
}
