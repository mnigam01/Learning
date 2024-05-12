package in.mridul.factory;

import in.mridul.entity.Button;
import in.mridul.entity.Checkbox;

public interface Factory {
	public Button createButton();
	public Checkbox createCheckBox();

}
