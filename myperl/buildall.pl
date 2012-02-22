#!/usr/bin/perl

# Build All projects in/below \\Projects

my $bpr_list = "bprlist";
my $prj_dir = "c:\\projects";

chdir $prj_dir or die "chdir to $prj_dir failed\n";

system "dir /s/b *.bpr >$bpr_list";

my $cnt = 0;
my $list_name = $bpr_list;


  print "try to process $list_name\n";

  open(FILE, $list_name) or die "cannot open $list_name: $!\n";
  LOOP: while ( <FILE> ) {
    next LOOP if /^\s/;

    if ( /^(.*)\\(.*)$/ ) {
        my $prj_path = $1;
        my $prj_name = $2;
        unless (chdir $prj_path) {
            warn "cannot chdir to $prj_path\n";
            next LOOP;
        }
        print "Enter [$prj_path]\n";
        if (-e $prj_name) {
            system "make -f$prj_name";
        }
        else {
            print "$prj_name not exist\n"
        }
        print "press any key to continue...";
        <STDIN>;
        $cnt++;
    }
  } # while ...
  close(FILE);

chdir $prj_dir;
unlink $bpr_list;

print "total processed: $cnt files\n";