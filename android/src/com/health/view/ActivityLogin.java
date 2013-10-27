package com.health.view;

import com.health.heart.Main;
import com.health.heart.R;
import com.health.mod.AsyncTaskLogin;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.EditText;

public class ActivityLogin extends Activity 
{
	
	private  EditText user;
	private  EditText pass;
	
	public void onCreate(Bundle savedInstanceState)
	{        
		      super.onCreate(savedInstanceState);
		      requestWindowFeature(Window.FEATURE_NO_TITLE); 
		      setContentView(R.layout.activity_login);
		        
		      user = (EditText) findViewById(R.id.editText1);
		      pass = (EditText) findViewById(R.id.editText2);			        		        
		        
    }
		
	public void login(View v) {
	  
			
			String rUser = user.getText().toString();
			String rPass = pass.getText().toString();
		
			//AsyncTaskLogin login = new AsyncTaskLogin();

			Intent intent = new Intent(ActivityLogin.this, Main.class);
       		startActivity(intent);       	 	
       		finish();
		
	}
	
	
	
}
