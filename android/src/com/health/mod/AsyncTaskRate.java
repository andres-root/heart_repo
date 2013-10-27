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
	
	private HttpClient client;
	private HttpPost methodPost;
	
	private HttpResponse response;
	private List<NameValuePair> values;
	
	@Override
	protected String doInBackground(String... arg0)
	{
				
				String jsonR = ""; 
	
				values = new ArrayList<NameValuePair>(1);    	    
				values.add(new BasicNameValuePair("", arg0[0]));
				values.add(new BasicNameValuePair("",  arg0[1]));
	   	   	
				try{    
				 
						   client = new DefaultHttpClient();
						   methodPost = new HttpPost("");
				           
						   methodPost.setHeader("Accept","application/json");
				 				           
						   methodPost.setEntity(new UrlEncodedFormEntity(values));
				        
						   response = client.execute(methodPost);
				           
				           HttpEntity httpEnti = response.getEntity();
				           
				           jsonR = EntityUtils.toString(httpEnti);
				           
				           Log.i("Response LOGIN   : ", jsonR);		      
				           
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

