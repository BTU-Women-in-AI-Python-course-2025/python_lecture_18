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

## 🔹 Overriding Mixin Methods

You can override the methods provided by the mixins inside your `ViewSet` to customize behavior.

---

### 📦 1. List View — `list(self, request, *args, **kwargs)`

```python
class ProductListViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "count": queryset.count(),
            "products": serializer.data
        })
```

---

### 🆕 2. Create View — `create(self, request, *args, **kwargs)`

```python
class ProductCreateViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data["message"] = "Product successfully created!"
        return response
```

---

### 🔍 3. Detail View — `retrieve(self, request, *args, **kwargs)`

```python
class ProductDetailViewSet(mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "product": serializer.data,
            "note": "Detailed view of a single product"
        })
```

---

### ✏️ 4. Update View — `update(self, request, *args, **kwargs)`

```python
class ProductUpdateViewSet(mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data["message"] = "Product successfully updated!"
        return response
```

---

### ❌ 5. Delete View — `destroy(self, request, *args, **kwargs)`

```python
class ProductDeleteViewSet(mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Product deleted successfully."})
```

---

### 🧩 6. Full CRUD — Override inside `ModelViewSet`

```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        return Response({"custom": "This is an overridden list method"})

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data["extra"] = "Created with ModelViewSet override"
        return response

    def retrieve(self, request, *args, **kwargs):
        return Response({"custom": "Overridden retrieve method"})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data["note"] = "Custom update logic applied"
        return response

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Deleted via overridden method"})
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
