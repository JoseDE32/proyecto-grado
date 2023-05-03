"""
Autor: Deiby A. Rodriguez R.
Correo: deiby.rodriguez@correounivalle.edu.co
Versión: 1.0.0
Fecha: 2023-03-28
Descripción: Este código importa los serializadores de 'Django' 'rest_framework' y los modelos 'instancia' y 'semestre'.
Luego crea dos clases de serializadores, 'instancia_serializer' y 'semestre_serializer', que se utilizan para serializar los datos de los modelos correspondientes.
La clase 'Meta' se define en cada serializador y especifica el modelo y los campos a incluir en la serialización. En este caso, se usan todos los campos de los modelos.
"""

from rest_framework import serializers
from .models import instancia, semestre

class instancia_serializer(serializers.ModelSerializer):
	class Meta:
		model = instancia
		fields = '__all__'

class semestre_serializer(serializers.ModelSerializer):
	class Meta:
		model = semestre
		fields = '__all__'
