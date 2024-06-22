package com.example.SpringJDBCExample.dao;

import com.example.SpringJDBCExample.model.Student;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@Repository
public class StudentDao {
    private JdbcTemplate jdbcTemplate;

    public JdbcTemplate getJdbcTemplate() {
        return jdbcTemplate;
    }
    @Autowired
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public void save(Student student){
//        System.out.println("Added");
        // we have two method execute update for insert, delete and update
        // execute query for read
        // execute update we can use it's short form update
        String query = "insert into student (rollNo, name, marks) values (?,?,?)";
        int rows = jdbcTemplate.update(query, student.getRollNo(), student.getName(), student.getMarks());
        System.out.println(rows + " affected");
    }

    public List<Student> findAll() {
//        List<Student> studentList = new ArrayList<>();
//        return studentList;
        String query = "select * from student";
        RowMapper<Student> mapper = new RowMapper<Student>() {
            @Override
            public Student mapRow(ResultSet rs, int rowNum) throws SQLException {
                Student s = new Student();
                s.setRollNo(rs.getInt("rollNo"));
                s.setName(rs.getString("name"));
                s.setMarks(rs.getInt("marks"));
                return s;
            }
        };
        List<Student> studentList = jdbcTemplate.query(query, mapper);
        /* same thing as above but using lambda expression as mapper is a functional interface*/
//        List<Student> studentList = jdbcTemplate.query(query, (rs, rowNum)->{
//            Student s = new Student();
//            s.setRollNo(rs.getInt("rollNo"));
//            s.setName(rs.getString("name"));
//            s.setMarks(rs.getInt("marks"));
//            return s;
//        });
        return studentList;
    }
}
