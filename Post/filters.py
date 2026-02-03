# from .models import Article

# # TENG BO'LISH
# Article.objects.filter(published=True)
# # SELECT * FROM article WHERE published = 1

# # I (IN) - bir nechta qiymatdan birortasiga teng
# Article.objects.filter(author_id__in=[1, 2, 3])
# # SELECT * FROM article WHERE author_id IN (1, 2, 3)

# # GT (GREATER THAN) - katta
# Article.objects.filter(views__gt=100)
# # SELECT * FROM article WHERE views > 100

# # GTE (GREATER THAN EQUAL) - katta yoki teng
# Article.objects.filter(views__gte=100)

# # LT (LESS THAN) - kichik
# Article.objects.filter(views__lt=50)

# # LTE (LESS THAN EQUAL) - kichik yoki teng
# Article.objects.filter(views__lte=50)

# # RANGE - oraliqda
# Article.objects.filter(views__range=[10, 100])
# # SELECT * FROM article WHERE views BETWEEN 10 AND 100

# # CONTAINS - o'z ichiga oladi (case-sensitive)
# Article.objects.filter(title__contains='Django')
# # SELECT * FROM article WHERE title LIKE '%Django%'

# # ICONTAINS - o'z ichiga oladi (case-insensitive)
# Article.objects.filter(title__icontains='django')

# # STARTSWITH - bilan boshlanadi
# Article.objects.filter(title__startswith='The')

# # ENDSWITH - bilan tugaydi
# Article.objects.filter(title__endswith='Django')

# # ISNULL - NULL bo'lish
# Article.objects.filter(category__isnull=True)
# Article.objects.filter(category__isnull=False)

# # YEAR, MONTH, DAY - sana bo'yicha
# Article.objects.filter(created_at__year=2024)
# Article.objects.filter(created_at__month=12)
# Article.objects.filter(created_at__day=25)

# # Boshqa lookups
# Article.objects.filter(created_at__date=datetime.date(2024, 1, 15))
# Article.objects.filter(created_at__time=datetime.time(12, 0))


# ########## Ketma-ket filterlash (Chaining) ###########

# # Bu QuerySet AND operatoridan foydalanadi
# Article.objects.filter(published=True).filter(views__gt=100).filter(author__name='Ali')
# # Ekvivalent:
# # SELECT * FROM article 
# # WHERE published = 1 AND views > 100 AND author.name = 'Ali'

# # Bir qatorda
# Article.objects.filter(published=True, views__gt=100, author__name='Ali')


# #### Get()  #######

# # Bitta ob'ektni olish
# article = Article.objects.get(id=1)
# article = Article.objects.get(title='Django Masterclass')

# # Exception qaytarish
# try:
#     article = Article.objects.get(id=999)
# except Article.DoesNotExist:
#     print("Maqola topilmadi")

# try:
#     article = Article.objects.get(published=True)  # 1+ natija bo'lsa
# except Article.MultipleObjectsReturned:
#     print("Bir nechta maqola topildi")

# # .get() yoki None qaytarish
# article = Article.objects.filter(id=1).first()
# # Yoki
# from django.shortcuts import get_object_or_404
# article = get_object_or_404(Article, id=1)


# ############ .exclude() ################

# # Nashr qilinmagan maqolalarni olish
# unpublished = Article.objects.exclude(published=True)
# # Ekvivalent:
# # SELECT * FROM article WHERE published = 0

# # Bir nechta shart bilan
# Article.objects.exclude(published=True, author__name='Ali')

# # Chainlash
# Article.objects.filter(views__gt=100).exclude(published=False)


# articles = Article.objects.all()[:10]
# for article in articles:
#     print(article.author.name)
# 1 + 10 = 11 SQL query

# # SQL:
# # SELECT * FROM article LIMIT 10  (1-so'rov)
# # SELECT * FROM author WHERE id = 1  (2-so'rov)
# # SELECT * FROM author WHERE id = 2  (3-so'rov) - takror!
# # ...va hokazo


# articles = Article.objects.select_related('author').all()[:10]
# for article in articles:
#     print(article.author.name)  # Avvaldan yuklanmagan

# # 1 ta JOIN so'rov
# # SELECT article.*, author.* 
# # FROM article 
# # JOIN author ON article.author_id = author.id 
# # LIMIT 10



