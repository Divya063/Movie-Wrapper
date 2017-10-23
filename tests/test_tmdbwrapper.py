import vcr
from pytest import fixture
from tmdbwrapper import TV

@fixture
def tv_keys():
    # Responsible only for returning the test data
    return ['id', 'origin_country', 'poster_path', 'name',
              'overview', 'popularity', 'backdrop_path',
              'first_air_date', 'vote_count', 'vote_average']


@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml')
		  
def test_tv_info():
    """Tests an API call to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
   
