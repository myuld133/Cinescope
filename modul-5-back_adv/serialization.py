from pydantic import BaseModel, Field
from enum import Enum

class ProductType(str, Enum):
    ELECTRONIC = 'Электроника'
    CLOTHES = 'Одежда'
    FOOD = 'Еда'

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
    type: ProductType

product = Product(name='Клубника', price=299, in_stock=True, type=ProductType.FOOD)

# Сериализация (объект Python -> JSON)
json_data = product.model_dump_json()
print(json_data)

# Десериализация (JSON -> объект Python)
new_product = Product.model_validate_json(json_data)
print(new_product.name)