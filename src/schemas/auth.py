from pydantic import BaseModel, EmailStr, field_validator, model_validator


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    password2: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> "CreateUserRequest":
        if self.password != self.password2:
            raise ValueError("Passwords must match")
        return self


class CreateUserResponse(BaseModel):
    email: EmailStr


class VerifyEmailRequest(BaseModel):
    email: EmailStr
    otp_code: str

    @field_validator("otp_code")
    @classmethod
    def validate_otp_code(cls, otp_code: str) -> str:
        if len(otp_code) != 6:
            raise ValueError("OTP code must be exactly 6 characters long")
        if not otp_code.isdigit():
            raise ValueError("OTP code must contain only digits")
        return otp_code


class JWTTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
