package in.mridul.main;


import in.mridul.entity.Button;
import in.mridul.entity.Checkbox;
import in.mridul.factory.Factory;
import in.mridul.factory.WindowFactory;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Factory factory = new WindowFactory();
		Button button = factory.createButton();
		Checkbox checkBox = factory.createCheckBox();
		button.paint();
		checkBox.paint();
		

	}

}
