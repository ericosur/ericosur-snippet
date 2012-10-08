package com.pega.stayawake;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.widget.Toast;

public class MainActivity extends Activity {
	

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //setContentView(R.layout.activity_main);
        Intent intent = new Intent("android.intent.action.PEGA_STAY_AWAKE");
        sendBroadcast(intent);
        Toast.makeText(this, "The PEGA StayAwakeService start!", Toast.LENGTH_LONG).show();
        finish(); 
    }
    
    public void onResume(){
    	super.onResume();
    }
    
    public void onDestroy(){
    	super.onDestroy();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
}
