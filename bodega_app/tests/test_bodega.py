from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from bodega_app.models import Bodega
from bodega_app.views import BodegaViewSet


class YourTestClass(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.node_1=Bodega.objects.create(
            nombre_corto='pbr1',
            nombre = 'prueba bodega 1',
            capacidad_maxima=50,
            direccion='CR 1 # 1 - 1 Barrio - Ciudad - Departamento',
            numero_telefonico='3001011010',
            correo_electronico='pbr1@gmail.com',
            descripcion='Prueba bodega # 1'
        )
        self.node_2=Bodega.objects.create(
            nombre_corto='pbr2',
            nombre = 'prueba bodega 2',
            capacidad_maxima=50,
            direccion='CR 2 # 2 - 2 Barrio - Ciudad - Departamento',
            numero_telefonico='3001011010',
            correo_electronico='pbr2@gmail.com',
            descripcion='Prueba bodega # 2'
        )
        self.node_3=Bodega.objects.create(
            nombre_corto='pbr3',
            nombre = 'prueba bodega 3',
            capacidad_maxima=50,
            direccion='CR 3 # 3 - 3 Barrio - Ciudad - Departamento',
            numero_telefonico='3001011010',
            correo_electronico='pbr3@gmail.com',
            descripcion='Prueba bodega # 3'
        )
        self.node_4=Bodega.objects.create(
            nombre_corto='pbr4',
            nombre = 'prueba bodega 4',
            capacidad_maxima=50,
            direccion='CR 4 # 4 - 4 Barrio - Ciudad - Departamento',
            numero_telefonico='3001011010',
            correo_electronico='pbr4@gmail.com',
            descripcion='Prueba bodega # 4'
        )
        self.node_5=Bodega.objects.create(
            nombre_corto='pbr5',
            nombre = 'prueba bodega 5',
            capacidad_maxima=50,
            direccion='CR 5 # 5 - 5 Barrio - Ciudad - Departamento',
            numero_telefonico='3001011010',
            correo_electronico='pbr5@gmail.com',
            descripcion='Prueba bodega # 5'
        )
        self.node_6=Bodega.objects.create(
            nombre_corto='pbr6',
            nombre = 'prueba bodega 6',
            capacidad_maxima=50,
            direccion='CR 6 # 6 - 6 Barrio - Ciudad - Departamento',
            numero_telefonico='3001011010',
            correo_electronico='pbr6@gmail.com',
            descripcion='Prueba bodega # 6'
        )
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
