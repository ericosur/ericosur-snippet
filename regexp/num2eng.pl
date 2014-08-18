#!/usr/bin/perl
#
#rex[at]zhasm[dot]com
#13 Feb 2009 on perl 5.10 and Ubuntu 8.10
#
# from
# http://iregex.org/blog/convert-digits-to-english-value.html
#

@single=(
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen"
);
@tens=(
    "",
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
);
@scale=(
    "",
    "Thundsand",
    "Million",
    "Billion",
    "Trillion",
    "Quadrillion",
    "Quintillion",
    "Sextillion",
    "Septillion",
    "Octillion",
    "Nonillion",
    "Decillion",
    "Undecillion",
    "Duodecillion",
    "Tredecillion",
    "Quattuordecillion",
    "Quindecillion",
    "Sexdecillion",
    "Septendecillion",
    "Octodecillion",
    "Novemdecillion",
    "Vigintillion"
);
sub dot
{
    my ($dot)=@_;
    if (length($dot)==2)
    {
        #$dot=1*$dot;
        if ($dot<20)
        {
            return $single[$dot];
        }
        else
        {
            $ten=int($dot/10);
            $extra=$dot-$ten*10;
            return "$tens[$ten] $single[$extra]";
        }
    }
    elsif (length($dot)==1)
    {
        return "$tens[$dot]";
    }
}
sub debug{
    print @_;
}
sub hundred{
    my ($number)=@_;
    $result="";
    if ($number>999)
    {
        debug("too large");
        return ;
    }
    my $c=int ($number/100);
    my $b=int(($number-$c*100)/10);
    my $a=$number % 10;
    $cc="";
    $bb="";
    $aa="";
    if ($c)
    {
        $cc="$single[$c] Hundred";
    }
    if ($a)
    {
        if ($b>=2)
        {
            $bb="$tens[$b]-$single[$a]";
        }
        elsif ($b<=1)
        {
            $bb=$single[$b*10+$a];
        }
    }
    if (!$a)
    {
        if ($b>=2)
        {
            $bb="$tens[$b]";
        }
        elsif ($b<=1)
        #includeing the condition when $b==0;
        {
            $bb=$single[$b*10];
        }
    }
    if ($c and ($a or $b))
    {
        return "$cc and $bb";
    }
    elsif($c and ($a==0 and $b==0))
    {
        return $cc;
    }
    elsif(!$c)
    {
        return  "and $bb";
    }
}

sub integer{
    my ($money)=@_;
    $index=0;
    $string="";
    $flag=1;
    while ($flag)
    {
        $small=0;
        if ($money<1000 and $money>0)
        {
            $small=$money;
            $flag=0;
        }
        elsif ($money>=1000)
        {
            $small=$money % 1000;
            $money=int($money/1000);
        }
        if ($small)
        {
            $string=hundred($small)." $scale[$index] ".$string;
        }
        $index++;
    }
    $string =~ s/\s+$//;
    $string =~ s/^\s+//;
    $string =~ s/^and\s+//i;
    $string;
}

sub convert{
    my ($digits)=@_;
    my $dot=0.0;
    my $integer=0;
    my $result="";
    $digits =~ s/[-,_' ]//g;
    if ($digits =~ /(\d*)\.(\d*)/)
    {
        $integer=$1;
        $dot=$2;
    }
    elsif ($digits =~ /(\d+)/)
    {
        $integer=$1;
    }
    if ($integer)
    {
        $result .= integer($integer);
    }
    if ($dot and $integer)
    {
        if ($dot==1)
        {
            $result .= " and ". dot($dot)." Cent";
        }
        elsif ($dot>1)
        {
             $result .= " and ". dot($dot)." Cents";
        }
    }
    elsif ($dot and $integer==0)
    {
        if ($dot==1)
        {
            $result .= dot($dot)." Cent";
        }
        elsif ($dot>1)
        {
             $result .= dot($dot)." Cents";
        }
    }
    $result="Total: Say US Dollars ".$result." Only.";
}

my ($money) = @ARGV;
print $line=convert($money)."\n";