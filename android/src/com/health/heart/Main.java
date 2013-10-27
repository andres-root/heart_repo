package com.health.heart;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Method;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.UUID;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.widget.TextView;
import android.widget.Toast;

public class Main extends Activity{
	
	   /* 
	   		private Button buttonOne;
	   		private Button buttonTwo;
	   		private Button buttonTree;
	   		private Button buttonFourt;
	   */
	   
	   private List<String> bufferData;
	
	   private static final String TAG_DEBUG = "Bluetooth: "; 
	   
	   //Handler
	   private  Handler h;
	   final int RECIEVE_MESSAGE = 1;
	   
	   //Bluerooth
	   private BluetoothAdapter btAdapter = null;
	   private BluetoothSocket btSocket = null;
	   private StringBuilder sb = new StringBuilder();
	   private ConnectedThread mConnectedThread;
	   
	   //Miscellaneous
	   private static final UUID MY_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
	   private static String address = "00:06:66:4F:B8:12";
	   private TextView textMsg;
	   
	   @Override
	   protected void onCreate(Bundle savedInstanceState) 
	   {
		   		 
		   		 super.onCreate(savedInstanceState);
		   		 setContentView(R.layout.activity_main);
		   		 textMsg = (TextView) findViewById(R.id.textMsg); 
		   		 		   		 
		   		 initializeHandler();		   		 
		   		 btAdapter = BluetoothAdapter.getDefaultAdapter();
		   		 checkBTState();
		   		 		   		 
		   		 bufferData = new ArrayList<String>();
		   		 //AsyncTaskRate rate = new AsyncTaskRate();
		   		 //rate.execute("roluisker@gmail.com","6",getDateTime());
		   		 		   				   		
	   }
	   
	   private String getDateTime()
	   {
		   
		   Calendar c = Calendar.getInstance();
	   	   SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
	   	   return df.format(c.getTime());		   
		   
	   }
	   
	   private BluetoothSocket createBluetoothSocket(BluetoothDevice device) throws IOException 
	   {
		      
						  if(Build.VERSION.SDK_INT >= 10){
					          
							  try{
					              
								  final Method  m = device.getClass().getMethod("createInsecureRfcommSocketToServiceRecord", new Class[] { UUID.class });
					              return (BluetoothSocket) m.invoke(device, MY_UUID);
					              
					          }catch(Exception err){					              
					        	  Log.e(TAG_DEBUG, "Could not create Insecure RFComm Connection",err);					              
					          }
					          
					      }
					      
					      return  device.createRfcommSocketToServiceRecord(MY_UUID);
					      
	   }
	   
	   
	   @Override
	   public void onResume()
	   {
		   		
		   		super.onResume();		   			
		   		BluetoothDevice device = btAdapter.getRemoteDevice(address);
		   		
		   		try{
		   			
		   				btSocket = createBluetoothSocket(device);
		   			
		   		}catch(IOException err){
		   			   					   			
		   				errorExit(err.getMessage());		   			
		   		}
		   		
		   		btAdapter.cancelDiscovery();
		   		
		   		try{
		         
		   				btSocket.connect();
		   				Log.d(TAG_DEBUG, "....Connection ok...");
		         
		        }catch(IOException e){
		         
		       			try{
		           
		       					btSocket.close();
		           
		       			}catch(IOException e2){ 		       				
		       					errorExit("In onResume() and unable to close socket during connection failure" + e2.getMessage() + ".");		         
		       			}
		       	
		       }
		   		
		   		Log.d(TAG_DEBUG, "...Create Socket...");
		   	   
		   	    mConnectedThread = new ConnectedThread(btSocket);
		   	    mConnectedThread.start();	
		   
	   }
	   
	   
	   @Override
	   public void onPause()
	   {
		   
		   	  super.onPause();		   	  
		   	  Log.d(TAG_DEBUG, "PAUSE TIME!!");
		   	  
		   	  try{
		        
		   		  	btSocket.close();
		        
		   	  }catch(IOException err){		    	
		   		  errorExit("In onPause() and failed to close socket." + err.getMessage() + ".");		   		  
		   	  }
		   	     
	   }
	   
	   private void checkBTState()
	   {
	   
			    if(btAdapter==null){ 
			      
			    	errorExit("Bluetooth not support");
			      
			    }else{
			    	
				      if(btAdapter.isEnabled()) 
				      {
				    	  
				    	  Log.d(TAG_DEBUG, "...Bluetooth ON...");
				      
				      }else{
				        
				    	  Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
				    	  startActivityForResult(enableBtIntent, 1);
				        
				      }
			      
			    }
		    
		}
	   	   	 	   	   	   
	@SuppressLint("HandlerLeak")
	public void initializeHandler()
	{
		
			   h = new Handler(){
			    	
				   public void handleMessage(android.os.Message msg)
				   {
			    		
							   switch(msg.what)
							   {
					            
							   			case RECIEVE_MESSAGE:													
					            	
							   						byte[] readBuf = (byte[]) msg.obj;
							   						String strIncom = new String(readBuf, 0, msg.arg1);					
					            	
							   						sb.append(strIncom);	
					            	
							   						int endOfLineIndex = sb.indexOf("\r\n");
					            	
							   						if(endOfLineIndex > 0) 
							   						{ 											
					            		
							   							String sbprint = sb.substring(0, endOfLineIndex);				
							   							sb.delete(0, sb.length());										
							   							//textMsg.setText(sbprint);
							   							
							   							boolean isAdd = bufferData.add(sbprint);
							   							
							   							textMsg.setText( String.valueOf(isAdd) );
							   							textMsg.setText(" ESPERANDO...." );
							   							
							   							if(bufferData.size() >= 100)
							   							{
							   								
							   								textMsg.setText( bufferData.size() );
							   								bufferData.clear();
							   								
							   							}
							   							
							   							//sendData();
							   							//AsyncTaskRate rate = new AsyncTaskRate();
							   					   		//rate.execute("roluisker@gmail.com",sbprint,getDateTime());
					                	
							   						}
							   			
							   			break;
							   			
					    		}
					   
			        };
			        
				};
				
						   
	   }
	
		private void sendData()
		{
			
			
			HttpClient client;
			HttpPost methodPost;
			
			HttpResponse response;
			List<NameValuePair> values;
			
			String jsonR = ""; 
			
			values = new ArrayList<NameValuePair>(1);    	    
			values.add(new BasicNameValuePair("email", "roluisker@gmail.com"));
			values.add(new BasicNameValuePair("BPM",  "70"));
			values.add(new BasicNameValuePair("when", "2013-01-01 00:00:00"));
			values.add(new BasicNameValuePair("ac","add_measurement"));
			
			try{    
				 
				   client = new DefaultHttpClient();
				   methodPost = new HttpPost("http://heartrepo.appspot.com/");
		           
				   methodPost.setHeader("Accept","application/json");
		 				           
				   methodPost.setEntity(new UrlEncodedFormEntity(values));
		        
				   response = client.execute(methodPost);
		           
		           HttpEntity httpEnti = response.getEntity();
		           
		           jsonR = EntityUtils.toString(httpEnti);
		           
		           Log.i("Response LOGIN   : ", jsonR);		      
		           
		           //return jsonR;
		           
			}catch(Exception error){					
					Log.d("ERROR SEND RATE: ", error.getMessage());
					//return "";					
			}
			
		}

	   @Override
	   public boolean onCreateOptionsMenu(Menu menu){
		
		   	 //Inflate the menu; this adds items to the action bar if it is present.
		   	 getMenuInflater().inflate(R.menu.main, menu);
		   	 return true;
		
	   }
	   
	   private class ConnectedThread extends Thread 
	   {
		    
		  	private final InputStream mmInStream;
		    private final OutputStream mmOutStream;
		 
		    public ConnectedThread(BluetoothSocket socket) 
		    {
		        
		    	InputStream tmpIn = null;
		        OutputStream tmpOut = null;		 

		        try {
		            
		        	tmpIn = socket.getInputStream();
		            tmpOut = socket.getOutputStream();
		            
		        }catch(IOException e){ 
		        	
		        }
		 
		        mmInStream = tmpIn;
		        mmOutStream = tmpOut;
		    }
		 
		    public void run()
		    {
		        
		    	byte[] buffer = new byte[256];  
		        int bytes; 

		        while(true){
		        	
		        	try{
		            	        		
		                bytes = mmInStream.read(buffer);	
	                    h.obtainMessage(RECIEVE_MESSAGE, bytes, -1, buffer).sendToTarget();	
		            
		        	}catch (IOException e) {
		                break;
		            }
		        	
		        }
		        
		    }

		    public void write(String message) 
		    {
		    	
		    	Log.d(TAG_DEBUG, "...Data to send: " + message + "...");
		    	
		    	byte[] msgBuffer = message.getBytes();
		    	
		    	try{
		            
		    		mmOutStream.write(msgBuffer);
		            
		        }catch(IOException e){		            
		        	
		        	Log.d(TAG_DEBUG, "...Error data send: " + e.getMessage() + "...");		            		          
		        
		        }
		    	
		    }
		    
		}
	   
	   private void errorExit(String message)
	   {
		   
		   Toast.makeText(getBaseContext(),"Ups Error inesperado - " + message, Toast.LENGTH_LONG).show();
		   finish();		  
		   
	   }

	
}
