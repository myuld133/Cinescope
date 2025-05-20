from constants import MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester


class MoviesAPI(CustomRequester):
    """
      Класс для работы с афишей фильмов.
      """

    def __init__(self, session):
        super().__init__(session=session, base_url="https://api.dev-cinescope.coconutqa.ru")

    def get_list_all_movies(self, expected_status=200, params=None):
        response = self.send_request(
            method='GET',
            endpoint=MOVIES_ENDPOINT,
            expected_status=expected_status,
            params=params
        )
        return response.json()['movies']

    def get_one_movie(self, movie_id, expected_status=200):
        return self.send_request(
            method='GET',
            endpoint=f'{MOVIES_ENDPOINT}/{movie_id}',
            expected_status=expected_status
        )

    def create_new_film(self, film_data, expected_status=201):
        return self.send_request(
            method='POST',
            endpoint=MOVIES_ENDPOINT,
            data=film_data,
            expected_status=expected_status
        )

    def delete_film(self, movie_id, expected_status=200):
        return self.send_request(
            method='DELETE',
            endpoint=f'{MOVIES_ENDPOINT}/{movie_id}',
            expected_status=expected_status
        )

    def get_reviews(self, movie_id, expected_status=200):
        return self.send_request(
            method='GET',
            endpoint=f'{MOVIES_ENDPOINT}/{movie_id}/reviews',
            expected_status=expected_status
        )

    def create_review(self, movie_id, review_data, expected_status=200):
        return self.send_request(
            method='POST',
            endpoint=f'{MOVIES_ENDPOINT}/{movie_id}/reviews',
            data=review_data,
            expected_status=expected_status
        )