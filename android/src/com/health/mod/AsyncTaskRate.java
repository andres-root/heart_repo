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

import android.os.AsyncTask;
import android.util.Log;


public class AsyncTaskRate extends AsyncTask<String, Void, String> 
{

	private HttpClient cliente;
	private HttpPost metodoPost;
	private HttpResponse respuesta;
	private List<NameValuePair> valores;
	
	@Override
	protected String doInBackground(String... arg0)
	{
	   
	  
				String jsonR = ""; 
	
				valores = new ArrayList<NameValuePair>(1);    	    
				valores.add(new BasicNameValuePair("", arg0[0]));
				valores.add(new BasicNameValuePair("",  arg0[1]));
	   	   	
				try{    
				 
				           cliente = new DefaultHttpClient();
				           metodoPost = new HttpPost("");
				           
				           metodoPost.setHeader("Accept","application/json");
				 				           
				           //Log.d("ENCODE ANDROID", new UrlEncodedFormEntity(valores).);
				           
				           metodoPost.setEntity(new UrlEncodedFormEntity(valores));
				        
				           respuesta = cliente.execute(metodoPost);
				           
				           HttpEntity httpEnti = respuesta.getEntity();
				           
				           jsonR = EntityUtils.toString(httpEnti);
				           
				           Log.i("Respuesta LOGIN   : ", jsonR);		      
				           
				           return jsonR;
				           
				}catch(Exception error){
						Log.d("ERROR LOGIN: ", error.getMessage());
						return "";
				}
	
	}
	
	@Override
	protected void onPostExecute(String result)
	{
		
	}

}

