package in.mridul.observer;

import in.mridul.observable.StockObservable;

public class MobileAlertObserver implements NotificationAlertObserver {

	private StockObservable stockObservable;
	private int mobileNo;
	
	public MobileAlertObserver(StockObservable stockObservable, int mobileNo) {
		this.stockObservable = stockObservable;
		this.mobileNo = mobileNo;
	}

	@Override
	public void update() {
		// TODO Auto-generated method stub
		sendMail("Product in stock");
	}
	
	public void sendMail(String mssge) {
		System.out.println("message sent to mobile: "+ this.mobileNo + " with message "+mssge);
	}

}
