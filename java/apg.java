import java.math.BigInteger;
import java.security.AlgorithmParameterGenerator;
import java.security.AlgorithmParameters;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import javax.crypto.spec.DHParameterSpec;

// try to play DH
// http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
public class apg {

    static BigInteger P = BigInteger.ZERO;
    static BigInteger G = BigInteger.ZERO;
    static final int nlen = 512;

    // init P and G for DH
    public static void init() throws Exception {
        KeyPairGenerator gen = null;
        try {
            gen = KeyPairGenerator.getInstance("DH");
        } catch (NoSuchAlgorithmException e) {
            System.out.println(e.getMessage());
        }
        AlgorithmParameterGenerator algo = AlgorithmParameterGenerator.getInstance("DH");
        algo.init(nlen, new SecureRandom());
        AlgorithmParameters algopara = algo.generateParameters();
        DHParameterSpec dhpara = algopara.getParameterSpec(DHParameterSpec.class);

        gen.initialize(dhpara);
        KeyPair key = gen.generateKeyPair();

        P = dhpara.getP();
        G = dhpara.getG();

        // both P and G are public
        System.out.println("P=" + P.toString());
        System.out.println("G=" + G.toString());
        //System.out.println("L=" + dhpara.getL());
    }

    private static BigInteger pass_one(BigInteger a) {
        BigInteger A = G.modPow(a, P);
        return A;
    }

    static class Alice {
        public static BigInteger get() {
            BigInteger a = new BigInteger("41");
            return a;
        }
    }
    static class Bob {
        public static BigInteger get() {
            BigInteger b = new BigInteger("71");
            return b;
        }
    }

    private static BigInteger alice() {
        BigInteger A = pass_one(Alice.get());
        System.out.println("A = G^a mod P = " + A.toString());
        return A;
    }
    private static BigInteger bob() {
        BigInteger B = pass_one(Bob.get());
        System.out.println("B = G^b mod P = " + B.toString());
        return B;
    }

    public static void test() {
        try {
            init();
        } catch (Exception e) {
            System.out.println("test(): shit happens: " + e.getMessage());
            return;
        }

        BigInteger A = alice(); // A is public and give to bob
        BigInteger B = bob();   // B is public and give to alice

        // alice part
        // s = B^a
        BigInteger sa = B.modPow(Alice.get(), P);
        //System.out.println("sa:" + sa.toString());

        // bob part
        // s = A^b
        BigInteger sb = A.modPow(Bob.get(), P);
        //System.out.println("sb:" + sb.toString());

        if (sa != sb) {
            System.out.println("sa != sb");
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

