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
