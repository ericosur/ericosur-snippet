import java.math.BigInteger;
import java.security.AlgorithmParameterGenerator;
import java.security.AlgorithmParameters;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import javax.crypto.spec.DHParameterSpec;

public class algorithm_para {

    public static BigInteger P = new BigInteger("0");
    public static BigInteger G = new BigInteger("0");
    public static final int PARAMETER_LEN = 512;

    public static void init() throws Exception {
        KeyPairGenerator gen = null;
        try {
            gen = KeyPairGenerator.getInstance("DH");
        } catch (NoSuchAlgorithmException e) {
            System.out.println(e.getMessage());
        }
        AlgorithmParameterGenerator algo = AlgorithmParameterGenerator.getInstance("DH");
        algo.init(PARAMETER_LEN, new SecureRandom());
        AlgorithmParameters algopara = algo.generateParameters();
        DHParameterSpec dhpara = algopara.getParameterSpec(DHParameterSpec.class);

        gen.initialize(dhpara);
        KeyPair key = gen.generateKeyPair();

        P = dhpara.getP();
        G = dhpara.getG();

        System.out.println("P=" + P.toString());
        System.out.println("G=" + G.toString());
        System.out.println("L=" + dhpara.getL());
    }

    public static void test() {
        try {
            init();
        } catch (Exception e) {
            System.out.println("test(): shit happens: " + e.getMessage());
            return;
        }
    }

public static void main(String[] args) {
        System.out.println("hello world");
        try {
            test();
        } catch (Exception e) {
            System.out.println("shit happens: " + e.getMessage());
        }
    }
}

