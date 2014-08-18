package com.pega.stayawake;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class stayawakeReceiver extends BroadcastReceiver{
	
	Context gContext;
	String TAG = "StayAwakeReceiver";
	stayawakeService mstayawakeService;

	
	@Override
	public void onReceive(Context context, Intent intent) {
		
		gContext = context;
		String action = intent.getAction();
		Log.i(TAG, "StayAwakeReceiver: onReceive(): action " + action);
		
		Intent mBootIntent = new Intent(context, stayawakeService.class);
		mBootIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
		mBootIntent.setAction("startForeground");
		context.startService(mBootIntent);
		
	}

}
