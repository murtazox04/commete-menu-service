from typing import List, Optional
from pydantic import parse_obj_as
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.api import schems
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import MenuCategory, Dish, DishParameter


class MenuCategoryDAO(BaseDAO[MenuCategory]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(MenuCategory, session)

    async def add_menu_category(
            self,
            menu_category: schems.MenuCategoryCreateUpdate
    ) -> dto.MenuCategory:
        async with self.session.begin():
            db_menu = MenuCategory(**menu_category.dict())
            self.session.add(db_menu)
        await self.session.refresh(db_menu)
        return db_menu

    async def get_menu_categories(self) -> List[dto.MenuCategory]:
        result = await self.session.execute(select(MenuCategory))
        menus = result.scalars().all()
        return parse_obj_as(List[dto.MenuCategory], menus)

    async def get_menu_category_by_id(self, menu_category_id: int) -> dto.MenuCategory:
        result = await self.session.execute(select(MenuCategory).where(MenuCategory.id == menu_category_id))
        return result.scalar_one_or_none()

    async def update_menu_category(
            self,
            menu_category_id: int,
            menu_category_update: schems.MenuCategoryCreateUpdate
    ) -> Optional[dto.MenuCategory]:
        result = await self.session.execute(select(MenuCategory).where(MenuCategory.id == menu_category_id))
        db_menu = result.scalar_one_or_none()
        if db_menu:
            for key, value in menu_category_update.dict().items():
                setattr(db_menu, key, value)
            await self.session.commit()
            await self.session.refresh(db_menu)
            return db_menu
        return None

    async def delete_menu_category(self, menu_category_id: int) -> bool:
        async with self.session.begin():
            result = await self.session.execute(select(MenuCategory).where(MenuCategory.id == menu_category_id))
            db_menu = result.scalar_one_or_none()
            if db_menu:
                await self.session.execute(delete(MenuCategory).where(MenuCategory.id == menu_category_id))
                await self.session.commit()
                return True
            return False


class DishDAO(BaseDAO[Dish]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Dish, session)

    async def add_dish(
            self,
            dish: schems.DishParameterCreateUpdate
    ) -> dto.Dish:
        db_dish = Dish(**dish.dict())
        self.session.add(db_dish)
        await self.session.commit()
        await self.session.refresh(db_dish)
        return db_dish

    async def get_dishes(self) -> List[dto.Dish]:
        result = await self.session.execute(select(Dish))
        dishes = result.scalars().all()
        return parse_obj_as(List[dto.Dish], dishes)

    async def get_dish_by_id(self, dish_id: int) -> Optional[dto.Dish]:
        result = await self.session.execute(select(Dish).where(Dish.id == dish_id))
        dish = result.scalar_one_or_none()
        if dish:
            return dish
        return None

    async def update_dish(
            self,
            dish_id: int,
            dish_update: schems.DishParameterCreateUpdate
    ) -> Optional[dto.Dish]:
        result = await self.session.execute(select(Dish).where(Dish.id == dish_id))
        db_dish = result.scalar_one_or_none()
        if db_dish:
            for key, value in dish_update.dict().items():
                setattr(db_dish, key, value)
            await self.session.commit()
            await self.session.refresh(db_dish)
            return db_dish
        return None

    async def delete_dish(self, dish_id: int) -> bool:
        result = await self.session.execute(select(Dish).where(Dish.id == dish_id))
        db_dish = result.scalar_one_or_none()
        if db_dish:
            await self.session.execute(delete(Dish).where(Dish.id == dish_id))
            await self.session.commit()
            return True
        return False


class DishParameterDAO(BaseDAO[DishParameter]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(DishParameter, session)

    async def add_product_parameter(
            self,
            product_parameter: schems.DishParameterCreateUpdate
    ) -> dto.DishParameter:
        db_product_parameter = DishParameter(**product_parameter.dict())
        self.session.add(db_product_parameter)
        await self.session.commit()
        await self.session.refresh(db_product_parameter)
        return db_product_parameter

    async def get_product_parameters(self) -> List[dto.DishParameter]:
        result = await self.session.execute(select(DishParameter))
        product_parameters = result.scalars().all()
        return parse_obj_as(List[dto.DishParameter], product_parameters)

    async def get_product_parameter_by_id(self, dish_parameter_id: int) -> Optional[dto.DishParameter]:
        result = await self.session.execute(select(DishParameter).where(DishParameter.id == dish_parameter_id))
        product_parameter = result.scalar_one_or_none()
        if product_parameter:
            return product_parameter
        return None

    async def update_product_parameter(
            self,
            product_parameter_id: int,
            product_parameter_update: schems.DishParameterCreateUpdate
    ) -> Optional[dto.DishParameter]:
        result = await self.session.execute(select(DishParameter).where(DishParameter.id == product_parameter_id))
        db_product_parameter = result.scalar_one_or_none()
        if db_product_parameter:
            for key, value in product_parameter_update.dict().items():
                setattr(db_product_parameter, key, value)
            await self.session.commit()
            await self.session.refresh(db_product_parameter)
            return db_product_parameter
        return None

    async def delete_product_parameter(self, product_parameter_id: int) -> bool:
        result = await self.session.execute(select(DishParameter).where(DishParameter.id == product_parameter_id))
        db_product_parameter = result.scalar_one_or_none()
        if db_product_parameter:
            await self.session.execute(delete(DishParameter).where(DishParameter.id == product_parameter_id))
            await self.session.commit()
            return True
        return False
