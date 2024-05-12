public interface Button {
	public void paint();

}

public interface Checkbox {
	
	public void paint();

}

public class MacButton implements Button{
	public void paint() {
		System.out.println("you have loaded mac button");
	}
}

public class MacCheckbox implements Checkbox{
	public void paint() {
		System.out.println("you have loaded mac checkobx");
	}
}

public class WinButton implements Button{
	public void paint() {
		System.out.println("you have loaded window button");
	}
}

public class WinCheckBox implements Checkbox{
	public void paint() {
		System.out.println("you have loaded window chekbox");
	}
}

public interface Factory {
	public Button createButton();
	public Checkbox createCheckBox();

}


public class WindowFactory implements Factory{
	public Button createButton() {
		return new WinButton();
	}
	public Checkbox createCheckBox() {
		return new WinCheckBox();
	}
}

public class MacFactory implements Factory{
	public Button createButton() {
		return new MacButton();
	}
	public Checkbox createCheckBox() {
		return new MacCheckbox();
	}
	
}


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







