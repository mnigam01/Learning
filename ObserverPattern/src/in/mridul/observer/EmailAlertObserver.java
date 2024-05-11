package in.mridul.observer;

import in.mridul.observable.StockObservable;


public class EmailAlertObserver implements NotificationAlertObserver {
	
	private StockObservable stockObservable;
	private String email;
	
	public EmailAlertObserver(StockObservable stockObservable, String email) {
		this.stockObservable = stockObservable;
		this.email = email;
	}

	@Override
	public void update() {
		// TODO Auto-generated method stub
		sendMail("Product in stock");
	}
	
	public void sendMail(String mssge) {
		System.out.println("mail sent to: "+ this.email + " with message "+mssge);
	}

}
