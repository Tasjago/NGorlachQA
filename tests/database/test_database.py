import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)    


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.inser_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.inser_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('Замовлення', orders)
    #Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders [0][0] == 1
    assert orders [0][1] == 'Sergii'
    assert orders [0][2] == 'солодка вода'
    assert orders [0][3] == 'з цукром'


# New tests for the individual part of Project Task 5

@pytest.mark.database
def test_insert_invalid_data_type():
    db = Database()
    with pytest.raises(Exception):
        db.inser_product(5, 'молоко', 'біла рідина', 'not_a_number')  # qnt should be an integer


@pytest.mark.database
def test_insert_negative_quantity():
    db = Database()
    db.inser_product(6, 'йогурт', 'ягідний', -5)
    qnt = db.select_product_qnt_by_id(6)
    assert qnt[0][0] == -5  # SQLite allows it, test to check unexpected values


@pytest.mark.database
def test_update_nonexistent_product():
    db = Database()
    db.update_product_qnt_by_id(999, 10)  # Product ID 999 does not exist (if not used)
    qnt = db.select_product_qnt_by_id(999)
    assert qnt == []


@pytest.mark.database
def test_multiple_inserts_and_total():
    db = Database()
    db.inser_product(10, 'печиво1', 'тест1', 5)
    db.inser_product(11, 'печиво2', 'тест2', 10)
    db.inser_product(12, 'печиво3', 'тест3', 15)
    total = db.select_product_qnt_by_id(10)[0][0] + \
            db.select_product_qnt_by_id(11)[0][0] + \
            db.select_product_qnt_by_id(12)[0][0]
    assert total == 30


@pytest.mark.database
def test_join_query_returns_valid_structure():
    db = Database()
    orders = db.get_detailed_orders()
    assert isinstance(orders, list)
    assert len(orders[0]) == 5  # id, name, product_name, description, date


@pytest.mark.database
def test_null_product_id():
    db = Database()
    with pytest.raises(Exception):
        db.select_product_qnt_by_id(None)       