package com.health.mod;

import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.util.Log;

public class GeoLocation implements LocationListener 
{

	
	private LocationManager locationManager;
	private int option = 0;
	
	public static final int GPS = 1;
	public static final int NETWORK = 2;
	
	public GeoLocation (int code, Context context)
	{
		
		locationManager = (LocationManager)context.getSystemService(Context.LOCATION_SERVICE);
		
		this.option = code;
		
		initializeLocationWithOption(code);
		
		
	}
	
	
	/*
	 * Retorno un vector cuyos indices son 0 longitud y 1 es latitud
	 */
	public double[] getLocation()
    {
    				
			try{
					
				
				Location place = null;
				double[] resultLocation =  new double[2];
				
					switch (option)
					{
					
						case GPS:
														
							place  = locationManager
			                		.getLastKnownLocation(LocationManager.GPS_PROVIDER);	
							
							
							break;
							
						case NETWORK:
							
							
							
							place = locationManager
									.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
							
							
							
							break;
						
					
					}
														
					resultLocation[0] = place.getLongitude();
					resultLocation[1] = place.getLatitude();
					
					
					return resultLocation;
					
					
			}catch(Exception error){
				
				Log.d("ERROR CLASS GEO LOCATION - GET LOCATION", error.getMessage());
				
			}
			  
    	return null;
			
    }
	
	private void initializeLocationWithOption(int code)
	{
		
		switch (code) {
			
		
			case GPS:				
				
		        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0,
		                0, this);
				
				break;
	
			case NETWORK:
				
				locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0,
		                0, this);
				
				break;
						
		}
		
		
	}


	@Override
	public void onLocationChanged(android.location.Location arg0) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void onProviderDisabled(String arg0) {
		
	}


	@Override
	public void onProviderEnabled(String arg0) {
		
		
	}


	@Override
	public void onStatusChanged(String arg0, int arg1, Bundle arg2) {
		
	}
	
	
	
}
