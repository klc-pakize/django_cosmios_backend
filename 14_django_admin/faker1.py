from products.models import Products, Review
from faker import Faker

def run1():
    '''
        python manage.py shell
        from faker1 import run1
        run1()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''

    faker = Faker()

    for i in range(1,200):
        product = Products(name=faker.name(),description=faker.paragraph(),is_in_stock=False)
        product.save()
    print('OK')


def run2():
    '''
        python manage.py shell
        from faker1 import run2
        run2()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''

    faker = Faker()

    for product in Products.objects.iterator():
        reviews = [Review(review=faker.paragraph(), product=product) for _ in range(0,4)]
        Review.objects.bulk_create(reviews)


    print('OK')