package me.whiteship.refactoring._22_data_class._42_encapsulate_record;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class OrganizationTest {

    @Test
    void name(){
        Organization organization =new Organization();
        organization.name = "keesun";
    }
}