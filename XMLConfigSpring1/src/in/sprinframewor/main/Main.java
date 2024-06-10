package in.sprinframewor.main;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import in.sprinframewor.beans.Student;




public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		ApplicationContext context = new ClassPathXmlApplicationContext();
		String confLoc = "/in/sprinframewor/resources/applicationContext.xml";
		ApplicationContext context = new ClassPathXmlApplicationContext(confLoc);
		
		Student std = (Student) context.getBean("student1");
		std.display();
		
		

	}

}
