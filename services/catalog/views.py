from django.shortcuts import get_object_or_404, render

from services.cart.forms import CartAddProductForm

from .models import Category, Product


def product_list(request, category_slug=None):
    category = category_slug
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    if category:
        try:
            category = Category.objects.get(name=category)
            product = product.filter(category=category.id)  # type: ignore
        except Category.DoesNotExist:
            product = product.none()
    return render(request, 'catalog/list.html', {'category': category, 'categories': categories, 'product': product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/detail.html', {'product': product, 'cart_product_form': cart_product_form})
