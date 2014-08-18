 #!/usr/bin/perl

# Akadia AG, Arvenweg 4, CH-3604 Thun                 send_attachment.pl
# ----------------------------------------------------------------------
#
# File:       send_attachment.pl
#
# Autor:      Martin Zahn / 05.01.2003
#
# Purpose:    Email attachments in Perl
#
# Location:   $ORACLE_HOME\Database
#
# Certified:  Perl 5.6.1, MIME-Lite-2.117 on Cygwin / Windows 2000
# ----------------------------------------------------------------------

# reference from http://www.akadia.com/services/email_attachments_using_perl.html

use strict;
use warnings

use MIME::Lite;
use Net::SMTP;

### Adjust sender, recipient and your SMTP mailhost
my $from_address = 'rasmus1@indigoqm.tw';
my $to_address = 'rasmus1@indigoqm.tw';
my $mail_host = 'mail.indigoqm.tw';

### Adjust subject and body message
my $subject = 'A message with 2 parts ...';
my $message_body = "Here's the attachment file(s) you wanted";

### Adjust the filenames
my $my_file_gif = 'img001.jpg';
my $your_file_gif = 'img002.jpg';
my $my_file_zip = 'foo.zip';
my $your_file_zip = 'bar.zip';

### Create the multipart container
$msg = MIME::Lite->new (
  From => $from_address,
  To => $to_address,
  Subject => $subject,
  Type =>'multipart/mixed'
) or die "Error creating multipart container: $!\n";

### Add the text message part
$msg->attach (
  Type => 'TEXT',
  Data => $message_body
) or die "Error adding the text message part: $!\n";

### Add the GIF file
$msg->attach (
   Type => 'image/gif',
   Path => $my_file_gif,
   Filename => $your_file_gif,
   Disposition => 'attachment'
) or die "Error adding $file_gif: $!\n";

### Add the ZIP file
$msg->attach (
   Type => 'application/zip',
   Path => $my_file_zip,
   Filename => $your_file_zip,
   Disposition => 'attachment'
) or die "Error adding $file_zip: $!\n";

### Send the Message
MIME::Lite->send('smtp', $mail_host, Timeout=>60);
$msg->send;
