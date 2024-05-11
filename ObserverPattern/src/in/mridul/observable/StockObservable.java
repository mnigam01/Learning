package in.mridul.observable;

import java.util.ArrayList;
import java.util.List;

import in.mridul.observer.NotificationAlertObserver;

public class StockObservable implements Observable {
	
	private int stock = 0;
	private List<NotificationAlertObserver> observers = new ArrayList<>();

	@Override
	public void add(NotificationAlertObserver observer) {
		// TODO Auto-generated method stub
		observers.add(observer);

	}

	@Override
	public void remove(NotificationAlertObserver observer) {
		// TODO Auto-generated method stub
		observers.remove(observer);

	}

	@Override
	public void notifyObservers() {
		// TODO Auto-generated method stub
		for (NotificationAlertObserver observer : observers) {
			observer.update();
		}

	}

	public int getStock() {
		return stock;
	}

	public void setStock(int newStockAdded) {
		//earlier stock count was zero means no stock now from out of stock come out so notify
		if (stock==0) {  
			notifyObservers();
		}
		this.stock += newStockAdded;
	}
	
	

}
