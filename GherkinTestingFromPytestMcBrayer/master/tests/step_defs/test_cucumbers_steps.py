from pytest_bdd import scenario, scenarios, parsers, given, when, then
import pytest
from retirement import RetireCalc


@scenario('../features/coomba.feature', 'Customer wants to calculate retirement age info at specific date')
def test_add():
    pass


@given("a users birth year is above 1959", target_fixture='test_basket')
def test_basket():
    b_year=1971
    return b_year



@when("their birth year is entered", target_fixture= 'add_cucumbers')
def add_cucumbers(test_basket):
    return RetireCalc.calculate_retirement_age(test_basket)

@then("program returns 67 for retirement age and no error tags")
def asst_number(add_cucumbers):
    assert add_cucumbers == (67, 0)



#one

@scenario('../features/coomba.feature', 'Customer wants to calculate retirement age info if born under 1937')
def test_add():
    pass

@given("a users birth year is less than 1937", target_fixture='test_basket2')
def test_basket2():
    b_year = 1930
    return b_year

@when("their birth year is entered" , target_fixture=add_cucumbers)
def add_cucumbers(test_basket2):
    return RetireCalc.calculate_retirement_age(test_basket2)

@then("program returns 65 for retirement age and no error tags")
def asst_number(add_cucumbers):
    assert add_cucumbers == (65, 0)

#two seem to be be good

@scenario('../features/coomba.feature', 'Customer enters birth information')
def test_add():
    pass
#given these inputs return list of those inputs
@given("a users age month and birth month info are 1956, 4 ,65 ,9", target_fixture='test_basket3')
def test_basket3():
    lister = [1956, 4, 65, 9]
    return lister
    #return CucumberBasket.calculate_retirement_date(1956, 4, 65, 9)
#CucumberBasket.calculate_retirement_date(1956, 4, 65, 9)
@when("their information is entered > 12 and entered into calculator" , target_fixture='add_cucumbers')
def add_cucumbers(test_basket3):
    return RetireCalc.calculate_retirement_date(*test_basket3)

@then("the retirement year output is 2022 and 1")
def asst_number(add_cucumbers):
    assert add_cucumbers == (2022, 1)



#three done!




@scenario('../features/coomba.feature', 'Customer enters birth information')
def test_add():
    pass

@given("a user is entering their birth year information as 1956, 4, 65, 8", target_fixture='test_basket4')
def test_basket4():
    lister = [1956, 4, 65, 8]
    return lister

@when("the birth month plus age month are <=12 and entered into calculator" , target_fixture='add_cucumbers')
def add_cucumbers(test_basket4):
    return RetireCalc.calculate_retirement_date(*test_basket4)

@then("the retirement year output is 2022 and 1")
def asst_number(add_cucumbers):
    assert add_cucumbers == (2022, 1)

#good ones above ^
#5 here



@scenario('../features/coomba.feature', 'Customer enters birth and age information')
def test_add():
    pass

@given("a user has a birth year below 1900", target_fixture='test_basket5')
def test_basket5():
    lister = [1899, 4, 65, 8]
    return lister

#@when("the birth year is entered into the calculator" , target_fixture='add_cucumbers')
#def add_cucumbers(test_basket4):
#    return CucumberBasket.calculate_retirement_date(*test_basket4)

@then("pyTest raises ValueError")
def asst_number(test_basket5):
    with pytest.raises(ValueError):
        RetireCalc.calculate_retirement_date(*test_basket5)



#6 here



@scenario('../features/coomba.feature', 'Customer enters birth and age information')
def test_add():
    pass

@given("a user has a birth year of 2021+", target_fixture='test_basket6')
def test_basket6():
    lister = [2021, 4, 65, 8]
    return lister

@then("pyTest raises ValueError")
def asst_number(test_basket6):
    with pytest.raises(ValueError):
        RetireCalc.calculate_retirement_date(*test_basket6)



    #7here



@scenario('../features/coomba.feature', 'A user is entering birth and age information')
def test_add():
    pass

@given("a user's birth month is <1", target_fixture='test_basket7')
def test_basket7():
    lister = [2021, -4, 65, 8]
    return lister

@then("pyTest raises ValueError")
def asst_number(test_basket7):
    with pytest.raises(ValueError):
        RetireCalc.calculate_retirement_date(*test_basket7)


            #8 here



@scenario('../features/coomba.feature', 'A user is entering birth and age information')
def test_add():
    pass

@given("a user's birth month is >12", target_fixture='test_basket8')
def test_basket8():
    lister = [2021, 13, 65, 8]
    return lister

@then("pyTest raises ValueError")
def asst_number(test_basket8):
    with pytest.raises(ValueError):
        RetireCalc.calculate_retirement_date(*test_basket8)


#9 here

@scenario('../features/coomba.feature', 'A user is entering birth and age information')
def test_add():
    pass

@given("a user's birth age year is >67", target_fixture='test_basket9')
def test_basket9():
    lister = [2021, 13, 68, 8]
    return lister

@then("pyTest raises ValueError")
def asst_number(test_basket9):
    with pytest.raises(ValueError):
        RetireCalc.calculate_retirement_date(*test_basket9)

#10 here

@scenario('../features/coomba.feature', 'A user is entering birth and age information')
def test_add():
    pass

@given("a user's birth age year is <65", target_fixture='test_basket10')
def test_basket10():
    lister = [2021, 13, 64, 8]
    return lister

@then("pyTest raises ValueError")
def asst_number(test_basket10):
    with pytest.raises(ValueError):
        RetireCalc.calculate_retirement_date(*test_basket10)

        #11 here

#@scenario('../features/coomba.feature', 'Entering range of dates')
#def test_add():
#    pass
#@given("customer enters multiple dates", target_fixture='test_basket10')
#def test_basket11():
#    pass
#@when("user's <year> entered between 1937-1943" , target_fixture='add_cucumbers')
#def add_cucumbers(year):
#    return CucumberBasket.calculate_retirement_date(*year)
#@then("the retirement age is: <age>")
#def asst_number(age):
#    assert age == 65
