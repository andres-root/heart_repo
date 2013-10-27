package com.health.view;

import com.health.heart.Main;
import com.health.heart.R;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.Window;

public class Splash extends Activity {

	private Handler handler;
	
	public void onCreate(Bundle savedInstanceState){
        
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE); 
        setContentView(R.layout.activity_splash);
        
        handler = new Handler();
        handler.postDelayed(getRunnableStartApp(), 5000);
        
    
    }
	
	 private Runnable getRunnableStartApp()
	 {
	         		 
	         Runnable runnable = new Runnable(){
	             
			         public void run()
			         {
			
				        		 Intent intent = new Intent(Splash.this, Main.class);
				        		 startActivity(intent);
				        		 finish();
			         }
	         
	         };
	         	         
	         return runnable;
	         
	  }
	
	
}	

