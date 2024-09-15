# Simple Django Rest Framework Example

This project showcases examples of using Django Rest Framework (DRF).

## drf-custom-user

- A custom user model that utilizes email as the unique identifier.
- User validation with **real email addresses and confirmation code** verification.
- For testing purposes, the expiration of the confirmation code is not limited; however, it will be set to `null` upon successful verification.

### Note

**Dont forget to set email backend through .env environment file, otherwise email confirmation will not work**

#### Relevent email setting in settings.py

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = bool(int(getenv("EMAIL_USE_TLS", 1)))
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL", "")
```
