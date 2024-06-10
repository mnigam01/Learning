package in.mridul.decorator;

import in.mridul.something.BasePizza;

public class MushroomTopping extends ToppingDecorator {
	
	
	public MushroomTopping(BasePizza basePizza) {
		super(basePizza);
	}
	
	public int getCost() {
//		int x = super.getCost();
//		return x + 5;
		return super.getCost() + 5;
	}
	
	

}
