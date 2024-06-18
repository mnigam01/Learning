package org.example;

import java.sql.*;

public class Main {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {

        // see below for example
        // https://tembo.io/docs/getting-started/postgres_guides/connecting-to-postgres-with-java

        String jdbcUrl = "jdbc:postgresql://localhost:5432/database_name";
        String username = "username";
        String password = "password";


        // Connect to the database
        Connection conn = DriverManager.getConnection(jdbcUrl, username, password);

        // Perform desired database operations

        // Close the connection
        conn.close();
    }
}