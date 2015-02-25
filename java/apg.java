import java.math.BigInteger;
import java.security.AlgorithmParameterGenerator;
import java.security.AlgorithmParameters;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import javax.crypto.spec.DHParameterSpec;
import java.security.SecureRandom;

// try to play DH
// http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
public class apg {

    static BigInteger P = BigInteger.ZERO;
    static BigInteger G = BigInteger.ZERO;
    static final int PARAMETER_LEN = 512;
    static final int SECRETKEY_LEN = 20;

    // init P and G for DH
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

        // both P and G are public
        System.out.println("P=" + P.toString() + " len: " + P.toString().length());
        System.out.println("G=" + G.toString());
        //System.out.println("L=" + dhpara.getL());
    }

    private static BigInteger pass_one(BigInteger a) {
        BigInteger A = G.modPow(a, P);
        return A;
    }

    static class SecretParty {
        private BigInteger a = BigInteger.ZERO;
        private static final boolean DEBUG = false;
        SecretParty() {
            a = new BigInteger(SECRETKEY_LEN, new SecureRandom());
        }
        public BigInteger get() {
            if (DEBUG) {
                System.out.println("a = " + a.toString());
            }
            return a;
        }
    }


    public static void test() {
        try {
            init();
        } catch (Exception e) {
            System.out.println("test(): shit happens: " + e.getMessage());
            return;
        }

        SecretParty alice = new SecretParty();
        SecretParty bob = new SecretParty();

        // A is public and give to bob
        BigInteger A = pass_one(alice.get());
        System.out.println("A = G^a mod P = " + A.toString());
        // B is public and give to alice
        BigInteger B = pass_one(bob.get());
        System.out.println("B = G^b mod P = " + B.toString());

        // alice part
        // s = B^a
        BigInteger sa = B.modPow(alice.get(), P);
        System.out.println("sa:" + sa.toString());

        // bob part
        // s = A^b
        BigInteger sb = A.modPow(bob.get(), P);
        System.out.println("sb:" + sb.toString());

        if (!sa.equals(sb)) {
            System.out.println("sa != sb");
        }

        System.out.println("sa.bitLength(): " + sa.bitLength());
        System.out.println("sa.hashCode(): " + sa.hashCode());
        System.out.println("sb.hashCode(): " + sb.hashCode());
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

