fn main() {
    let mut s = String::from("Hello, world!");
    let _postfix = String::from("Great!");

    println!("[{}] {}", s.len(), s);

    append(&mut s, "wtf!");
    println!("[{}] {}", s.len(), s);

    append(&mut s, &_postfix);
    println!("[{}] {}", s.len(), s);

}


fn append(s: &mut String, t: &str) {
    //println!("s = {}", s);
    //println!("len = {}", s.len());
    let r = " ".to_owned() + t;
    s.push_str(&r);
    //s.push_str(t);
    //println!("s = {}", s);
}
