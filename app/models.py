from django.db import models

class Klass_Name(models.Model):
	name = models.CharField('Класс', max_length=3, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural= 'Числа'
		verbose_name= 'Создать Число класса'

class Klass(models.Model):
	class_name = models.CharField('Название класса', max_length=20, blank=True, null=True)
	klass_name = models.ForeignKey(Klass_Name, max_length=20, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Цыфра класса')
	
	def __str__(self):
		return self.class_name

	class Meta:
		verbose_name_plural= 'Классы'
		verbose_name= 'Создать класса'

class Children(models.Model):
	last_name = models.CharField('Фамилия', max_length=20, blank=True, null=True)
	name = models.CharField('Имя', max_length=10, blank=True, null=True)
	klass = models.ForeignKey(Klass, max_length=20, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Класса')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural= 'Ученики'
		verbose_name= 'Создать Ученика'

class Teacher(models.Model):
	last_name = models.CharField('Фамилия', max_length=20, blank=True, null=True)
	name = models.CharField('Имя', max_length=10, blank=True, null=True)
	lesson = models.CharField('Предмет', max_length=15, blank=True, null=True)
	klass = models.ForeignKey(Klass, max_length=20, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Класса')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural= 'Учителя'
		verbose_name= 'Создать Учителя'

class Boss(models.Model):
	last_name = models.CharField('Фамилия', max_length=20, blank=True, null=True)
	name = models.CharField('Имя', max_length=10, blank=True, null=True)
	job = models.CharField('Должность', max_length=15, blank=True, null=True)
	lesson = models.CharField('Предмет(если есть)', max_length=15, blank=True, null=True)
	
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural= 'Главные'
		verbose_name= 'Создать Главного'

class NewsLine(models.Model):
	title = models.CharField('Название', max_length=30, blank=True, null=True)
	image1 = models.ImageField('Фото 1', blank=True, null=True)
	image2 = models.ImageField('Фото 2', blank=True, null=True)
	image3 = models.ImageField('Фото 3', blank=True, null=True)
	date = models.DateTimeField('Дата выпуска', auto_now_add=True, blank=True, null=True)
	inf = models.TextField('Иформация',max_length=300, blank=True, null=True)

	def __str__(self):
		return self.title
    
	class Meta:
		verbose_name_plural= 'Посты'
		verbose_name= 'Создать Пост'
		ordering = '-date',