from django.db import models
from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model


class Genre(BaseModel):
    name = models.CharField(
        _("Name"),
        max_length=255,
    )

    def __str__(self):
        return self.name


class Author(BaseModel):
    first_name = models.CharField(
        _("First Name"),
        max_length=255,
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=255,
    )
    birth_date = models.DateField(
        verbose_name=_("Birth Date"),
        null=True,
        blank=True
    )
    death_date = models.DateField(
        verbose_name=_("Death Date"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Book(BaseModel):
    title = models.CharField(
        _("Title"),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        max_length=500,
    )

    author = models.ForeignKey(
        to='Author',
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
    )
    genre = models.ForeignKey(
        to='Genre',
        verbose_name=_("Genre"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    length = models.PositiveIntegerField(
        verbose_name=_("Length"),
        default=0,
    )
    published_date = models.DateField(
        verbose_name="Published Date"
    )
    created_date = models.DateField(
        verbose_name="Created Date",
        auto_now_add=True
    )
    copies_sold = models.PositiveIntegerField(
        verbose_name=_("Copies Sold"),
        default=0,
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        decimal_places=2,
        max_digits=15
    )
    discount = models.PositiveIntegerField(
        verbose_name=_("Discount"),
        validators=[
            MaxValueValidator(100)
        ]
    )
    cover = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Rating(BaseModel):
    user = models.ForeignKey(
        to=get_user_model(),
        verbose_name=_('User'),
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        to='Book',
        verbose_name=_('Book'),
        on_delete=models.CASCADE,
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        verbose_name=_('Rating'),
    )

    def __str__(self):
        return f'{self.rating}  {self.user}\'s rating -> {self.book}'

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')
