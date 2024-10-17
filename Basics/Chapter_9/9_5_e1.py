import user_class

Mark = user_class.User('Mark','Kowalski','admin','12-12-2010',True)

Mark.increment_login_attempts()
Mark.increment_login_attempts()
Mark.increment_login_attempts()
Mark.increment_login_attempts()

print(Mark)
Mark.describe_user()
Mark.reset_login_attempts()
Mark.describe_user()