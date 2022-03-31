// TestBytes.java
//


import java.nio.charset.StandardCharsets;

public class TestBytes {

    private static final byte[] HEX_ARRAY = "0123456789ABCDEF".getBytes(StandardCharsets.US_ASCII);
    private static final String TEST_HEX_STRING = "624540FD";

    public static byte[] hexStringToBytes(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                                 + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }

    public static String bytesToHexString(byte[] bytes) {
        byte[] hexChars = new byte[bytes.length * 2];
        for (int j = 0; j < bytes.length; j++) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = HEX_ARRAY[v >>> 4];
            hexChars[j * 2 + 1] = HEX_ARRAY[v & 0x0F];
        }
        return new String(hexChars, StandardCharsets.UTF_8);
    }

    private static void show(String msg) {
        System.out.println(msg);
    }

    private static void test(String hex) {
        String msg = "";
        show("Input: " + hex);
        byte[] bytes = hexStringToBytes(hex);
        show("it is not good to print it directly...");
        msg = "bytes: " + bytes;
        show(msg);
        msg = "hex: " + bytesToHexString(bytes);
        show(msg);
    }

    public static void main(String[] args) {
        System.out.println("main()");
        test(TEST_HEX_STRING);
        test("E69C83E8ADB0E9968BE5A78B");
    }
}
