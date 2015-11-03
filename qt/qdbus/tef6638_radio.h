#ifndef __TEF6638_RADIO_H
#define __TEF6638_RADIO_H

#ifdef __cplusplus
extern "C" {
#endif

typedef unsigned char		u8;
typedef unsigned short		u16;
typedef unsigned int		u32;

/* radio band define */
#define MAX_BAND_NUM 6
#define FM1_BAND 0
#define FM2_BAND 1
#define FM3_BAND 2
#define MW_BAND 3
#define LW_BAND 4
#define SW_BAND 5

enum Radio_AreaCode {
    Radio_CHN = 0,
    Radio_EUR,
    Radio_USA,
    Radio_JPN
};

struct Radio_BandInfoDef {
	//area radio parameter
	u32 FM_MaxFreq;			// FM max freq
	u32 FM_MinFreq;			// FM min freq
	u32 AM_MaxFreq;			// AM max freq
	u32 AM_MinFreq;			// AM min freq
	u32 FM_SeekStep;		// FM step
	u32 AM_SeekStep;		// AM step
};

struct Radio_InfoDef {
	u16 enable;
	u16 current_freq;
	u16 radio_band;
	struct Radio_BandInfoDef BandInfo;
};

/* turn on radio and set to frequency, OnEnabled() */
void enable( u16 frequency );

/* turn off radio, OnDisabled() */
void disable( void );

/* set frequency, OnFrequencyChanged() */
void setFrequency( u16 frequency );

/* set mode to f1/f2/f3/mw/lw/sw */
void setMode( u16 BandType );

/* seek up */
u16 seekUp( void );

/* seek down */
u16 seekDown( void );

/* Cancel Seek */
void cancelSeek( void );

/* set radio Area */
void radioArea( u16 AreaCode );

/* radio Infomation */
void radioInfo( struct Radio_InfoDef *Radio_Info );

/* signal power */
u8 signalPower( void );

/* set volume gain, OnRadioVolumeGain() */
void setVolumeGain( u16 vol );

#ifdef __cplusplus
}	// extern "C" {
#endif

#endif	// __TEF6638_RADIO_H