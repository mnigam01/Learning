package in.mridul.main;

import in.mridul.decorator.CheeseTopping;
import in.mridul.decorator.MushroomTopping;
import in.mridul.something.BasePizza;
import in.mridul.something.Margerita;
import in.mridul.something.PlainDough;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		BasePizza plainPizza = new Margerita();
//		System.out.println(plainPizza.getCost());
//		
//		BasePizza plainMushroomPizza = new MushroomTopping(plainPizza);
//		System.out.println(plainMushroomPizza.getCost());
		
		
		BasePizza plainMushroomCheesePizza = new CheeseTopping(new MushroomTopping(new Margerita()));
		
		System.out.println(plainMushroomCheesePizza.getCost());
		
		
		BasePizza plainDoubleCheesePizza = new CheeseTopping(new CheeseTopping(new Margerita()));
		
		System.out.println(plainDoubleCheesePizza.getCost());
		
		
	}

}
