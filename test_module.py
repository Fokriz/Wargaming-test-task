import pytest

@pytest.mark.parametrize('ship', list(range(200)))
def test_weapon(ship, db_fixture):
    data_ship = db_fixture['db'].select('Weapons', 'Ship-' + str(ship))
    data_ship_temp = db_fixture['db_temp'].select('Weapons', 'Ship-' + str(ship))
    output = 'Ship-{0}, {1}'

    if data_ship != data_ship_temp:
        output = output.format(ship, data_ship_temp[0][0])

        if data_ship[0][0] != data_ship_temp[0][0]:
            assert data_ship[0][0] == data_ship_temp[0][0], \
                output + '\n\texpected {0}, was {1}'.format(data_ship_temp[0][0],
                                                            data_ship[0][0])
        else:
            weapon_values = [
                '',
                'reload_speed',
                'rotation_speed',
                'diameter',
                'power_volley',
                'count']
            for i in range(1, 6):
                if data_ship_temp[0][i] != data_ship[0][i]:
                    output += '\n\t{0}: expected {1}, was {2}'.format(weapon_values[i],
                                                                      data_ship_temp[0][i],
                                                                      data_ship[0][i])
            assert 0, output



@pytest.mark.parametrize('ship', list(range(200)))
def test_hull(ship, db_fixture):
    data_ship = db_fixture['db'].select('Hulls', 'Ship-' + str(ship))
    data_ship_temp = db_fixture['db_temp'].select('Hulls', 'Ship-' + str(ship))
    output = 'Ship-{0}, {1}'

    if data_ship != data_ship_temp:
        output = output.format(ship, data_ship_temp[0][0])


        if data_ship[0][0] != data_ship_temp[0][0]:
            assert data_ship[0][0] == data_ship_temp[0][0], \
                output + '\n\texpected {0}, was {1}'.format(data_ship_temp[0][0],
                                                            data_ship[0][0])
        else:
            hull_values = ['', 'armor', 'type', 'capacity']
            for i in range(1, 4):
                if data_ship_temp[0][i] != data_ship[0][i]:
                    output += '\n\t{0}: expected {1}, was {2}'.format(hull_values[i],
                                                                      data_ship_temp[0][i],
                                                                      data_ship[0][i])
            assert 0, output

@pytest.mark.parametrize('ship', list(range(200)))
def test_engine(ship, db_fixture):
    data_ship = db_fixture['db'].select('Engines', 'Ship-' + str(ship))
    data_ship_temp = db_fixture['db_temp'].select('Engines', 'Ship-' + str(ship))
    output = 'Ship-{0}, {1}'

    if data_ship != data_ship_temp:
        output = output.format(ship, data_ship_temp[0][0])

        if data_ship[0][0] != data_ship_temp[0][0]:
            assert data_ship[0][0] == data_ship_temp[0][0], \
                output + '\n\texpected {0}, was {1}'.format(data_ship_temp[0][0],
                                                            data_ship[0][0])
        else:
            engine_values = ['', 'power', 'type']
            for i in range(1, 3):
                if data_ship_temp[0][i] != data_ship[0][i]:
                    output += '\n\t{0}: expected {1}, was {2}'.format(engine_values[i],
                                                                      data_ship_temp[0][i],
                                                                      data_ship[0][i])
            assert 0, output
