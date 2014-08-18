#!/usr/bin/perl
use Net::SMTP::TLS;
my $mail = 'ericosur@gmail.com';
my $subject = 'test subject';
my $msg = 'Hello there!';
    my $mailer = new Net::SMTP::TLS(
        'smtp.gmail.com',
        Hello   => 'smtp.gmail.com',
        #Port    =>      465, #redundant
        User    =>      'ericosur@gmail.com',
        Password=>      'adjm1234',
    );
    $mailer->mail('ericosur@gmail.com');
    $mailer->to($mail);
    $mailer->data;
    $mailer->datasend("From: ericosur\n");
    $mailer->datasend("To: $mail\n");
    $mailer->datasend("Subject: $subject\n\n");
    $mailer->datasend($msg);
    $mailer->dataend;
    $mailer->quit;

    print "send mail to $mail\n";
    undef $mailer;
