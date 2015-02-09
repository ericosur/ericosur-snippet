//import java.security.SecureRandom;
import java.util.UUID;

public class TestUuid {

    private static void test() {
        int rep = 10;
        for (int i=0; i<rep; i++) {
            System.out.println("uuid: " + UUID.randomUUID().toString());
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

