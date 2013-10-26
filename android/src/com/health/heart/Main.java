package com.health.heart;

import android.os.Bundle;
import android.os.Handler;
import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothSocket;
import android.view.Menu;
import android.widget.Button;

public class Main extends Activity {

	private Button buttonOne;
	private Button buttonTwo;
	private Button buttonTree;
	private Button buttonFourt;
	
	private  static final String TAG_DEBUG = "Bluetooth: "; 
	
	//Handler
	private  Handler h;
	final int RECIEVE_MESSAGE = 1;
	
	private BluetoothAdapter btAdapter = null;
	private BluetoothSocket btSocket = null;
	private StringBuilder sb = new StringBuilder();
	
	@Override
	protected void onCreate(Bundle savedInstanceState) 
	{
		
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
		
	}

	
}
