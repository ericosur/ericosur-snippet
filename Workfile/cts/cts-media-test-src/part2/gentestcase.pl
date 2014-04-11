#!/usr/bin/perl

use strict;
use File::Basename;

my $filelist;

sub gen_header()
{
print<<EOHEADER;
/*
 * Copyright (C) 2012 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package android.mediastress.cts;

public class WmvShortPlayerTest extends MediaPlayerStressTest {

EOHEADER
}

sub gen_body()
{
    my $vpath = q(qtc-video/);
    my $cnt = 0;

print<<EOB;
    private final static String VIDEO_PATH_MIDDLE = "$vpath";
    private final String[] mMedias = {
EOB

    open my $fh, $filelist or die;
    while (<$fh>) {
        $cnt ++;
        s/^\S+\///;
        s/[\r\n]//g;
        my $fn = basename($_);
        printf("        \"%s\",\n", $fn);
    }
    close $fh;

print<<EOC;
    };

EOC

    for (my $ii=0; $ii<$cnt; $ii++) {
        printf("    public void testPlay%02d() throws Exception {\n", $ii);
        printf("        doTestVideoPlaybackShort(%d);\n", $ii);
        printf("    }\n\n");
    }

}

sub gen_footer()
{
print<<EOFOOTER;
    \@Override
    protected String getFullVideoClipName(int mediaNumber) {
        return VIDEO_TOP_DIR + VIDEO_PATH_MIDDLE + mMedias[mediaNumber];
    }

}

EOFOOTER
}

sub gen_testcase()
{
    if (-e $filelist) {
        gen_header();
        gen_body();
        gen_footer();
    } else {
        print "$filelist not found\n";
    }
}

sub main()
{
    $filelist = "filelist.txt";

    if ($ARGV[0]) {
        print $ARGV[0],"\n";
        $filelist = $ARGV[0];
    }

    gen_testcase();
}

main;
