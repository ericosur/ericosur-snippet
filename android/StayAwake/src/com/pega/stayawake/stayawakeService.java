package com.pega.stayawake;

import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.os.IBinder;
import android.os.PowerManager;
import android.util.Log;

public class stayawakeService extends Service{

	String TAG = "StayAwakeService" ;
	PowerManager pm; 
	PowerManager.WakeLock wakeLock;
	
	@Override
	public IBinder onBind(Intent arg0) {
		// TODO Auto-generated method stub
		return null;
	}
	
	public void onCreate() {
		
		pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
		wakeLock = pm.newWakeLock(PowerManager.SCREEN_DIM_WAKE_LOCK | PowerManager.ON_AFTER_RELEASE, "WakeLockActivity");
	
	}
	
	public int onStartCommand(Intent intent, int flags, int startId){
		wakeLock.acquire();  
		Log.i(TAG, "StayAwakeService: acquire wakeLock");
		return START_STICKY;
	}
	
	public void onDestroy() {
		wakeLock.release();
		Log.i(TAG, "StayAwakeService: release wakeLock");
	}

}
