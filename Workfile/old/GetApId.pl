#! /usr/bin/perl

#
# 2007/11/14 don't know what the purpose of this perl script
#

use File::Find; # 指揮 perl 至 perl 的主要目錄下尋找 File/Find.pm 這個
                # 模組，引入使用! 其中 :: 相當於 / 這個符號。

$idx=1;
@IDs = @tempIDs = ();
%table = ();
%def_table = ();

# directory path.
my $dir = shift || die "Please input full directory path.\n";

my $tmp1="All_IDS.csv";
my $tmp2="File_IDS.csv";



#open(file1, "> $tmp1") || die "$!\n";
#open(file2, "> $tmp2") || die "$!\n";

# visit all sub-directorys
for ($i=0; $i < 5; $i++)
{
   #printf "loop %d\n",$i;
   find(\&doit, $dir);
}

@tempIDs = sort @tempIDs;
#print @tempIDs,"\n";
print "Total, $#tempIDs\n";

for ($i=0; $i <= $#tempIDs; $i++)
{
   if($tempIDs[$i] ne $tempIDs[$i+1])
   {
      push @IDs, $tempIDs[$i];
   }
}

print "IDs\n";

foreach (@IDs)
{
   printf "0x%08.0X, \n",$_;
}
print "total IDs, ",$#IDs+1,"\n";

while (($File,$ID) = each %table)
{
   print "$File, ";
   if ($ID eq "None")
   {
      printf "None\n";
      next;
   }
   foreach (split(/ /,$ID))
   {
      printf "0x%08.0X, ",$_;
   }
   print "\n";
}
#print file2 "\n\n Total IDs, ",$#IDs+1,"\n";

#close(file1);
#close(file2);

sub doit {
	print_process_status($idx);

	if (/\.mfx$|\.bid$/i =~ split(/\//,$_))
	{
	   my $filename = $_;
	   my @val = (None);

	   #print "$_\n";
	   # Read only
		open(FHD, "$File::Find::name") || die "$!\n";
		while(<FHD>)
		{
			while ($_ =~ /0x([a-f0-9]+)|\"[\s+]?(\w*)[\s+]?\"/ig)
			{
				my $num = $1;
				my $str = $2;
				if (length($num) == 8)
				{
					if($val[0] eq "None")
					{
						$val[0] = hex("$num");
					}
					else
					{
						push @val, hex("$num");
					}
					push @tempIDs, hex("$num");
				}

				if (exists $def_table{$str})
				{
					if($val[0] eq "None")
					{
						$val[0] = $def_table{$str};
					}
					else
					{
						push @val,$def_table{$str};
					}
					#printf "%s found, value=0x%08.0X in file:%s\n",$str,$def_table{$str},$filename;
					push @tempIDs, $def_table{$str};
					#printf " 0x%08.0X added \n",$tempIDs[$#tempIDs];
				}
	      	}
	   }
		$table{$filename} = "@val";
		close(FHD);
	}
	elsif (/\.h$/i =~ split(/\//,$_))
	{
		#print "$_\n";
		#  Read only
		open(FHD, "$File::Find::name") || die "$!\n";
		while(<FHD>)
		{
			#format: #define name (value1 + value2)
			while ($_ =~ /\#define\s+(\w*)\s+[\(]?[\s+]?(\w*)[\s+]?[\+|\)]?[\s+]?(\w*)?[\s+]?[\)]?/ig)
			{
				#print $1,"  ",$2,"   ",$3,"\n";
				my $name = $1;
				my $value1 = $2;
				my $value2 = $3;
				my $tmp_value1 = 0;
				my $tmp_value2 = 0;

				next if (exists $def_table{$name});

				if ($name && $value1 && !$value2)
				{
					if ($value1 =~ /^[\d]/)
					{
						no warnings;
						if ($value1 =~ /^0x/i)
						{
							$tmp_value1 = hex("$value1");
						}
						elsif ($value1 =~ /^0/)
						{
							$tmp_value1 = oct("$value1");
						}
						else
						{
							$tmp_value1 = $value1;
						}
						$def_table{$name} = $tmp_value1;
						use warnings;
		            }
					if((exists $def_table{$value1}) && ($def_table{$value1} =~ /^[\d]/))
					{
						$def_table{$name} = $def_table{$value1};
					}
				}
				elsif ($name && $value1 && $value2)
				{
					if(((exists $def_table{$value1}) && ($def_table{$value1} =~ /^[\d]/)) &&
					((exists $def_table{$value2}) && ($def_table{$value2} =~ /^[\d]/)))
					{
						$def_table{$name} = $def_table{$value1} + $def_table{$value2};
					}
					elsif (((exists $def_table{$value1})
							&& ($def_table{$value1} =~ /^[\d]/))
							&& ($value2 =~ /^[\d]/))
					{
						if ($value2 =~ /^0x/i)
						{
							$tmp_value2 = hex("$value2");
						}
						elsif ($value2 =~ /^0/)
						{
							$tmp_value2 = oct("$value2");
						}
						else
	            		{
							$tmp_value2 = $value2;
						}
						$def_table{$name} = $def_table{$value1} + $tmp_value2;
					}
					elsif (($value1 =~ /^[\d]/) &&
					((exists $def_table{$value2}) && ($def_table{$value2} =~ /^[\d]/)))
					{
						if ($value1 =~ /^0x/i)
						{
						$tmp_value1 = hex("$value1");
						}
						elsif ($value1 =~ /^0/)
						{
							$tmp_value1 = oct("$value1");
						}
						else
						{
							$tmp_value1 = $value1;
						}
						$def_table{$name} = $tmp_value1 + $def_table{$value2};
					}
					elsif(($value1 =~ /^[\d]/)
						&& ($value2 =~ /^[\d]/))
					{
						if ($value1 =~ /^0x/i)
						{
							$tmp_value1 = hex("$value1");
						}elsif ($value1 =~ /^0/)
						{
							$tmp_value1 = oct("$value1");
						}
						else
						{
							$tmp_value1 = $value1;
						}

						if ($value2 =~ /^0x/i)
						{
							$tmp_value2 = hex("$value2");
						}elsif ($value2 =~ /^0/)
						{
							$tmp_value2 = oct("$value2");
						}
						else
						{
							$tmp_value2 = $value2;
						}
						$def_table{$name} = $tmp_value1 + $tmp_value2;
					}
	         	}	# elsif ($name && $value1 && $value2)
			}
		}
		close(FHD);
	}
	$idx++;
}

sub print_process_status {
    my $i=shift;
    my $j = $i % 4;
    SWITCH : {
	$j == 0 && do { print STDERR " (|)\r";  last SWITCH; };
	$j == 1 && do { print STDERR " (/)\r";  last SWITCH; };
	$j == 2 && do { print STDERR " (-)\r";  last SWITCH; };
	$j == 3 && do { print STDERR " (\\)\r"; last SWITCH; };
    }
}
