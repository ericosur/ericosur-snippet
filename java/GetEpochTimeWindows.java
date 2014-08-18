// reference from
// http://www.roseindia.net/java/java-get-example/get-epoch-windows.shtml

import java.util.Calendar;
import java.text.SimpleDateFormat;

public class GetEpochTimeWindows  {
    public static void  main(String arg[])  {
		try  {
			// Getting the current epoch time
			long epoch = System.currentTimeMillis() / 1000;
			System.out.println("Epoch time => "+ epoch);
			//  Convert from Readable date to epoch
			System.out.println("Parsed date=> "+
				new SimpleDateFormat("dd/MM/yyyy HH:mm:ss")
				.parse("01/01/1601 00:00:00"));
		}
		catch (Exception e)  {
			System.out.println(e.getMessage());
		}
	}
}
