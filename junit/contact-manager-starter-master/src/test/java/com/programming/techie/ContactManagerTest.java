package com.programming.techie;

import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

class ContactManagerTest {

    ContactManager contactManager;


    @BeforeAll
    public static void setupAll(){   // need to make class static because before all executes before the
        // initialization of ContactManagerTest object.
        System.out.println("Should print before all tests");
    }

    @BeforeEach
    public void setup(){
        contactManager = new ContactManager();  // instead of creating contactManager in
        // all classes we can create before each test case and junit will create a new manager for each
//        test case

    }

    @Test
    public void shouldCreateContact(){
//        ContactManager contactManager = new ContactManager();
        contactManager.addContact("John","Doe", "0234567890");
        Assertions.assertFalse(contactManager.getAllContacts().isEmpty());
        Assertions.assertEquals(1, contactManager.getAllContacts().size());
        Assertions.assertTrue(contactManager.getAllContacts().stream()
                .anyMatch(contact -> contact.getFirstName().equals("John") &&
                        contact.getLastName().equals("Doe") &&
                        contact.getPhoneNumber().equals("0234567890")));
    }

    @Test
    @DisplayName("Should not create contact when first name is null")
    public void shouldThrowRuntimeExceptionWhenFirstNameIsNull(){
//        ContactManager contactManager = new ContactManager();
        Assertions.assertThrows(RuntimeException.class, ()->{

            contactManager.addContact(null,"Doe", "0234567890");
        });

    }

    // similarly we can create test for last name null and phone number null also

    // Parametrized test give multiple values and check
    @DisplayName("Check different values of phone number")
    @ParameterizedTest
    @ValueSource(strings={"0123455","0234567890","9234567890"})
    public void shouldTestPhoneNumberCreationUsingValueSource(String phoneNumber){
        contactManager.addContact("John","Doe", phoneNumber);
        Assertions.assertFalse(contactManager.getAllContacts().isEmpty());
        Assertions.assertEquals(1, contactManager.getAllContacts().size());
    }
// Parametrized test give multiple values and check same as above but directly give comma sep values
    @DisplayName("Check different values of phone number")
    @ParameterizedTest
    @CsvSource({"0123455","0234567890","9234567890"})
    public void shouldTestPhoneNumberCreationUsingCSVSource(String phoneNumber){
        contactManager.addContact("John","Doe", phoneNumber);
        Assertions.assertFalse(contactManager.getAllContacts().isEmpty());
        Assertions.assertEquals(1, contactManager.getAllContacts().size());
    }


    @AfterEach
    public void tearDown(){
        System.out.println("Should execute after each test");
    }

    @AfterAll
    public static void tearDownAll(){
        System.out.println("Should be executed after the end of the test");
    }
}