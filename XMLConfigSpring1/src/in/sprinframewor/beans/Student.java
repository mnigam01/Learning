package in.sprinframewor.beans;

public class Student {
	private String name;
	private String rollNo;
	private String emailId;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getRollNo() {
		return rollNo;
	}
	public void setRollNo(String rollNo) {
		this.rollNo = rollNo;
	}
	public String getEmailId() {
		return emailId;
	}
	public void setEmailId(String emailId) {
		this.emailId = emailId;
	}
	public void display() {
		System.out.println(this.name + " "+ this.rollNo+" "+this.emailId);
	}

}
