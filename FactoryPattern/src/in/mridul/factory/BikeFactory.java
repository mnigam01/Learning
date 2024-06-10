package in.mridul.factory;

import in.mridul.entity.Bike;
import in.mridul.entity.Vehicle;

public class BikeFactory implements Factory{
	public Vehicle createVehicle() {
		return new Bike();
	}
}
