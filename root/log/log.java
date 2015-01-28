// just a stupid for-loop vs Math.log(), Math.log10()
// javac log.java && java log
//
public class log {
    public static void main(String[] argv) {
        double vals[] = {1, 2.7182818284, 10, 100, 300};
        for (double v : vals) {
            System.out.printf("%.5f: %.5f -- %.5f\n",
                v, Math.log(v), Math.log10(v));
        }
    }
}
