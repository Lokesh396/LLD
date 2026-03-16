from abc import ABC, abstractmethod
from typing import List

# Before: Fat interface bundles three unrelated sets of operations
class UserService(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str):
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> str:
        pass

    @abstractmethod
    def update_user(self, user_id: str, new_email: str):
        pass

    @abstractmethod
    def delete_user(self, user_id: str):
        pass

    @abstractmethod
    def ban_user(self, user_id: str, reason: str):
        pass

    @abstractmethod
    def promote_user(self, user_id: str, role: str):
        pass

    @abstractmethod
    def get_login_history(self, user_id: str) -> List[str]:
        pass

    @abstractmethod
    def get_activity_log(self, user_id: str) -> List[str]:
        pass

class BasicUserService(UserService):
    def create_user(self, name, email):
        print(f"Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"Deleting user: {user_id}")

    def ban_user(self, user_id, reason):
        raise NotImplementedError("Not an admin service.")

    def promote_user(self, user_id, role):
        raise NotImplementedError("Not an admin service.")

    def get_login_history(self, user_id):
        raise NotImplementedError("No audit capability.")

    def get_activity_log(self, user_id):
        raise NotImplementedError("No audit capability.")

# if __name__ == "__main__":
#     svc = BasicUserService()
#     svc.create_user("Alice", "alice@example.com")
#     svc.get_user("u123")

# TODO: Create UserCrud, AdminControls, and AuditLog interfaces.
# TODO: Refactor BasicUserService to implement only UserCrud.
# TODO: Create an AdminUserService that implements UserCrud and AdminControls.
# TODO: Create a FullUserService that implements all three interfaces.


class UserCrud(ABC):

    @abstractmethod
    def create_user(self, name, email):
        pass

    @abstractmethod
    def update_user(self,user_id, new_email):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

class AdminControls(ABC):

    @abstractmethod
    def ban_user(self, user_id):
        pass

    @abstractmethod
    def promote_user(self, user_id):
        pass

class AuditLog(ABC):

    @abstractmethod
    def getLoginHisotry(self, user_id):
        pass

    @abstractmethod
    def getActivityLog(self, user_id):
        pass


class BasicuserService(UserCrud):

    def create_user(self, name, email):
        print(f"Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"Deleting user: {user_id}")

class AdminUserService(UserCrud, AdminControls):
    def create_user(self, name, email):
        print(f"Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"Deleting user: {user_id}")

    def ban_user(self, user_id, reason):
        print(f'user with the userid - {user_id} banned for the following reason: {reason}')

    def promote_user(self, user_id, role):
        print(f'user with the userid - {user_id} promtoed to the {role}')


class FullUserService(UserCrud, AdminControls, AuditLog):
    def create_user(self, name, email):
        print(f"Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"Deleting user: {user_id}")

    def ban_user(self, user_id, reason):
        print(f'user with the userid - {user_id} banned for the following reason: {reason}')

    def promote_user(self, user_id, role):
        print(f'user with the userid - {user_id} promtoed to the {role}')

    def getLoginHisotry(self, user_id):
        print(f'Login History of the  userid - {user_id}')

    def getActivityLog(self, user_id):
        print(f'Activity Log of the  userid - {user_id}')


if __name__ == '__main__':
    basicuserservice = BasicuserService()
    basicuserservice.create_user('Lokesh', 'lokesh.c@gmail.com')

    adminservice = AdminUserService()
    adminservice.promote_user('123', 'sde2')

    fulluser = FullUserService()
    fulluser.getActivityLog('123')