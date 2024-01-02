Feature: Creating a facility
  Scenario: Creating a new facility in desktop app
    Given User is on Desktop application
    When User navigate to the facility section
    And User creates a new  facility
    |Facility_name |Standard  |	Address	  |City |State|Postal Code |   Country    |
    |Test_Facility |	HTM02-01|	{Datetime}|	NA  |	    |  NA	       |United Kingdom|
    Then the facility is created successfully
