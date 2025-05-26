# Django REST Framework: ViewSets with Mixins

---

## 🔹 What are ViewSets with Mixins?

DRF provides a modular way to build ViewSets using combinations of:

* `CreateModelMixin`
* `ListModelMixin`
* `RetrieveModelMixin`
* `UpdateModelMixin`
* `DestroyModelMixin`
* `GenericViewSet` (base class to enable ViewSet behavior)

These allow you to define only the actions you need, with clean and readable code.

---

## 📦 1. List View — `ListModelMixin`

```python
from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductListViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

🟢 **GET `/products/`** — Returns a list of products.

---

## 🆕 2. Create View — `CreateModelMixin`

```python
class ProductCreateViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

🟢 **POST `/products/`** — Creates a new product.

---

## 🔍 3. Detail View — `RetrieveModelMixin`

```python
class ProductDetailViewSet(mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

🟢 **GET `/products/<id>/`** — Retrieves a product by ID.

---

## ✏️ 4. Update View — `UpdateModelMixin`

```python
class ProductUpdateViewSet(mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

🟢 **PUT `/products/<id>/`** — Updates a product.

---

## ❌ 5. Delete View — `DestroyModelMixin`

```python
class ProductDeleteViewSet(mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

🟢 **DELETE `/products/<id>/`** — Deletes a product.

---

## 🧩 Full CRUD ViewSet — `ModelViewSet`

```python
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

✅ Equivalent to combining:

* `CreateModelMixin`
* `ListModelMixin`
* `RetrieveModelMixin`
* `UpdateModelMixin`
* `DestroyModelMixin`
* `GenericViewSet`

---

## 🧰 Summary Table

| ViewSet Class          | Included Mixins                         | Purpose                  |
| ---------------------- | --------------------------------------- | ------------------------ |
| `ProductListViewSet`   | `ListModelMixin` + `GenericViewSet`     | List all products        |
| `ProductCreateViewSet` | `CreateModelMixin` + `GenericViewSet`   | Create a new product     |
| `ProductDetailViewSet` | `RetrieveModelMixin` + `GenericViewSet` | Get single product       |
| `ProductUpdateViewSet` | `UpdateModelMixin` + `GenericViewSet`   | Update a product         |
| `ProductDeleteViewSet` | `DestroyModelMixin` + `GenericViewSet`  | Delete a product         |
| `ProductViewSet`       | `ModelViewSet`                          | Full CRUD out of the box |
