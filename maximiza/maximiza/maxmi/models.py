from django.db import models

class Quem_Somos(models.Model):
	title= models.CharField('Titulo', max_length = 100)
	description = models.TextField('Descrição', blank=True)
	image = models.ImageField(upload_to='midia/quem_somos',verbose_name='Imagem',
		null=True , blank=True
		)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Descrição/Foto'
		verbose_name_plural = 'Quem Somos'
		ordering = ['title']

class Portifolio(models.Model):
	title = models.CharField('Titulo',max_length=100)
	image = models.ImageField(upload_to='midia/portifolio',verbose_name='Imagem',
		null=True , blank=True
		)
