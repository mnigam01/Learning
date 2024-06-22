package com.example.SpringJDBCExample.service;

import com.example.SpringJDBCExample.dao.StudentDao;
import com.example.SpringJDBCExample.model.Student;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StudentService {

    private StudentDao studentDao;

    public StudentDao getStudentDao() {
        return studentDao;
    }

    @Autowired
    public void setStudentDao(StudentDao studentDao) {
        this.studentDao = studentDao;
    }




    public void addStudent(Student student){
        studentDao.save(student);
    }

    public List<Student> getStudents() {
        return studentDao.findAll();
    }
}
