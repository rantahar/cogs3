from selenium_base import SeleniumTestsBase


class UserIntegrationTests(SeleniumTestsBase):

    def test_user_login(self):
        """
        Sign in as an external user
        """
        # Just sign in. There is an assert in the sign_in function
        users = [
            self.user,
            self.external,
            self.student,
            self.rse,
            self.admin,
        ]
        for user in users:
            self.sign_in(user)
            self.log_out()
