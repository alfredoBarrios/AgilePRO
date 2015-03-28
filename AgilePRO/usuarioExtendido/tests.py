"""from django.test import TestCase
from whatever.models import Whatever
from django.utils import timezone
from django.core.urlresolvers import reverse
from whatever.forms import WhateverForm

# models test
class WhateverTest(TestCase):

    def create_whatever(self, title="only a test", body="yes, this is only a test"):
        return Whatever.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Whatever))
        self.assertEqual(w.__unicode__(), w.title)
"""

from django.test import TestCase

from usuarioExtendido.models import usuario
from psycopg2.tests.testutils import unittest
class testUsuarioExtendido(TestCase):
    def crear_usuario_extendido(self):
        a=usuario.objects.create(telefono='0981595590')
        a.save()

unittest.main()