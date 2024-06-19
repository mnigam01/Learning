public interface BasePizza {
    int cost();
}

public class FarmHouse implements BasePizza {

    @Override
    public int cost() {
        // TODO Auto-generated method stub
        return 200;
    }

}

public class VegDelight implements BasePizza {

    @Override
    public int cost() {
        // TODO Auto-generated method stub
        return 120;
    }

}

public interface ToppingDecorator extends BasePizza {

}

public class ExtraCheese implements ToppingDecorator {
    BasePizza basePizza;
    

    public ExtraCheese(BasePizza basePizza) {
        this.basePizza = basePizza;
    }


    @Override
    public int cost() {
        // TODO Auto-generated method stub
        return this.basePizza.cost() + 10;
    }

     
}

public class Mushroom implements ToppingDecorator {
    BasePizza basePizza;
    

    public Mushroom(BasePizza basePizza) {
        this.basePizza = basePizza;
    }


    @Override
    public int cost() {
        // TODO Auto-generated method stub
        return this.basePizza.cost() + 15;
    }

     
}



public class Store {
    public static void main(String[] args) {

        
    }
}

/*

import java.util.ArrayList;


public interface SubjectInterface {
    // in interface all methods are public abstract so no need to write those
    void add(ObserverInterface observer);
    void remove(ObserverInterface observer);
    void notifySubscribers();
    void setStockCount(int newAddedStock);
    int getStockCount();
}

public class Subject implements SubjectInterface{
    List<observer> observerList = new ArrayList<>();
    int stockCount = 0;
    @Override
    public void add(ObserverInterface observer) {
        // TODO Auto-generated method stub
        observerList.add(observer);
        
    }
    @Override
    public int getStockCount() {
        // TODO Auto-generated method stub
        return stockCount;
        
    }
    @Override
    public void notifySubscribers() {
        // TODO Auto-generated method stub
        for(auto observer: observerList){
            observer.update();
        }
        
    }
    @Override
    public void remove(ObserverInterface observer) {
        // TODO Auto-generated method stub
        observerList.remove(observer);
        
    }
    @Override
    public void setStockCount(int newAddedStock) {
        // TODO Auto-generated method stub
        if (this.stockCount==0){
            notifySubscribers();
        }
        this.stockCount += newAddedStock;
        
    }

     
}


public interface ObserverInterface {
    public void update();
    
}

public class EmailObserver implements  ObserverInterface{

    String email;
    SubjectInterface observable;

    public EmailObserver(String email, SubjectInterface observable) {
        this.email = email;
        this.observable = observable;
    }

    @Override
    public void update() {
        // TODO Auto-generated method stub
        sendMail(this.email, "new stock has arrived");
        
    }

    public void sendMail(String email, String mssge){
        System.out.println("email send with message");
    }
    
}

public class MobileObserver implements  ObserverInterface{

    int mobileNo;
    SubjectInterface observable;

    public EmailObserver(int mobileNo, SubjectInterface observable) {
        this.mobileNo = mobileNo;
        this.observable = observable;
    }

    @Override
    public void update() {
        // TODO Auto-generated method stub
        sendMessage(this.mobileNo, "new stock has arrived");
        
    }

    public void sendMessage(int mobileNo, String mssge){
        System.out.println("sms send with message");
    }
    
}


public class Store {
    public static void main(String[] args) {

        ObserverInterface iphoneOberservable = new Subject();
        Subject subject1 = new EmailObserver("adfdf.com", iphoneOberservable);
        Subject subject2 = new EmailObserver("adfdf.com", iphoneOberservable);
        Subject subject3 = new MobileObserver(234, iphoneOberservable);
    }
}

*/