package in.mridul.main;

import in.mridul.entity.Vehicle;
import in.mridul.factory.BikeFactory;
import in.mridul.factory.CarFactory;
import in.mridul.factory.Factory;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Factory factory = new CarFactory();
		Vehicle obj = factory.createVehicle();
		obj.drive();
		

	}

}
