from django.test import TestCase
from .models import Pets


def create_pet(name):
    return Pets.objects.create(name=name)


class PetsModelTests(TestCase):
    def test_update_success(self):
        """
        test that update is successful
        """
        pet = create_pet('old_name')
        res = self.client.patch('/pets/' + str(pet.id) + '/', '{"name": "new_name"}', 'application/json')
        # print(res)
        pet_from_db = Pets.objects.get(id=pet.id)

        self.assertEqual(pet_from_db.name, 'new_name')
