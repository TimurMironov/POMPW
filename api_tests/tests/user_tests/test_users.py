from dataclasses import dataclass
from typing import Any

import allure
import pytest

from api_tests.src.services.users.endpoints import Endpoints
from api_tests.src.services.users.user_client import UserClient

# from api_tests.src.services.users.user_model import User
from api_tests.src.services.users.user_helpers import UserHelper


@dataclass
class InvalidDataCase:
    field: str
    value: Any
    expected_status: int
    expected_error: str


class TestUsers:
    # @pytest.mark.api_tests
    # def test_user_creation(self, user_client, user):
    #     User.model_validate(user)
    #     user_client.create_user(user_data=user)

    @pytest.mark.api_tests
    def test_get_user(self, user_client, created_user):
        user_id, expected_user = created_user
        actual_user = user_client.get_user(user_id)
        different_fields = UserHelper.compare_users(
            expected_user=expected_user,
            actual_user=actual_user,
        )
        assert not different_fields, f"Данные в полях {different_fields} разные"

    @pytest.mark.parametrize(
        "invalid_data_case",
        [
            pytest.param(
                InvalidDataCase(
                    field="first_name",
                    value="",
                    expected_status=422,
                    expected_error="String should have at least 1 character",
                ),
                id="Empty name",
            ),
            pytest.param(
                InvalidDataCase(
                    field="age",
                    value="abc",
                    expected_status=422,
                    expected_error="Input should be a valid integer, unable to parse string as an integer",
                ),
                id="Invalid age type",
            ),
            pytest.param(
                InvalidDataCase(
                    field="gender",
                    value="Unknown",
                    expected_status=422,
                    expected_error="IInput should be 'male' or 'female'",
                ),
                id="Invalid gender value",
            ),
        ],
    )
    def test_create_user_invalid_data(
            self,
            generated_user: dict[str, Any],
            user_client: UserClient,
            invalid_data_case: InvalidDataCase,
    ):
        with allure.step(f"Заменить поле {invalid_data_case.field} на некорректное {invalid_data_case.value}"):
            generated_user[invalid_data_case.field] = invalid_data_case.value
        with allure.step(
                "Отправить запрос на добавление user в БД с невалидными данными"
        ):
            response = user_client.post(
                endpoint=Endpoints.create_user(),
                json=generated_user,
            )
        with allure.step(
                f"Проверить, что статус - {invalid_data_case.expected_status}\n"
                f"и ошибка в ответе - {invalid_data_case.expected_error}"
        ):
            assert response.status_code == invalid_data_case.expected_status
            assert response.json()["detail"][0]["msg"] == invalid_data_case.expected_error
        with allure.step("Проверить, что пользователь в БД не создался"):
            response = user_client.search_user_by_email(
                generated_user["contact"]["email"]
            )
            assert response.status_code == 404

    @pytest.mark.api_tests
    def test_get_users(self, user_client):
        users = user_client.get_users()
        assert users[0].first_name == "Дмитрий"
