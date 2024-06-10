package in.mridul.decorator;

import in.mridul.something.BasePizza;

public abstract class ToppingDecorator implements BasePizza{
	private BasePizza basePizza;
	
	public ToppingDecorator(BasePizza basePizza) {
		this.basePizza = basePizza;
	}
	public int getCost()
	{
//		int x = this.basePizza.getCost();
//		return x;
		return this.basePizza.getCost();
	}

}
