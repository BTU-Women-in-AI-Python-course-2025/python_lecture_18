# Django Rest Framework

- **Model Serializers** - https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
- **Dynamic Fields Serializer** - https://github.com/BTU-Women-AI-Python-course/Btu_Python_Lecture_17/blob/main/serializers.md#dynamic-fields
- **ViewSets** - https://www.django-rest-framework.org/api-guide/viewsets/:
- **SimpleRouter and DefaultRouter** - https://www.django-rest-framework.org/api-guide/routers/:
  - Automatically generate URL routing for your API.

### 📚 **Student Task: Build a Flexible API Using ViewSets and Dynamic Serializers**

1. **Create a model** (e.g., `Article` with `title`, `content`, `author`, `published`).

2. **Create a `ModelSerializer`** with **dynamic fields**:  
   - Allow the serializer to include only selected fields (e.g., via query params like `?fields=title,author`).

3. **Use a `ViewSet`** to handle all CRUD operations for the `Article` model.

4. **Use `DefaultRouter` or `SimpleRouter`** to auto-generate the routes.

---

#### 🔍 Example Output:
- `GET /articles/?fields=title,author` → returns only `title` and `author` for each article.
- `GET /articles/1/` → returns full details of article with ID 1.
- `POST /articles/` → creates a new article.
