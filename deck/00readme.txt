在 liar game 2 第二集後半的 17 pokers
17張牌共有 6188 種組合 C(17,5)
有八種牌型分別是

4 Aces, 4 Kings, 4 Queens, 4 Jacks and a Joker
joker card is wild card

1. 5 cards (one joker)            // five-of-a-kind
2. royal straight flush (joker?)  // royal flush
3. 4 cards (no joker)             // four-of-a-kind
4. full house (3-of-1 + 1pair)
5. straight (joker)
6. 3 cards               // three-of-a-kind
7. 2 pairs
8. 1 pair

在此遊戲中，至少會有 1pair 可拿，
各牌型出現的機率為 (百分比)：

1: 0.0646 / 100
2: 0.0646 / 100
3: 0.7757 / 100
4: 4.6542 / 100
5: 4.0724 / 100
6: 15.5139 / 100
7: 31.4156 / 100
8: 43.4389 / 100
總計: 100.0000 / 100

上述的統計，特別要注意的是，鬼牌並沒有提升 1pair 成為 3cards，
或是 2pair 成為 full house。

如果鬼牌如此使用，則出現機率將成為：

1.txt: 4  0.0646 / 100
2.txt: 4  0.0646 / 100
3.txt: 48  0.7757 / 100
4.txt: 504  8.1448 / 100	(216joker)
5.txt: 252  4.0724 / 100
6.txt: 2112  34.1306 / 100
7.txt: 1728  27.9250 / 100
8.txt: 1536  24.8222 / 100
總計: 6188  100.0000 / 100

files
=====
17poker.py	init deck and deal 5 cards to 4 players
cmb.py		list all combinations for C(17,5)
fisher_yates_shuffle.py		provide shuffle function
num-to-desk.pl	to determine what type of cards


reference:
http://blog.yam.com/mehome0619/article/28938038
http://en.wikipedia.org/wiki/In_shuffle
http://en.wikipedia.org/wiki/Faro_shuffle

http://en.wikipedia.org/wiki/List_of_poker_hands

52P5
52C5 = 2,598,960

* straight flush
  all same suit
  (4*10) / (2598960) = 0.0015%

  5♦ 4♦ 3♦ 2♦ A♦ ==> steel wheel
  An ace-high straight flush such as A♦ K♦ Q♦ J♦ 10♦ is known as a royal flush
  total 4 royal flush

* four of a kind
  (13C1*4C4 * 12C1*4C1)
  --------------------- = 0.024%
        52C5

* full house
flush
straight
three of a kind
two pair
one pair
high card
