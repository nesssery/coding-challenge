from django.test import TestCase
from users.models import CustomUser


class CustomUserModelTest(TestCase):
    def testCreateCustomUser(self):
        user = CustomUser.objects.create(
            username="testuser",
            email="testuser@example.com",
            phone="1234567890",
            badgeList=["Star", "Collector"],
            profileImage="media/ProfileImages/user.png"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.phone, "1234567890")
        self.assertEqual(user.badgeList, ["Star", "Collector"])
        self.assertEqual(user.profileImage, "media/ProfileImages/user.png")

    def testCustomUserStrRepresentation(self):
        user = CustomUser.objects.create(username="testuser")
        self.assertEqual(str(user), "testuser")
