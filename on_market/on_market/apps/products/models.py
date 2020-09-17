from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField('product name', max_length = 100)
	short_description = models.CharField('short description', max_length = 200)
	long_description = models.TextField('long description')
	price = models.IntegerField('price')
	category = models.CharField('product category', max_length = 50)
	producer = models.CharField('product producer', max_length = 50)

	def __str__(self):
		return self.product_name

	def inf(self):
		return {
				'name': self.product_name, 
				'price': self.price, 
				'short_description': self.short_description, 
				'long_description': self.long_description
				}


class Comment(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	author_name = models.CharField('author name', max_length = 50)
	comment_text = models.CharField('comment text', max_length = 500)

	def __str__(self):
		return self.author_name

	def inf(self):
		return self.author_name, self.comment_text