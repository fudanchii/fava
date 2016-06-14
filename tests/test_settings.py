from fava.application import load_settings_from_entries

def test_settings(example_api):
    assert len(example_api.settings) == 4
    assert example_api.settings['theme'] == 'alternative'
    assert example_api.settings['charts'] == False
    assert example_api.settings['journal-show'] == 'transaction open'
    assert example_api.settings['editor-print-margin-column'] == 10

    settings = load_settings_from_entries(example_api.settings)
    assert len(settings) == 4
    assert settings['theme'] == 'alternative'
    assert settings['charts'] == False
    assert settings['journal-show'] == ['transaction', 'open']
    assert settings['editor-print-margin-column'] == 10
