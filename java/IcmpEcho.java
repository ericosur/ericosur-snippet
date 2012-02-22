import java.net.*;
import com.sun.security.auth.module.UnixSystem;

// reference from: http://blas.phemo.us/articles/2008/05/12/root-permissions-required-to-send-icmp-echo-request-from-java-using-java-net-inetaddress


/**
 *
 * @author Tres Wong-Godfrey
 */
public class IcmpEcho {

    public static void main(String[] args) {
        String host = null;
        int timeOut = 3000;
        boolean isUp = false;
        boolean validRequest = true;
        String output = "";
        long uid = -1;

        UnixSystem user = new UnixSystem();
        uid = user.getUid();

        if (args.length != 1) {
            System.out.println("ICMP echo check requires a single argument -- the hostname");
            System.exit(1);
        }

        if (uid != 0) {
            System.out.println(" ICMP echo check requires root permissions");
            System.exit(2);

        }

        host = args[0];
        try {
            isUp = InetAddress.getByName(host).isReachable(timeOut);
        } catch (SecurityException $e) {
            System.out.println(" ICMP echo check requires root permissions");
            validRequest = false;

        } catch (UnknownHostException $e) {
            System.out.println(" Unknown host: " + host);
            validRequest = false;

        } catch (Exception $e) {
            System.out.println("Unknown error");
            $e.printStackTrace();
            validRequest = false;

        }

        if (validRequest == true) {
            output = (isUp == true) ? host + " is up" : host + " is down";
        }
        System.out.println(output);

    }
}

