package main;

import com.example.testmoma1.R;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager.NameNotFoundException;
import android.os.Bundle;
import android.provider.Settings;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {

	private TextView tvState;
	final static public String TAG = "TestMoma";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);

		Log.i("MainActivity", "onCreate"+this.hashCode());
		this.setContentView(R.layout.activity_main);

		tvState = (TextView) this.findViewById(R.id.tvState);
		//get version
		PackageInfo packageInfo = null;
		try {
			packageInfo = this.getPackageManager().getPackageInfo(this.getPackageName(), 0);
		} catch (NameNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		String version = "Version: "+packageInfo.versionName+" ("+packageInfo.versionCode+")";

		tvState.setText(version);
	}

	@Override
	protected void onResume() {
		super.onResume();
		Log.i("MainActivity", "onResume"+this.hashCode());
	}
	@Override
	protected void onPause() {
		super.onPause();
		Log.i("MainActivity", "onPause"+this.hashCode());
	}
	@Override
	protected void onDestroy() {
		super.onDestroy();
		Log.i("MainActivity", "onDestroy "+this.hashCode());
	}

	public void onButtonClick(View v){

		switch (v.getId()) {
			case R.id.btnOpenSettingsMenu:
				startActivity(new Intent(Settings.ACTION_SETTINGS));
				break;
			case R.id.btnSoundSettings:
				startActivity(new Intent(Settings.ACTION_SOUND_SETTINGS));
				break;
			case R.id.btnDisplaySettings:
				startActivity(new Intent(Settings.ACTION_DISPLAY_SETTINGS));
				break;
			case R.id.btnAdbEnable:
				System.setProperty("persist.sys.usb.config", "mtp,adb");
				Toast.makeText(this, "Now property (persist.sys.usb.config) = "+System.getProperty("persist.sys.usb.config"), Toast.LENGTH_SHORT).show();
				break;
			case R.id.btnAdbDisable:
				System.setProperty("persist.sys.usb.config", "mtp");
				Toast.makeText(this, "Now property (persist.sys.usb.config) = "+System.getProperty("persist.sys.usb.config"), Toast.LENGTH_SHORT).show();
				break;
			default:
			    break;
		}
	}

	@Override
	public void onBackPressed() {
		Log.i("MainActivity", "onBackPressed "+this.hashCode());
		Toast.makeText(this, "Test Launcher onBackPressed."+this.hashCode(), Toast.LENGTH_SHORT).show();
	}

    public void launchWifi(View view) {
    	Log.i(TAG, "launchWifi");
    	Intent intent = new Intent();
    	intent.setClassName("com.android.settings", "com.android.settings.wifi.WifiSetupActivity");
    	intent.putExtra("firstRun", true);
        startActivity(intent);
    }
    
    public void launchDate(View view) {
    	Log.i(TAG, "launchDate");
    	Intent intent = new Intent();
    	intent.setClassName("com.android.settings", "com.android.settings.DateTimeSettingsSetupWizard");
        startActivity(intent);
    }
    
    public void launchEthernet(View view) {
    	Log.i(TAG, "launchEthernet");
    	Intent intent = new Intent();
    	intent.setClassName("com.android.settings", "com.android.settings.ethernet.EthernetSettings");
        startActivity(intent);
    }


}
