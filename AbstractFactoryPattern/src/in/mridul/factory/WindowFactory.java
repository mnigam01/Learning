package in.mridul.factory;

import in.mridul.entity.Button;
import in.mridul.entity.Checkbox;
import in.mridul.entity.WinButton;
import in.mridul.entity.WinCheckBox;

public class WindowFactory implements Factory{
	public Button createButton() {
		return new WinButton();
	}
	public Checkbox createCheckBox() {
		return new WinCheckBox();
	}
}
