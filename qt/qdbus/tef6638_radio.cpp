#include "tef6638_radio.h"

#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

/* turn on radio and set to frequency, OnEnabled() */
void enable( u16 frequency )
{
    (void)frequency;
    printf("freq: %u", frequency);
}

/* turn off radio, OnDisabled() */
void disable( void )
{
    printf("disable()");
}

/* set frequency, OnFrequencyChanged() */
void setFrequency( u16 frequency )
{
    (void)frequency;
    printf("setFrequency()");
}

/* set mode to am or fm */
void setMode( u16 BandType )
{
    (void)BandType;
    printf("setMode(%u)", BandType);
}

/* seek up */
u16 seekUp( void )
{
    return 10070;
}

/* seek down */
u16 seekDown( void )
{
    return 8950;
}

/* Cancel Seek */
void cancelSeek( void )
{

}

/* set radio Area */
void radioArea( u16 AreaCode )
{
    (void)AreaCode;
}

/* radio Infomation */
void radioInfo( struct Radio_InfoDef *ri )
{
    ri->enable = 0;
    ri->current_freq = 10850;
    ri->radio_band = 1;
    ri->BandInfo.FM_MaxFreq = 103;
    ri->BandInfo.FM_MinFreq = 87;
    ri->BandInfo.AM_MaxFreq = 1197;
    ri->BandInfo.AM_MinFreq = 789;
    ri->BandInfo.FM_SeekStep = 5;
    ri->BandInfo.AM_SeekStep = 10;
}

/* signal power */
u8 signalPower( void )
{
    return 100;
}

/* set volume gain, OnRadioVolumeGain() */
void setVolumeGain( u16 vol )
{
    (void)vol;
    printf("setVolumeGain()\n");
}

#ifdef __cplusplus
}
#endif
