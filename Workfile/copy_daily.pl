#!/usr/bin/perl
#
# copy_daily.pl
# 2007/12/21 revised by rasmus.lai@indigomobile.com.tw
# 2008/01/30 add mod for source insight file copy
# 2008/02/12 add benchmark code piece
#

use strict;
use Readonly;
use File::Glob ':glob';
use File::Copy;
use Cwd;
use Getopt::Std;
use Benchmark ':hireswallclock';
use Win32::Clipboard;

sub main;
sub copy_and_extract_rar();
sub exec_pre_project();
sub copy_and_rename_si_project();
sub update_image_magick_files();
sub show_help_message();
sub append_backslash($);
sub remove_backslash($);
sub change_fname($$$);
sub modify_makefile_lcd();
sub copy_dsw_to_clipboard();
sub pf($$);
sub open_build_log($);
sub build_agent_service();
sub make_source_list();
sub mount_network_drive();
#----------------------------------------------------------------------------#
# behavior setting
#----------------------------------------------------------------------------#
# 0: Munich, 1: Dusseldorf
my $project_opt = 0;	# change the index if default project changes

# important !!! change to 0 if you want it work
my $debug = 0;

#----------------------------------------------------------------------------
# process the command line arguments
#----------------------------------------------------------------------------
my %opts;

# suggest sort by alphalets order
	# '-d' is bool, '-t:' take argument
getopts("dfghi:l:mp:st:x", \%opts);


#----------------------------------------------------------------------------#
$debug = $opts{d} || 0;
print STDERR "debug: $debug\n";

my $make_list = $opts{f} || 0;
print STDERR "make_list: $make_list\n";

my $stop_flag = $opts{g} || 0;
print STDERR "stop_flag: $stop_flag\n";

print STDERR "help: ", $opts{h}, "\n" if $opts{h};

$project_opt = $opts{p} || 0;
print STDERR "project_opt: $project_opt\n" if defined $project_opt;

my $arg_today = $opts{t};
print STDERR "arg_today: $arg_today\n" if $arg_today;
warn "arg_today undefined\n" if undef eq $arg_today;

my $mount_opt = $opts{m} || 0;
print STDERR "cmd: mount network drive\n" if $mount_opt;

my $open_log = $opts{l} || 0;
print STDERR "open_log from $open_log\n";

print "Unprocessed by Getopt::Std:\n" if $ARGV[0];
foreach (@ARGV) {
	print "$_\n";
}


#----------------------------------------------------------------------------#
# config here configuration settings
#----------------------------------------------------------------------------#
Readonly::Scalar my $base_dir => "d:\\project\\";		# local project dir
Readonly::Scalar my $rarexe_path => "c:\\progra~1\\winrar\\rar.exe";
Readonly::Scalar my $si_dir => "D:\\Project\\source_insight";

Readonly::Array my @project => (	# add more project/location if needs
		{	project_name => 'TK1',
			locate_dir => "Z:\\",
			#extra => '08A_',
			default_para => '"tk1 gprs"',
			mnt_cmd => q(net use Z: \\\\se2-server2\\tokyo_08a$\tk1 /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'PX1',
			locate_dir => "X:\\",
			#extra => '08A_',
			default_para => '"sharp gprs"',
			mnt_cmd => q(net use X: \\\\se2-server3\\phoenix_08a$\px1 /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'Sharp',
			locate_dir => "W:\\",
			extra => '08A_',
			default_para => '"sharp gprs"',
			mnt_cmd => q(net use W: \\\\SE2-Server\\Sharp_08A$ /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'MB1',
			locate_dir => "X:\\",
			#extra => '08A_',
			default_para => '"MB1 gsm"',
			mnt_cmd => q(net use X: \\\\se2-server1\\MB1_08A$ /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'MB1_inter1',
			locate_dir => "X:\\",
			#extra => '08A_',
			default_para => '"MB1 gsm"',
			mnt_cmd => q(net use X: \\\\se2-server1\\MB1_INTER1_08A$ /user:rasmus.lai@indigomobile)
			},
	);

Readonly::Scalar my $project_name => $project[$project_opt]{project_name};
Readonly::Scalar my $drive_name => $project[$project_opt]{locate_dir};
#printf "%s @ %s\n", $project_name, $drive_name;

#----------------------------------------------------------------------------#
# only help message would be execute outside the main procedure
#----------------------------------------------------------------------------#
show_help_message() if ($opts{h});
#----------------------------------------------------------------------------#
# only help message would be execute outside the main procedure
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------
# get the current date if no specified
#----------------------------------------------------------------------------
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
my $today = sprintf "%04d%02d%02d", ($year+1900), ($mon+1), $mday;	# like 20071225
my $today_4;

if ($arg_today)  {
	if ($arg_today =~ m/\d{8}/)  {
		$today = $arg_today;
	}
	elsif ($arg_today =~ m/\d{4}/)  {
		$today = ($year+1900) . $arg_today;
	}
}

$today =~ m/\d+(\d{4})$/;
$today_4 = $1;

print STDERR "today: $today, today_4: $today_4\n";
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# the basic project name
my $today_name;
if ($project[$project_opt]{extra}) {
	$today_name = $project_name . '_' . $project[$project_opt]{extra} . $today;
}
else {
	$today_name = $project_name . '_' . $today;
}
print STDERR "today_name: ", $today_name, "\n";

# the path copy from
my $from_file = $drive_name . "ZIP\\" . $today_name . "\\" . $today_name . '.rar';
print STDERR "from: ", $from_file, "\n";

# the path to copy to
Readonly::Scalar my $to_dir => $base_dir . $today_name;
print STDERR "to: ", $to_dir, "\n";

# the final project root directory
Readonly::Scalar my $project_base_dir => $to_dir . "\\" . $today_name;
print STDERR "project_base_dir: $project_base_dir\n";



#----------------------------------------------------------------------------
#
#
# main procedure here
#
#
#----------------------------------------------------------------------------
sub main
{
	exit(2) if $stop_flag ne 0;

    my $t0 = new Benchmark;
	system "timer /nologo";

	if ($opts{s})  {
		# only copy source insight project files
		copy_and_rename_si_project();
	}
	elsif ($opts{l})  {
		set_log_path($opts{l});
		# open_build_log();
	}
	elsif (defined $opts{i})  {
		build_agent_service();
	}
	elsif ($make_list)  {
		make_source_list();
	}
	elsif ($mount_opt)  {
		mount_network_drive();
	}
	else  {
# normal procedure here
		try_to_mount_drive();

		# if not exist, mkdir it
		if (not -d $to_dir)  {
			pf(__LINE__, "mkdir $to_dir");
			my $r = mkdir $to_dir;
			pf(__LINE__, "mkdir: $r");
		}

		# normal total operations
		if ( $opts{x} )  {
			pf(__LINE__, "===> skip copy and extract RAR");
		} else  {
			copy_and_extract_rar();
		}

#		if ( $project_opt == 0 )  {	# only for dussedolf_07B
#			modify_makefile_lcd();
#		}

		#exec_pre_project();
		copy_and_rename_si_project();
#		update_image_magick_files();
		copy_dsw_to_clipboard();
	}

	print STDERR "\n";
	print "\n";

	system "timer /s /nologo";
    my $t1 = new Benchmark;
    my $td = timediff($t1, $t0);
	print STDERR "\nThis action took: ", timestr($td),"\n";
}

main;
#----------------------------------------------------------------------------
# end of main procedure
#----------------------------------------------------------------------------


#----------------------------------------------------------------------------
# check the source rar, if not, mount network drive and try again
#----------------------------------------------------------------------------
sub try_to_mount_drive()
{
	pf(__LINE__, ('=' x 10 . ">>> try_to_mount_drive()"));

	my $netdrive = $project[$project_opt]{locate_dir};

	# check the from file
	if (not -e $from_file)  {
		# try to mount the network
		pf(__LINE__, ("$from_file not found"));

		if (not -d $netdrive)  {
			#print STDERR "==> try to mount project net drive: $netdrive\n";
			pf(__LINE__, "==> try to mount project net drive: " . $project[$project_opt]{mnt_cmd});

			# if already mount, unmount it first
			if ( -e $project[$project_opt]{locate_dir} )  {
				print STDERR "network drive already used, umount it\n";
				my $cmd = "cmd /c " . "net use " . remove_backslash($netdrive) . " /delete";
				system $cmd;
				sleep 1;
			}
			print STDERR $project[$project_opt]{mnt_cmd} if $debug;
			system "cmd /c " . $project[$project_opt]{mnt_cmd};	# $_->{mnt_cmd};
		}

		if (not -e $from_file)  {	# if failed again, abort
			$from_file =~ s/\.rar$/\.zip/i;
			pf(__LINE__, ("now try this: " . $from_file));
			if (not -e $from_file)  {
				print STDERR "[$from_file] not found!!!\n";
				if (not ($opts{l} or $opts{s}) )  {
					die;
				}
			}
		}
	}
}
#----------------------------------------------------------------------------


#----------------------------------------------------------------------------
# copy and extract rar
#----------------------------------------------------------------------------
sub copy_and_extract_rar()
{
	#
	# copy the file
	#
	my $cmd_str;
	my $localrar_file = $to_dir . "\\" . $today_name;

	if ( $from_file =~ m/(\.\w+)$/ )  {
		$localrar_file = $localrar_file . $1;
	}

	pf(__LINE__, ("from_file: " . $from_file));
	if (-f $from_file && -d $to_dir)  {
		$cmd_str = "copy $from_file $to_dir";
		print STDERR "==> $cmd_str\n";
		if ($debug != 1)  {
			if (-f $localrar_file)	 {	# the file exists
				pf(__LINE__, "localrar_file exists, skip");
			}
			else  {
				system "cmd /c " . $cmd_str;
			}
		}
	}
	else  {
		pf(__LINE__, "not found, did not copy");
	}

	#
	# unrar the local file
	#
	die $localrar_file, " not found\n" if (not -f $localrar_file);
	die $rarexe_path, "not found\n" if (not -f $rarexe_path);

	#
	# perform the unrar
	#
	my $unzip_dir = $today_name . "\\";
	print STDERR "unzip_dir: ", $unzip_dir, "\n";

	if ( $localrar_file =~ m/\.rar/i )  {
		$cmd_str = sprintf "%s x %s %s", $rarexe_path, $localrar_file, $unzip_dir;
	}
	elsif ( $localrar_file =~ m/\.zip/i )  {
		$cmd_str = "unzip " . $localrar_file;
	}
	print STDERR "==> ", $cmd_str, "\n";

	print STDERR "==> chdir $to_dir\n";
	chdir $to_dir;
	print STDERR "Cwd: ", cwd, "\n";

	# call winrar to extract archive file to specific directory
	system $cmd_str if ($debug ne 1);
	# check the exit code if successfully
	if (($? >> 8) == 0)  {
		unlink $localrar_file;
	}
	else  {
		pf(__LINE__, "something error, local rar file did not been deleted");
	}
}


#----------------------------------------------------------------------------
# execute the modis gen
#----------------------------------------------------------------------------
sub exec_pre_project()
{
	pf(__LINE__, ('=' x 10 . ">>> exec_pre_project()"));
	#
	# copy pre_project.bat to $unzip_dir
	#
	Readonly::Scalar my $pre_project => "pre_project.bat";
	my $cmd_str;
	my $def_para;

	#
	# call modm.pl to modify the M.bat
	#
	if ( -e ($base_dir . 'modm.pl') )  {
		$def_para = $project[$project_opt]{default_para} if $project[$project_opt]{default_para};
		$cmd_str = 'perl ' . $base_dir . 'modm.pl ' . $project_base_dir . '\M.bat' . ' ' . $def_para;
		print STDERR "==> $cmd_str\n";
		system $cmd_str if ($debug ne 1);
	}

	#
	# copy the pre_project.bat
	#
	$cmd_str = "copy " . $base_dir . $pre_project . " " . $project_base_dir;
	print STDERR "==> ", $cmd_str, "\n";
	copy(($base_dir . $pre_project), $project_base_dir) if ($debug ne 1);;

	#
	# execute pre_project.bat
	#
	print STDERR "==> chdir $project_base_dir\n";
	chdir $project_base_dir;
	print STDERR "Cwd: ", cwd, "\n";

	$cmd_str = "cmd /c " . $pre_project;
	print STDERR "==> $cmd_str\n";
	system $cmd_str if ($debug ne 1);
}

#----------------------------------------------------------------------------
# copy and rename source insight project
#----------------------------------------------------------------------------
sub copy_and_rename_si_project()
{
	pf(__LINE__, ('=' x 10 . ">>> copy_and_rename_si_project()"));
	my @list = ();
	my $cmd_str;
	my $proj_name = @project[$project_opt]->{project_name};
	my $prefix = 'Dusseldorf';	# default, may change
	my $dest_dir = $project_base_dir;
	my $curr_dir;

	$curr_dir = cwd;
	print STDERR "Cwd: ", cwd, "\n";
	print STDERR "==> chdir $si_dir\n";
	chdir $si_dir;
	print STDERR "Cwd: ", cwd, "\n";
	print STDERR "proj_name => $proj_name\n";

	if ( not -d $dest_dir )  {
		# if the dest dir not exists
		$dest_dir = $curr_dir;
	}
	print STDERR "destination dir: $dest_dir\n";

	@list = glob('*_????.*');
	for (@list)  {
		my $oldf = $_;
		s/([A-Za-z0-9]+)_(\d){4}/${proj_name}_${today_4}/;
#		s/\d{4}/$today_4/;
#		s/$prefix/$proj_name/;
		my $newf = $_;

		print STDERR ">>> $oldf\n<<< $newf\n";
		$cmd_str = sprintf "cmd /c copy %s %s\\%s", $oldf, $dest_dir, $newf;
		#print "==> cmd: $cmd_str\n";
		if ((-f $oldf) && ($debug ne 1))  {
			system "$cmd_str > nul";
		}
	}
}


#----------------------------------------------------------------------------
# update image magick dll/exe to newer version
#----------------------------------------------------------------------------
sub update_image_magick_files()
{
	pf(__LINE__, ('=' x 10 . ">>> update_image_magick_files()"));
	my $copy_from = "c:\\progra~1\\ImageMagick";
	my $copy_to = $project_base_dir . "\\plutommi\\Customer\\ResGenerator\\";
	my $cmd;

	$cmd = sprintf "cmd /c copy /y %s\\*.exe %s", $copy_from, $copy_to;
	print STDERR "==> $cmd\n";
	system $cmd if (not $debug);

	$cmd = sprintf "cmd /c copy /y %s\\*.dll %s", $copy_from, $copy_to;
	print STDERR "==> $cmd\n";
	system $cmd if (not $debug);
}


sub show_help_message()
{
	print<<EOL;
-d	debug on
-f	make source file list and exit
-g	print all settings and then exit
-h	help message
-i	0: turn off build service, 1: turn on
-l	show build log and exit
-m	mount the network drive for specified project, if not, default is 0
-s	copy source insight files only and exit
-t	specify the date to copy
-x	skip copy and extract rar
-p	specify project to copy, default is 0, could apply to:
EOL

	print "\t";
	my $ii = 0;
	foreach my $pp (@project)  {
		#printf "%d:%s\t", $ii, $project[$ii]->{project_name};
		printf "%d:%s\t", $ii, $pp->{project_name};
		++ $ii;
	}

	exit(1);
}

#
# append backslash at the end of string
#
sub append_backslash($)
{
	my $path = shift;
	if ( $path =~ m/\\$/ )  {
		# do nothing maybe for debug
	} else  {
		$path .= "\\";
	}
	print STDERR $path,"\n" if $debug;
	return $path;
}

#
# remove backslash at the end of string
#
sub remove_backslash($)
{
	my $path = shift;

	$path =~ s/\\$//;
	print STDERR $path,"\n" if $debug;
	return $path;
}

#
# original file name
# temp working file name
# backup file name
#
sub change_fname($$$)
{
	my ($org, $tmp, $bak) = @_;
	pf(__LINE__, "rename $org, $bak") if $debug;
	rename $org, $bak;
	pf(__LINE__, "rename $tmp, $org") if $debug;
	rename $tmp, $org;
}

# modify dusseldorf make file into 176X220 size for simulator
sub modify_makefile_lcd()
{
	pf(__LINE__, ('=' x 10 . ">> modify_makefile_lcd()"));

	my $mk_name = 'Dusseldorf_GPRS.mak';
	# the path to makefile
	my $mfile = append_backslash($project_base_dir) . "make\\$mk_name";
	# working output file
	my $ofile = $mfile . '.tmp';
	# backup file name
	my $bfile = $mfile . '.bak';

	printf STDERR "mfile = %s\nofile = %s\nbfile = %s\n", $mfile, $ofile, $bfile if $debug;

	open my $ifh, "< $mfile" or die;
	open my $ofh, "> $ofile" or die;

	while (<$ifh>)  {
		if (m/^MAIN_LCD_SIZE\s*=\s*(\d+X\d+)/)  {
			pf(__LINE__, "matched! ==> $1") if $debug;
			if ($1 ne "176X220")  {
				print $ofh "#", $_;	# comment out this line
				print $ofh "MAIN_LCD_SIZE = 176X220\t# modify to bigger LCD size\n";
			}
		}
		else  {
			print $ofh $_;
		}
	}

	close $ifh;
	close $ofh;

	change_fname($mfile, $ofile, $bfile);
}


sub copy_dsw_to_clipboard()
{
	my $dsw = append_backslash($project_base_dir) . "MoDIS\\MoDIS.dsw";

	pf(__LINE__, "dsw = $dsw") if $debug;
	pf(__LINE__, "dsw not found!") if (not -e $dsw);
	Win32::Clipboard::Set($dsw);
}


sub pf($$)
{
	my ($ln, $msg) = @_;
	printf STDERR "line %d: %s\n", $ln, $msg;
}

sub grep_error_from_file($)
{
	my $ifile = shift;
	my $fh;
	my $err = 0;
	my $line = 0;

	open $fh, $ifile or die;
	while ( <$fh> )  {
		++ $line;
		if ( m/Error: \w\d+\w/ )  {
			++ $err;
			printf("%s(%d): %s", $ifile, $line, $_);
		}
	}
	close $fh;
	return $err;
}

sub open_build_log($)
{
	pf(__LINE__, "open_build_log(): lookup errors from dailybuild server");

	my $loglist = '~cdtmplog.txt';
	my $logp = shift;
	my $cmd;
	my $err_cnt = 0;

	print "build log path: ", $logp,"\n" if $debug;
	$cmd = sprintf("cmd /c dir /s /b $logp\\*.log > $loglist");
	system $cmd;
	open my $fh, $loglist or die;
	while (<$fh>)  {
		s/\r\n//;
		$err_cnt += grep_error_from_file($_);
	}
	close $fh;
	print "total error found: ", $err_cnt, "\n";
}

sub set_log_path($)
{
	my $opt = shift;
	my $logpath;

	if ($opt eq 1)  {  # remote
		print STDERR "grep remote logs\n";
		$logpath = $drive_name . "SRC\\" . $today_name . "\\build" ;
	}
	elsif ($opt eq 2)  {	# local
		print STDERR "grep local logs\n";
		$logpath = ".\\build";
	}
	open_build_log($logpath);
}

sub build_agent_service()
{
	pf(__LINE__, "build_agent_service()");

	my $net_cmd;
	if ($opts{i} eq "0")  {	# turn off
		$net_cmd = q(net stop "IncrediBuild Agent");
	}
	elsif ($opts{i} eq "1")  {	# turn on
		$net_cmd = q(net start "IncrediBuild Agent");
	}

	if (length($net_cmd))  {
		print STDERR $net_cmd, "\n";
		system $net_cmd if (not $debug);
	}
}

sub make_source_list()
{
	pf(__LINE__, "make_source_list()");

	my $tmp_file = 'list.txt';

#	print STDERR "==> chdir $project_base_dir\n";
#	chdir $project_base_dir;
#	print STDERR "Cwd: ", cwd, "\n";

	my $cmd = "cmd /c dir /s /b *.c *.h > $tmp_file";
	#my $cmd = "cmd /c dir /s /b *.c *.h";
	print STDERR $cmd;
	system $cmd;

	die "not found!\n" if not -e $tmp_file;
}

sub mount_network_drive()
{
	pf(__LINE__, "mount_network_drive()");
	my $cmd;
	my $netdrive = $project[$project_opt]{locate_dir};

	if ( -e $project[$project_opt]{locate_dir} )  {
		print "network drive already used, umount it\n";
		$cmd = "cmd /c " . "net use " . remove_backslash($netdrive) . " /delete";
		system $cmd;
		sleep 1;
	}

	$cmd = "cmd /c " . $project[$project_opt]{mnt_cmd};

	print STDERR "CMD: $cmd\n";
	system $cmd;
}


=pod

=head1 NAME

copy_daily.pl

=head1 DESCRIPTION

Perform the following actions:

=item C<1.>
copy zipped dailybuild from server

=item C<2.>
to local specified project directory

=item C<3.>
unzip it to preset directory

=head1 REQUIREMENT

You need mount dailybuild folder before running this script.

	> net use Y: \\DailyBuild\Dusseldorf$
	> net use Z: \\DailyBuild\Munich$

=head1 NOTE

2007/12/18 first version for this script

=cut

=pod
		{	project_name => 'VE4',
			locate_dir => "Y:\\VE4\\",
			#extra => '08A_',
			default_para => '"VE4 gprs"',
			mnt_cmd => q(net use Y: \\\\Dailybuild\\Venice_08A$ /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'Dusseldorf',
			locate_dir => "W:\\",
			extra => '07B_',
			default_para => '"Dusseldorf gprs"',
			mnt_cmd => q(net use W: \\\\SE2-Server\\Dusseldorf_07B$ /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'Munich',
			locate_dir => "Y:\\",
			mnt_cmd => q(net use Y: \\\\DailyBuild\\Munich$ /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'Seoul',
			locate_dir => "Z:\\",
			extra => '07B_',
			mnt_cmd => q(net use Z: \\\\dailybuild\\seoul_07b$ /user:rasmus.lai@indigomobile)
			},
		{	project_name => 'DH1',
			locate_dir => "V:\\",
			extra => '07B_',
			mnt_cmd => q(net use V: \\\\SE2-Server\\DH1_07b$ /user:rasmus.lai@indigomobile)
			},
=cut
