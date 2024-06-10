package in.mridul.main;

import in.mridul.observable.IphoneObservable;
import in.mridul.observable.MacBookObservable;
import in.mridul.observable.StockObservable;
import in.mridul.observer.EmailAlertObserver;
import in.mridul.observer.MobileAlertObserver;
import in.mridul.observer.NotificationAlertObserver;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StockObservable iphoneStockObservable = new IphoneObservable();
		NotificationAlertObserver observer1 = new EmailAlertObserver(iphoneStockObservable, "abc");
		NotificationAlertObserver observer2 = new EmailAlertObserver(iphoneStockObservable, "def");
		NotificationAlertObserver observer3 = new MobileAlertObserver(iphoneStockObservable, 1234);
		
		StockObservable macBookStockObservable = new MacBookObservable();
		NotificationAlertObserver observer11 = new EmailAlertObserver(macBookStockObservable, "ABC");
		NotificationAlertObserver observer21 = new MobileAlertObserver(macBookStockObservable, 9289);
		NotificationAlertObserver observer31 = new EmailAlertObserver(macBookStockObservable, "DEF");
		
		iphoneStockObservable.add(observer1);
		iphoneStockObservable.add(observer2);
		iphoneStockObservable.add(observer3);
		
		macBookStockObservable.add(observer11);
		macBookStockObservable.add(observer21);
		macBookStockObservable.add(observer31);
		
		iphoneStockObservable.setStock(5);

		
		macBookStockObservable.setStock(2);
		
		iphoneStockObservable.setStock(-5);
		iphoneStockObservable.setStock(15);

	}

}
