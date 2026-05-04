import pytest
from pydantic import ValidationError

from src.schemas.auth import (
    CreateUserRequest,
    CreateUserResponse,
    JWTTokenResponse,
    VerifyEmailRequest,
)


def test_create_user_request():
    data = {
        "email": "test@example.com",
        "password": "strongpassword123",
        "password2": "strongpassword123",
    }
    user_request = CreateUserRequest(**data)

    assert user_request.email == data["email"]
    assert user_request.password == data["password"]
    assert user_request.password2 == data["password2"]


def test_create_user_request_password_validation():
    data = {
        "email": "test@example.com",
        "password": "strongpassword123",
        "password2": "strongpassword321",
    }
    with pytest.raises(ValidationError):
        CreateUserRequest(**data)


def test_create_user_response():
    data = {"email": "test@example.com"}
    user_response = CreateUserResponse(**data)

    assert user_response.email == data["email"]


def test_verify_email_request():
    data = {"email": "test@example.com", "otp_code": "123456"}
    verify_user_request = VerifyEmailRequest(**data)

    assert verify_user_request.email == data["email"]
    assert verify_user_request.otp_code == data["otp_code"]


def test_verify_email_request_otp_code_validation():
    data_with_wrong_length = {"email": "test@example.com", "otp_code": "1234567"}
    with pytest.raises(ValidationError):
        VerifyEmailRequest(**data_with_wrong_length)

    data_with_letters = {"email": "test@example.com", "otp_code": "02D456"}
    with pytest.raises(ValidationError):
        VerifyEmailRequest(**data_with_letters)


def test_jwt_token_response():
    data = {
        "access_token": "test_access_token",
        "refresh_token": "test_refresh_token",
    }
    jwt_token = JWTTokenResponse(**data)

    assert jwt_token.access_token == data["access_token"]
    assert jwt_token.refresh_token == data["refresh_token"]
