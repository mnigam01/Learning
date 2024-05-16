import java.util.*;



public class ParkingLotManager{

    ParkingLot parkingLot;
    
    void createParkingLot(ParkingLot parkingLot, String lotId, int floors, int slots){
        this.parkingLot = parkingLot;
        this.parkingLot.setParkingFloors(Dao().initialize(floors, slots));
        System.out.println("Created parking lot with "+ parkingLot.getNoOfFloors()+
                "floors and "+parkingLot.getNoOfSlotsPerFloor()+" slots per floor");

    }

}


public class Dao{

    public static List<ParkingFloor> parkingFloors;
    public static List<ParkingFloor> initialize(int floors, int slots){
        parkingFloors = new ArrayList<>(floors);
        for (int i=0;i<floors;i++){
            List<ParkingSlot> parkingSlots = new ArrayList<>(slots);
            for (int j=0;j<slots;j++){
                if (j==0)
                    parkingSlots.set(j,new ParkingSlot(VehicleType.TRUCK, true, j));
                else if (j<3)
                    parkingSlots.set(j,new ParkingSlot(VehicleType.BIKE, true, j));
                else
                    parkingSlots.set(j,new ParkingSlot(VehicleType.CAR, true, j));
                parkingSlots.get(j).setFloorId(i);
            }
            parkingFloors[i] = new ParkingFloor(parkingSlots);

        }
        return parkingFloors;

    } 

}


public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ParkingLotManager manager = new ParkingLotManager();
        while (true){
            String val = scan.next();
            if (val=="create_parking_lot"){
                manager.createParkingLot(new ParkingLot(scan.nextInt()), scan.nextInt(), scan.nextInt());
            }
            // else if (val=="park_vehicle"){
            //     manager.parkVehicle(VehicleType.valueOf(scan.next()), scan.next(), scan.next());
            // }else if (val=="unpark_vehicle"){
            //     manager.unParkVehicle(scan.next());
            // }else if (val=="display"){
            //     manager.display(scan.next(), scan.next());
            // }
            else{
                break;
            }
        }

    }

    
}
