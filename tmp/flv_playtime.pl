package playtime;

use Exporter 'import';
@EXPORT_OK=qw(playtime);
use POSIX qw(SEEK_CUR SEEK_SET SEEK_END);

sub new{
    my $class=shift;
    my $type=ref $class || $class;
    my $this={};
    bless $this, $type;
    return $this;
}

sub BigEndian2Int{
    my $byte_word=shift;
    my $signed=0;
    my $int_value=0;
    my $byte_wordlen=length($byte_word);
    my @ttt=split(//,$byte_word,$byte_wordlen);

    for(my $i=0;$i<$byte_wordlen;$i++){
         my $tmp=256 ** ($byte_wordlen-1-$i);
         $int_value +=ord($ttt[$i]) * $tmp;
    }
    if($signed == '1'){
    my $sign_mask_bit = 0x80 << (8 * ($byte_wordlen - 1));
    if ( $int_value & $sign_mask_bit) {
         $int_value = 0 - ($int_value & ($sign_mask_bit - 1));
     }
    }
    return $int_value;
}

sub playtime(){
    my $this=shift;
    my $filename=shift;
    my $flv_data_length=(lstat $filename)[7];
    my $flv_head;
    my $record;
    open(FD,"<:raw","$filename") || die "can't open $filename\n";
    read(FD,$flv_head,9) || die "read $filename error\n";
        seek(FD,5,SEEK_SET) || die "seek $filename failed\n";
    read(FD,$record,4) || die "read $filename failed(2)\n";
    my $frame_size_data_length=BigEndian2Int($record);
    my $flv_header_frame_length=9;
    if( $frame_size_data_length > $flv_header_frame_length){
        seek(FD,$abc,SEEK_CUR);
    }
    my $duration=0;
    while((tell(FD) + 1) < $flv_data_length){
        my $this_tag_header;
     read(FD,$this_tag_header,16);
        my $data_length = BigEndian2Int(eval {substr($this_tag_header,5,3)});
        my $timestamp = BigEndian2Int(eval {substr($this_tag_header,8,3)});
        my $next_offset = tell(FD) - 1 + $data_length;
    if($timestamp > $duration){
        $duration = $timestamp;
    }
    seek(FD,$next_offset,SEEK_SET);
    }
    close(FD);
    return $this->{'filename'}=$duration;
}

1;

__END__

=head1 NAME

playtime - grab *.flv playtime

=head1 SYNOPSIS

use playtime;

my $play=new playtime;

$play->playtime('yourdir/tmp.flv');

=head1 AUTHOR

   | create by irror (irror2008@163.com) |
              | 2007-12-17 |
     | v1.0 |

     from http://blog.chinaunix.net/u/187/showart_451193.html

=cut