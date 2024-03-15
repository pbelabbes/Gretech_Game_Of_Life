import game_of_life

def test_empty_generation():
    # GIVEN
    initial_generation = ['...',
                          '...',
                          '...'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == ['...',
                      '...',
                      '...'
    ]

def test_isolation():
    # GIVEN
    initial_generation = ['...',
                          '.o.',
                          '...'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == ['...',
                      '...',
                      '...'
    ]

def test_birth():
    # GIVEN
    initial_generation = ['.oo',
                          '..o',
                          '...'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == ['.oo',
                      '.oo',
                      '...'
    ]
    
def test_birth_2():
    # GIVEN
    initial_generation = ['...',
                          'o..',
                          'oo.'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == ['...',
                      'oo.',
                      'oo.'
    ]

def test_birth_3():
    # GIVEN
    initial_generation = ['...',
                          '.o.',
                          'oo.'
    ]
    # WHEN
    actual = game_of_life.get_next_generation(
        initial_generation
    )
    # THEN
    assert actual == ['...',
                      'oo.',
                      'oo.'
    ]
    
