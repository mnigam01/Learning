package in.mridul.entity;

import in.mridul.strategy.NormalDriveStrategy;

public class PassengerCar extends Vehicle {
	
	public PassengerCar(){
		super(new NormalDriveStrategy());
	}
	
	

}
