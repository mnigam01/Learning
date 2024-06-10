package in.mridul.decorator;

import in.mridul.something.BasePizza;

public class CheeseTopping extends ToppingDecorator {
	
	public CheeseTopping(BasePizza basePizza) {
		super(basePizza);
	}
	
	public int getCost() {
//		int x = super.getCost();
//		return x + 36;
		return super.getCost() + 36;
	}

}
