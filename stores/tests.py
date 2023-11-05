from django.test import TestCase
from django.urls import reverse
from stores.models import Model3d

class HomePageTests(TestCase):
    def testHomePageStatusCode(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def testViewUrlByName(self):
        response = self.client.get(reverse('home-view'))
        self.assertEquals(response.status_code, 200)



class DetailViewTest(TestCase):
    def setUp(self):
        self.model3d = Model3d.objects.create(
            title="Mon modèle 3D", 
            description="Description de mon modèle",
            views=0 ,
            image="media/TestImages/testImage.jpg"
            )

    def testDetailViewStatusCode(self):
        url = reverse('detail-view', args=[str(self.model3d.pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)




class Model3dTests(TestCase):
    def testCreateModel3d(self):
        model3d = Model3d.objects.create(
            title="Mon modèle 3D",
            description="Ceci est une description de mon modèle 3D",
            views=0 ,
            image="media/TestImages/testImage.jpg"
        )
        self.assertEqual(model3d.title, "Mon modèle 3D")
        self.assertEqual(model3d.description, "Ceci est une description de mon modèle 3D")
        self.assertEqual(model3d.views, 0)
        self.assertEqual(model3d.image, "media/TestImages/testImage.jpg")


    def testModel3dViewsIncrement(self):
        model3d = Model3d.objects.create(
            title="Modèle 3D à tester",
            description="Description du modèle 3D à tester",
            views=0,
            image="media/TestImages/testImage.jpg"
        )

        model3d.views += 1
        model3d.save()
        updatedModel3d = Model3d.objects.get(pk=model3d.pk)
        self.assertEqual(updatedModel3d.views, 1)