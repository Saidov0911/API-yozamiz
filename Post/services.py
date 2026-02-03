# from .models import Article, Author

# # # YOMON: 100+ SQL queries
# # def get_articles_bad():
# #     articles = Article.objects.all()[:10]
# #     result = []
# #     for article in articles:
# #         comments_count = article.comments.count()
# #         author_name = article.author.name
# #         result.append({
# #             'title': article.title,
# #             'author': author_name,
# #             'comments': comments_count
# #         })
# #     return result

# # # YAXSHI: 3 SQL queries
# # def get_articles_good():
# #     articles = Article.objects.select_related(
# #         'author'
# #     ).prefetch_related('comments').all()[:10]
    
# #     result = []
# #     for article in articles:
# #         result.append({
# #             'title': article.title,
# #             'author': article.author.name,
# #             'comments': article.comments.count()  # Cacheda avvaldan
# #         })
# #     return result

# # #SUPER YAXSHI: 2 SQL queries
# # from django.db.models import Count, Prefetch

# # articles = Article.objects.select_related(
# #     'author'
# # ).annotate(
# #     comments_count=Count('comments')
# # ).all()[:10]

# # for article in articles:
# #     print(f"{article.title} - {article.comments_count} comments")


# from django.db.models import Count, Sum, Avg, Max, Min

# # Barcha maqolalar soni
# count = Article.objects.aggregate(Count('id'))
# # {'id__count': 15}

# # Jami ko'rishlar
# total_views = Article.objects.aggregate(Sum('views'))
# # {'views__sum': 5000}

# # O'rtacha ko'rish
# avg_views = Article.objects.aggregate(Avg('views'))
# # {'views__avg': 333.33}

# # Maksimal ko'rish
# max_views = Article.objects.aggregate(Max('views'))
# # {'views__max': 2000}

# # Minimal ko'rish
# min_views = Article.objects.aggregate(Min('views'))
# # {'views__min': 5}

# # Ko'p aggregates bir vaqtda
# stats = Article.objects.aggregate(
#     total_articles=Count('id'),
#     total_views=Sum('views'),
#     avg_views=Avg('views'),
#     max_views=Max('views'),
#     min_views=Min('views')
# )
# # {'total_articles': 15, 'total_views': 5000, ...}

# # Filtrlash bilan
# Article.objects.filter(published=True).aggregate(
#     published_count=Count('id'),
#     avg_views=Avg('views')
# )



# # Har bir maqola uchun kommentlar soni
# articles = Article.objects.annotate(
#     comments_count=Count('comments')
# )

# for article in articles:
#     print(f"{article.title}: {article.comments_count} comments")

# # Har bir muallif uchun yozgan maqolalar soni
# from django.db.models import Count

# authors_with_counts = Author.objects.annotate(
#     article_count=Count('articles')
# ).order_by('-article_count')

# for author in authors_with_counts:
#     print(f"{author.name}: {author.article_count} articles")

# # Murakkab - Har bir maqola uchun ko'rish-komment nisbati
# articles = Article.objects.annotate(
#     comments_count=Count('comments'),
#     avg_rating=Avg('comments__rating'),
#     total_comments_rating=Sum('comments__rating')
# )

# # Har bir kategoriya uchun o'rtacha maqola ko'rishlar
# from django.db.models import Avg

# categories = Category.objects.annotate(
#     avg_article_views=Avg('articles__views')
# )

# # Filtrlash bilan annotate
# published_with_comments = Article.objects.filter(
#     published=True
# ).annotate(
#     comment_count=Count('comments')
# )

# # Having o'xshash filtrlash
# top_commented = Article.objects.annotate(
#     comment_count=Count('comments')
# ).filter(comment_count__gte=5)








# # #  MISOLLAR
# # # 1. Har bir muallif uchun yozgan nashr qilingan maqolalar soni
# # top_authors = Author.objects.annotate(
# #     published_articles=Count('articles', filter=Q(articles__published=True)),
# #     total_views=Sum('articles__views')
# # ).order_by('-published_articles')

# # for author in top_authors:
# #     print(f"{author.name}: {author.published_articles} published")

# # # 2. Top 5 eng ko'p ko'rilgan kategoriyalar
# # from django.db.models import Sum
# # top_categories = Category.objects.annotate(
# #     total_views=Sum('articles__views')
# # ).order_by('-total_views')[:5]

# # # 3. Har bir maqola uchun o'rtacha baholash
# # articles_with_rating = Article.objects.annotate(
# #     avg_rating=Avg('comments__rating'),
# #     comment_count=Count('comments')
# # ).filter(comment_count__gt=0)

# # # 4. Yozuvchilar uchun statistika
# # author_stats = Author.objects.annotate(
# #     total_articles=Count('articles'),
# #     total_views=Sum('articles__views'),
# #     avg_views=Avg('articles__views'),
# #     recent_article=Max('articles__created_at')
# # )

# # # 5. 5+ komentga ega maqolalar
# # popular_articles = Article.objects.annotate(
# #     comment_count=Count('comments')
# # ).filter(comment_count__gte=5)





# from django.db.models import F, Q

# # Ko'rishlar sonini 1 ga oshirish (database darajasida)
# Article.objects.all().update(views=F('views') + 1)
# # SQL: UPDATE article SET views = views + 1

# # Filtrlashda F() (maqola turi bilan kategoriya solishtirlash)
# # Agar Author.first_name == 'Ali' deb olsangiz:
# # Article.objects.filter(author__name=F('category__name'))

# # O'z-o'ziga muqayasa (mavhum misol)
# # Article.objects.filter(views__gt=F('comments__count'))

# # Jami 10 ga kamaytirish
# Article.objects.all().update(views=F('views') - 10)

# # O'ng tarafda matematika
# Article.objects.all().update(
#     views=F('views') * 2
# )

# # Satr birlashtirilishi (SQLite da)
# Article.objects.all().update(
#     title=F('title') + ' - Updated'
# )


# from django.db.models import Q

# # OR - biror shartga mos
# Article.objects.filter(
#     Q(published=True) | Q(views__gt=1000)
# )
# # SELECT * FROM article WHERE published = 1 OR views > 1000

# # AND (default)
# Article.objects.filter(
#     Q(published=True) & Q(views__gt=100)
# )
# # SELECT * FROM article WHERE published = 1 AND views > 100

# # NOT
# Article.objects.filter(~Q(published=False))
# # SELECT * FROM article WHERE NOT (published = 0)

# # Murakkab kombinatsiyalar
# Article.objects.filter(
#     Q(published=True, views__gt=100) |  # (published AND views > 100)
#     Q(author__name='Ali')                # OR author = 'Ali'
# )

# # Juda murakkab
# Article.objects.filter(
#     (Q(published=True) | Q(views__gt=500)) &  # (published OR views > 500)
#     ~Q(author__name='Spam Author')             # AND NOT author = 'Spam'
# )



# 1. kelgan
# 2. Miqdor
# 3. Sotilgani


# Oy oxirida qancha mahsulot qoldi?

# n = miqdor+kelgan
# n - sotilgan = miqdor





# # MISOLLAR
# # 1. Barcha maqolalar uchun ko'rishlarni 5% ga oshirish
# from django.db.models import F, Q

# Article.objects.all().update(
#     views= F('views') * 1.05  # 5% ortiqcha
# )

# # 2. Nashr qilingan yoki 1000+ ko'rish shartlaridan biri
# trending = Article.objects.filter(
#     Q(published=True) | Q(views__gte=1000)
# )

# # 3. 'Python' bo'lgan va nashr qilingan, yoki 500+ ko'rish
# python_or_trending = Article.objects.filter(
#     Q(title__icontains='Python', published=True) |
#     Q(views__gte=500)
# )

# # 4. Nashr qilingan VA (Kategoriyasi 'Tech' YA 'Programming')
# Article.objects.filter(
#     published=True,
#     category__name__in=['Tech', 'Programming']
# ).update(views=F('views') + 100)

# # 5. Muallifi emas 'Admin' va aynan 10+ komment
# valid_articles = Article.objects.filter(
#     ~Q(author__name='Admin'),
#     comments__count__gte=10
# )

# # 6. Rating < Talab va nashr qilingan
# from django.db.models import Avg
# Article.objects.annotate(
#     avg_rating=Avg('comments__rating')
# ).filter(
#     Q(avg_rating__lt=2.0) & Q(published=True)
# )

