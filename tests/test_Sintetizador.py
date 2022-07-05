from Sintetizador.principal_file import Sintetizer

test_sinte = Sintetizer(44100, 'test_oboe.txt', 'test_musical_escale.txt', 'wave_test.wav')

def test_instrument():
    expected = ([1, 2, 3, 4, 5, 6, 7, 8],
            [0.0577501, 0.0577501, 0.063525, 0.12705, 0.10395, 0.1155, 0.1155, 0.1155], 
            {'TRI': [0.05, 0.03, 1.3], 'CONSTANT': [], 'INVLINEAR': [0.02]})
    assert test_sinte.instrument( test_sinte.instrument_info) == expected

def test_read_sheet():
    expected = [('0.0', 'B4', '0.5'),
                ('0.5', 'Bb4', '0.5'),
                ('1.0', 'A4', '0.5'),
                ('1.5', 'Ab4', '0.5'),
                ('2.0', 'G4', '0.5'),
                ('2.5', 'Gb4', '0.5'),
                ('3.0', 'F4', '0.5'),
                ('3.5', 'E4', '0.5'),
                ('4.0', 'Eb4', '0.5'),
                ('4.5', 'D4', '0.5'),
                ('5.0', 'Db4', '0.5'),
                ('5.5', 'C4', '0.5')]    
    assert test_sinte.read_sheet(test_sinte.sheet) == expected

def test_track():
    test_sinte.generate_track()
    

            


