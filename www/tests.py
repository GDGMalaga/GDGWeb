from django.test import TestCase
from django.utils import timezone
import datetime
from www.models import Curso, Grupo

# Create your tests here.


class CursoGrupoTests(TestCase):

    # Test de calentamiento
    def test_is_curso_in_grupo(self):
        gdg = Grupo(name='GDGDevelopers', pub_date=timezone.now())
        gdg.save()
        c1 = Curso(name='django for noobs',
                        pub_date=timezone.now(),
                        date_activity=timezone.now(),
                        location='ETSII',
                        information='blah blah blah',
                        grupo=gdg)
        c1.save()
        self.assertEqual(c1.grupo.name, 'GDGDevelopers')
