fn main() {
    println!("Hello, Cargo!");

    let mut x = 5;
    println!("x = {}", x);

    const ONE_MINUTE: u32 = 60;
    println!("om = {}", ONE_MINUTE);

    x = 6 * ONE_MINUTE;
    println!("x = {}", x);

}
