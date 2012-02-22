use File::Find;
use File::Basename;
my $src_dir = '/media/Extension/Miro';
find(\&travse, $src_dir);
sub travse {
    my $filename = $File::Find::dir . '/' . $_;
    my $new_filename;
    my $cmd;
    if (-d $filename) {
        $_ = $filename;
        s/Miro/podcast/;
        print "directory:$_ ";
        if (not -e $_) {
            die "cant create directory ${_}:$!" unless mkdir $_, 4;
        }
    }
    else {
        $_ = $filename;
        s/Miro/podcast/;
        $new_filename = $_ . '.avi';
        if (not -e $new_filename) {
            print "\241X\241X\241X\241X\241X\241X\241X\241X\241X\241X\241X\241V\n";
            print "$new_filename\n";
            $cmd = "mencoder $filename -oac lavc -ovc lavc -ffourcc DIVX -lavcopts vcodec=mpeg4:vbitrate=150:acodec=mp3:abitrate=64 -o $new_filename -sws 2 ";
            print "$cmd\n";
            print "\241X\241X\241X\241X\241X\241X\241X\241X\241X\241X\241X\241V\n";
            system "$cmd";
        }
        else {
            print "$new_filename PASS!\n";
        }
    }
}
