#!/usr/bin/perl -w

#@ �ѩ� DOS �� dir /b �O�H \r\n �@����
#@ �u�� chomp �u�|�� \n �h���A�Ӥ��|�� \r �h��
#@ �ҥH�n�A�h�@�@�Ӱʧ@�h�� \r


while ( <> )
{
    chomp;
    s/\r//;
    print "$_\n";
}

#
# 2006/12/27 by ericosur
# now I use the stupid way:
# s/\n//;
# s/\r//;
#
