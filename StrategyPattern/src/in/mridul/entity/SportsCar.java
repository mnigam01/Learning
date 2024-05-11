package in.mridul.entity;

import in.mridul.strategy.AdvDriveStrategy;

public class SportsCar extends Vehicle {
	
	public SportsCar(){
		super(new AdvDriveStrategy());
	}

}
