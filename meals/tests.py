from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase

from recipes.models import RecipeIngredient, Recipe
from .models import Meal,MealStatus

User = get_user_model()


class MealTestCase(TestCase):
    def setUp(self):
        self.user_a =User.objects.create_user('shiva',password='shiva')
        self.user_id=self.user_a.id
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user=self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Grilled Chicken Tacos',
            user=self.user_a
        )
        self.recipe_c = Recipe.objects.create(
            name='Nachos',
            user=self.user_a
        )
        self.recipe_ingredient_a=RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound'
        )
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='asdfghjk',
            unit='pound'
        )
        self.meal=Meal.objects.create(
        user=self.user_a,
        recipe=self.recipe_a
        )
        meal_b=Meal.objects.create(
            user=self.user_a,
            recipe=self.recipe_a,
            status=MealStatus.COMPLETED
        )


    def test_pending_meals(self):
        qs=Meal.objects.all().pending()
        self.assertEqual(qs,count(),1)
        qs1=Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs1.count(),1)

    def test_completed_meals(self):
        qs = Meal.objects.all().completede()
        self.assertEqual(qs, count(), 1)
        qs1 = Meal.objects.by_user_id(self.user_id).completed()
        self.assertEqual(qs1.count(), 1)

    def test_add_item_via_toggle(self):
        meal_b=Meal.objects.create(
            user=self.user_a,
            recipes=self.recipe_a
        )
        qs1=Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs1.count(),2)
        added=Meal.objects.toggle_in_queue(self.user_id,self.recipe_c.id)
        qs2=Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs2.count(),3)
        self.assertTrue(added)

    def test_remove_item_via_toggle(self):
        added=Meal.objects.toggle_in_queue(self.user_id,self.recipe_a.id)
        qs2=Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs2.count(),2)
        self.assertTrue(added)


    def test_user_recipe_reverse_count(self):
        user=self.user_a
        qs=user.recipe_set.all()
        self.assertEqual(qs.count(),0)


    def test_user_recipe_forward_count(self):
        user=self.user_a
        qs=Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(),2)

    def test_user_ingredient_recipe_reverse_count(self):
        recipe=self.recipe_a
        qs=recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(),2)

    def test_user_ingredientcount(self):
        recipe=self.recipe_a
        qs=RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(),2)

    def test_user_two_level_relation(self):
        user=self.user_a
        qs=RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(),2)

    def test_user_two_level_relation_reverse(self):
        user=self.user_a
        recipeingredient_ids=list(user.recipe_set.all().values_list('recipeingredient__id',flat=True))
        qs=RecipeIngredient.objects.filter(id__in=recipeingredient_ids)
        self.assertEqual(qs.count(),2)

    def test_user_two_level_relation_via_recipes(self):
        user=self.user_a
        ids=user.recipe_set.all().values_list("id", flat=True)
        qs=RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(),2)

    def test_unit_measure_validation(self):
        invalid_unit='ounce'
        ingredient=RecipeIngredient(
            name='New',
            quantity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_units=['nada','asdfadsf']
        with self.assertRaises(ValidationError):
            for unit in invalid_units:
                ingredient=RecipeIngredient(
                    name='New',
                    quantity=10,
                    recipe=self.recipe_a,
                    unit=unit
                )
                ingredient.full_clean()

    def test_quantity_as_float(self):
        self.assertIsNotNull(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNull(self.recipe_ingredient_b.quantity_as_float)