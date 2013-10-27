package com.health.view;

import com.health.heart.R;

import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;

public class ActivityLogin extends Activity 
{

	private  EditText user;
	private  EditText pass;
	private  Button loginButton;
	 
	public void onCreate(Bundle savedInstanceState){
        
		        super.onCreate(savedInstanceState);
		        requestWindowFeature(Window.FEATURE_NO_TITLE); 
		        setContentView(R.layout.activity_login);
		        
		        user = (EditText) findViewById(R.id.editText1);
		        pass = (EditText) findViewById(R.id.editText2);
		        
		        loginButton = (Button) findViewById(R.id.button1);
        
    }
	
	
	
	
}
