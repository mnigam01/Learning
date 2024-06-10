package in.mridul.observable;

import in.mridul.observer.NotificationAlertObserver;

public interface Observable {
	
	void add(NotificationAlertObserver observer);
	
	void remove(NotificationAlertObserver observer);
	
	void notifyObservers();
	
}
