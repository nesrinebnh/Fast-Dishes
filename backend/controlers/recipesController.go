package controlers

import (
	"backend/database"
	"backend/models"

	"github.com/gofiber/fiber/v2"
)

func GetRecipes(c *fiber.Ctx) error {
	var recipes []models.Recipe

	database.DB.Find(&recipes)

	return c.JSON(recipes)
}

func AddRecipes(c *fiber.Ctx) error {
	var data map[string]string

	//Get the request data that we will send
	if err := c.BodyParser((&data)); err != nil {
		return err
	}

	recipe := models.Recipe{
		Title:       data["title"],
		Description: data["description"],
		ImageUrl:    data["url"],
	}

	database.DB.Create(&recipe)

	return c.JSON(recipe)
}
