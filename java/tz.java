import java.util.*;

class tz {
	public static void main(String[] argv)  {
         String[] ids = TimeZone.getAvailableIDs();

         for (int i = 0; i < ids.length; i++)
             System.out.println(ids[i].toString());

	}
}
