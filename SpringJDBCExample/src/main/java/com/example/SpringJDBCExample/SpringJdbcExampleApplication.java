package com.example.SpringJDBCExample;

import com.example.SpringJDBCExample.model.Student;
import com.example.SpringJDBCExample.service.StudentService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import java.util.List;

@SpringBootApplication
public class SpringJdbcExampleApplication {

	public static void main(String[] args) {
		ApplicationContext context = SpringApplication.run(SpringJdbcExampleApplication.class, args);
		Student student = context.getBean(Student.class);
		student.setMarks(22);
		student.setName("Mridul");
		student.setRollNo(1);

//		System.out.println(student.toString());
		StudentService service = context.getBean(StudentService.class);
		service.addStudent(student);

		List<Student> studentList = service.getStudents();
		System.out.println(studentList);



	}

}
