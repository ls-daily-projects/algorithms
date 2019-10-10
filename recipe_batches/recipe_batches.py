#!/usr/bin/python

import math

# Time => O(n), where n is recipe keys
# Space => O(1)


def recipe_batches(recipe, ingredients):
    actual_batch_count = math.inf

    for name, amount in recipe.items():
        ingredient_amount = ingredients.get(name)

        if not ingredient_amount:
            actual_batch_count = 0
            break

        batch_count = ingredient_amount // amount
        actual_batch_count = batch_count if actual_batch_count > batch_count else actual_batch_count

    return actual_batch_count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
