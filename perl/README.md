README
======

# 2020/09/09

if 'ag' or 'ack-grep' is installed, use
```
ag [string to search]
ack [string to search]
```

# 2008/07/25

```/w*.pl``` checked
```/win32/*``` checked

# 2008/07/24

```/i*.pl``` checked

# 2008-03-13

解決多層子目錄尋找特定字串的方法 (win32 ok)
```
find . -iname '*.pl' | xargs grep -i 'string_to_find'
```

# 2008-02-28

1. 現在有很多 script 裡面已經有 pod 了，改用 perldoc 來看吧！
2. use strict; 之外，還可以再加上 use warnings

# 2006-11-30

1. 使用 C xxx.pl 可以看 perl script 裡面的注意事項
// c is c.bat
// perl script 裡面 #@ 就是注意事項的註解行。
2. 可以用 run.bat 執行 perl script
3. FindTr/ 下面是找出 Tr() 的 script
4. perl_hash/ 下的 script 是練習寫 perl hash 相關的
5. 請愛用 use strict; 'my', 'local'


# 2003-03-16

注意:
    '||' 與 'or' 的差別在於，運算優先順序不同。
    or 是最低的

    ∴   $a = $ARGV[0] or "abc"; =>  ($a = $ARGV[0]) or "abc";
    and, $a = $ARGV[0] || "abc"; =>  $a = ($ARGV[0] || "abc");

perl 5.10, 可以用 $a = $ARGV[0] // "abc";
