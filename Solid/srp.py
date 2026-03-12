"""
Single Responsibility Principle (SRP) states that a class 
should have only one reason to change, meaning it should 
have only one responsibility or job. This principle helps 
to create more maintainable and flexible code by ensuring 
that each class is focused on a single aspect of the functionality.


"""
class UserService:
    def __init__(self, username: str, email: str, password: str):
        self._username = username
        self._email = email
        self._password = password

    def validate_and_hash_password(self):
        # Check password strength
        # Generate salt
        # Hash with bcrypt
        pass

    def save_to_database(self):
        # Connect to database
        # Prepare SQL
        # Execute query
        pass

    def generate_auth_token(self):
        # Create JWT payload
        # Sign with secret key
        # Return token string
        pass

    def send_welcome_email(self):
        # Connect to email server
        # Build welcome template
        # Send email
        pass

# The UserService class is doing too much - it has multiple responsibilities:

#A class should have one, and only one, reason to change. — Robert C. Martin (Uncle Bob)

"""
Why does srp matter?
 - Easier to test
 - Less brittle
 - Easier to use
 - Scales well
"""

# Applying SRP


class User:
    def __init__(self, username: str, email: str, password: str):
        self._username = username
        self._email = email
        self._password = password

    def get_username(self) -> str:
        return self._username

    def get_email(self) -> str:
        return self._email

    def get_password(self) -> str:
        return self._password
    
class PasswordHasher:
    def validate_and_hash(self, password: str) -> str:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        # Generate salt and hash with bcrypt
        return "bcrypt_hashed_" + password  # Simplified for illustration

class UserRepository:
    def save(self, user: User):
        print(f"Saving user {user.get_username()} to database...")

class AuthTokenService:
    def generate_token(self, user: User) -> str:
        # Create JWT payload with user claims
        payload = f'{{"username":"{user.get_username()}","email":"{user.get_email()}"}}'
        # Sign with secret key (simplified)
        return f"eyJhbGciOiJIUzI1NiJ9.{payload}.signature"
class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to: {user.get_email()}")
        print(f"Welcome to our platform, {user.get_username()}!")


# Common pitfalls 

"""
1. Over splitting - creating too many tiny classes that are hard to manage
 -Focus on cohesion, not fragmentation. Group logic that changes together
 or belongs to the same business concern.

2. Confusing methods with Responsibilities - A method can have multiple 
steps, but the class should have one reason to change. Don't split a class
just because it has multiple methods - look at the overall responsibility
(sending emails).

3. Ignoring small classes or utility classes -Watch for creeping responsibilities
 even in utility classes. Apply SRP early, before small classes become unmanageable.

4. Misundestanding "reason to change" - Clarify the responsibility in terms of
business logic or technical behavior. Ask: Is this logic cohesive, or are unrelated
concerns bundled together?
"""