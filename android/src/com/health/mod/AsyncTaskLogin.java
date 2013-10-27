package com.health.mod;

import java.util.ArrayList;
import java.util.List;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONObject;
import android.os.AsyncTask;
import android.util.Log;

public class AsyncTaskLogin extends AsyncTask <String, Integer, Boolean >{

	
	  private HttpClient cliente;
	  private HttpPost metodoPost;
	  private HttpResponse respuesta;
	  private List<NameValuePair> valores;
	

	  protected Boolean doInBackground(String... params)
	  {
		  		  
		  		String jsonR = "";
		  
		  		try{
		  		
				  		valores = new ArrayList<NameValuePair>(1); 
			        
				  		valores.add(new BasicNameValuePair("email",params[0]));
				  		valores.add(new BasicNameValuePair("password",params[1]));
			    		    	
				  		cliente = new DefaultHttpClient();
				  		metodoPost = new HttpPost("");
				  		metodoPost.setHeader("Accept","application/json");
			        
				  		metodoPost.setEntity(new UrlEncodedFormEntity(valores));
			     
				  		respuesta = cliente.execute(metodoPost);
			        
				  		HttpEntity httpEnti = respuesta.getEntity();
			        
				  		jsonR =EntityUtils.toString(httpEnti);
			        
				  		Log.d("JSON REGRESO LOGIN: ", jsonR);
			                    
				  		JSONArray jsonArray = new JSONArray(jsonR);
				  		 
				  		JSONObject jsonObject = jsonArray.getJSONObject(0);
	                    
                        int res = jsonObject.getInt("result");
                        
                        if(res == 1)
                        	return true;
                        else
                        	return false;
                        				  		
		  		}catch(Exception e){
			    	
		  				Log.d("ENTRE EXCEPTION GET PAISES: ", "EXCEPTION");			    				    	
		  				return false;
		  				
			    }  		 
		  		
		  
	  }
	  
	  protected void onPostExecute(Integer result)
	  {
			
	  }
	  
	  
	
}
