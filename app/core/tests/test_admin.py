from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):

    def setUp(self):
        """Configuracion previa a la ejecucion de pruebas"""

        #Crear cliente
        self.client = Client()

        #Crear admin
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@admin.com',
            password = 'admin123'
        )

        #Crear una conexion con el admin que hemos creado
        self.client.force_login(self.admin_user)

        #Crear un usuario
        self.user = get_user_model().objects.create_user(
            email = 'user@user.com',
            password = 'user123',
            name = 'Usuario basico de prueba'
        )

    def test_user_listed(self):
        """Prueba que los usuarios se listan en el panel de admin"""

        url = reverse('admin:core_user_changelist')
        #print(url)

        # Peticion get a la url
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Prueba que la pagina para editar usuarios carga correctamente"""

        url = reverse('admin:core_user_change', args=[self.user.id])
        #print(url)

        res = self.client.get(url)
        print(res)

        # Verificar que el codigo devuelto este ok (200)
        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        """Prueba que la pagina para crear usuarios carga correctamente"""

        url = reverse('admin:core_user_add')

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
