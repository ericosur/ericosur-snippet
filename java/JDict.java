import java.net.*;
import java.io.*;
import java.util.regex.*;

/**
 * TextBrowser - URL/text mode getter.
 * Display the contents of a text-only URL
 * @author	Ian Darwin, http://www.darwinsys.com/
 */
public class JDict {

	public static void main(String[] av) {
		if (av.length == 0) {
			System.err.println("Usage: TextBrowser URL [...]");
			System.exit(1);
		}
		else for (int i=0; i<av.length; i++) {
			String doc = getDocument( composeQueryURL(av[i]) );
			String res = composeResult(doc);
			System.out.println(res);
		}
	}

	public static String composeQueryURL(String word)  {
		String dictURL = "http://tw.dictionary.yahoo.com/search?p=" + word;
		//System.out.println(dictURL);
		return dictURL;
	}

	/** Show one document, by filename */
	public static String getDocument(String loc) {
		URL webURL = null;
		String total = "";
		try {
			//System.err.println("*** Loading " + loc + "... ***");
			webURL = new URL(loc);
			BufferedReader is = new BufferedReader(
				new InputStreamReader(webURL.openStream()) );
			String line;
			while ((line = is.readLine()) != null) {
				//System.out.println(line);
				total += line;
			}
			is.close();
		} catch (MalformedURLException e) {
			System.err.println("Load failed: " + e);
		} catch (IOException e) {
			System.err.println("IOException: " + e);
		}
		//System.out.println(total);
		return total;
	}

	public static String composeResult(String doc)  {
		String result = "";
		String divp = "<div class=p(\\w+)>(.*?)</div>";
		Pattern p = Pattern.compile(divp, Pattern.CASE_INSENSITIVE);
		Matcher m = p.matcher(doc);
		while ( m.find() )  {
			String type = m.group(1);
			String line = m.group(2);

		  	line.replaceAll("^\\s+", "");
		  	line.replaceAll("\\s+$", "");

		  	System.out.println(line);
/*
			if (type == "cixin")  {
				result +=
			}
*/
		}
		return "";
	}
}
