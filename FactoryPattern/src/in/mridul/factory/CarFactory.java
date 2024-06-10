package in.mridul.factory;

import in.mridul.entity.Car;
import in.mridul.entity.Vehicle;

public class CarFactory implements Factory{
	public Vehicle createVehicle() {
		return new Car();
	}

}
