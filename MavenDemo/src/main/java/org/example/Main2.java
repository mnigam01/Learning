package org.example;

import java.sql.*;

public class Main2 {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {

        String jdbcUrl = "jdbc:postgresql://localhost:5432/postgres";
        String username = "postgres";
        String password = "test";



        // Connect to the database
        Connection conn = DriverManager.getConnection(jdbcUrl, username, password);

        // Perform desired database operations
        System.out.println("connection established");

        String query = "select * from student";
        Statement st = conn.createStatement();
        ResultSet result = st.executeQuery(query);
        while (result.next())
        {
            String name = result.getString("name");
            int age = result.getInt("marks");
            System.out.println(name+" "+age);
        }

        query = "insert into student values (3, 'Mathew', 70)";
        st.execute(query);

        query = "select * from student";
        result = st.executeQuery(query);
        while (result.next())
        {
            String name = result.getString("name");
            int age = result.getInt("marks");
            System.out.println(name+" "+age);
        }

        // similarly update and delete query as well.


        // Close the connection
        conn.close();
    }
}