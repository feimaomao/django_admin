# from django.conf import settings
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
# from django.db.models import Q
# from django.contrib.auth import get_user_model
#
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Permission
#
# class SettingsBackend(object):
#     def authenticate(self, username=None, password=None,userna=None,**kwargs):
#     #     UserModel = get_user_model()
#     #     username = UserModel.id
#     #     pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
#     #     userna = UserModel.userna
#     #     if username and pwd_valid and userna:
#     #         try:
#     #             user = User.objects.get(Q(username=username) | Q(userna=userna))
#     #         except User.DoesNotExist:
#     #             # Create a new user. Note that we can set password
#     #             # to anything, because it won't be checked; the password
#     #             # from settings.py will.
#     #             user = User(username=username, password='get from settings.py')
#     #             user.save()
#     #         return user
#     #     return None
#     #
#     # def get_user(self, user_id):
#     #     try:
#     #         return User.objects.get(pk=user_id)
#     #     except User.DoesNotExist:
#     #         return None
#         UserModel = get_user_model()
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         try:
#             user = UserModel._default_manager.get_by_natural_key(username)
#             if user.check_password(password):
#                 return user
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             UserModel().set_password(password)