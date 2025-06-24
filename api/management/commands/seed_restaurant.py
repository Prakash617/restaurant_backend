from django.core.management.base import BaseCommand
from api.models import Category, MenuItem, Table, Order, OrderItem
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with fake restaurant data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Clear existing data (optional)
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        MenuItem.objects.all().delete()
        Category.objects.all().delete()
        Table.objects.all().delete()

        # Create users
        user, _ = User.objects.get_or_create(username='waiter', defaults={'email': 'waiter@example.com'})
        user.set_password('waiter123')
        user.save()

        # Create Categories
        categories = []
        for name in ['Starters', 'Mains', 'Desserts', 'Drinks']:
            category = Category.objects.create(name=name)
            categories.append(category)

        # Create Menu Items
        menu_items = []
        for _ in range(20):
            item = MenuItem.objects.create(
                name=fake.word().capitalize() + " Dish",
                description=fake.text(),
                price=round(random.uniform(5, 50), 2),
                available=random.choice([True, True, True, False]),
                category=random.choice(categories)
            )
            menu_items.append(item)

        # Create Tables
        tables = []
        for i in range(1, 11):
            table = Table.objects.create(
                number=i,
                status=random.choice(['available', 'reserved', 'occupied'])
            )
            tables.append(table)

        # Create Orders
        for _ in range(15):
            order = Order.objects.create(
                table=random.choice(tables),
                created_by=user,
                status=random.choice(['pending', 'preparing', 'ready', 'served'])
            )
            for _ in range(random.randint(1, 4)):
                OrderItem.objects.create(
                    order=order,
                    menu_item=random.choice(menu_items),
                    quantity=random.randint(1, 3)
                )

        self.stdout.write(self.style.SUCCESS("✅ Done seeding fake restaurant data."))
