import java.io.*;

/*
   reference from: http://www.javaworld.com.tw/jute/post/view?bid=29&id=31477&sty=3&age=0&tpg=1&ppg=1#31477
*/
 
public class JPing {
  public static void main(String[] args) {
    Runtime runtime = Runtime.getRuntime();
    Process process = null;
    String line = null;
    InputStream is = null;
    InputStreamReader isr = null;
    BufferedReader br = null;
    String ip = "127.0.0.1"; //要Ping 的IP位址
    try {
      process = runtime.exec("ping -c 3 " + ip);
      is = process.getInputStream();
      isr = new InputStreamReader(is);
      br = new BufferedReader(isr);
      while ( (line = br.readLine()) != null) {
        System.out.println(line);
        System.out.flush();
      }
      is.close();
      isr.close();
      br.close();
      System.out.println("Java 呼叫 ping 程式，執行完畢！");
    }
    catch (IOException e) {
      System.out.println(e);
      runtime.exit(0);
    }
  }//end main method
}//end class

