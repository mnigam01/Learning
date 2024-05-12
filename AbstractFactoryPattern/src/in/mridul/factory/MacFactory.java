package in.mridul.factory;

import in.mridul.entity.Button;
import in.mridul.entity.Checkbox;
import in.mridul.entity.MacButton;
import in.mridul.entity.MacCheckbox;


public class MacFactory implements Factory{
	public Button createButton() {
		return new MacButton();
	}
	public Checkbox createCheckBox() {
		return new MacCheckbox();
	}
	

}
