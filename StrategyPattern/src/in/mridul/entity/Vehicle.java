package in.mridul.entity;

import in.mridul.strategy.DriveStrategy;

public class Vehicle {
	
	DriveStrategy driveStrategy;
	Vehicle(DriveStrategy driveStrategy){
		this.driveStrategy = driveStrategy;
	}
	public void drive() {
		this.driveStrategy.drive();
	}

}
