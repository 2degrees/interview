from django.db.models import Model, CharField, ManyToManyField, DecimalField, ForeignKey, CASCADE, PositiveIntegerField


class Company(Model):
    name = CharField(max_length=128)
    co2_emission = DecimalField(decimal_places=2, max_digits=5) # in tonnes

    class Meta:
        abstract = True


class Supplier(Company):
    pass


class Buyer(Company):
    suppliers = ManyToManyField(Supplier)


class ProductionDistribution(Model):
    buyer = ForeignKey(Buyer, on_delete=CASCADE, related_name='supply_distributions')
    supplier = ForeignKey(Supplier, on_delete=CASCADE, related_name='production_distributions')
    ratio = DecimalField(decimal_places=2, max_digits=3) # 1.00 equals to 100%

    class Meta:
        unique_together = ('buyer', 'supplier')
